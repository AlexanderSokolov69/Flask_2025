import sys

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

API_KEY_STATIC = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'


class MainWindow(QMainWindow):
    g_map: QLabel
    g_search: QLineEdit
    g_layer1: QPushButton
    g_layer2: QPushButton
    press_delta = 0.1

    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)

        self.map_zoom = 10
        self.map_ll = [37.977751, 55.757718]
        self.map_key = ''
        self.theme = "light"

        # noinspection PyUnresolvedReferences
        self.g_search.returnPressed.connect(self.search)
        self.g_layer1.clicked.connect(self.set_layer1)
        self.g_layer2.clicked.connect(self.set_layer2)

        self.refresh_map()

    def set_layer1(self):
        self.theme = "light"
        self.refresh_map()

    def set_layer2(self):
        self.theme = "dark"
        self.refresh_map()

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key.Key_PageUp:
            if self.map_zoom < 17:
                self.map_zoom += 1
        elif key == Qt.Key.Key_PageDown:
            if self.map_zoom > 0:
                self.map_zoom -= 1
        elif key == Qt.Key.Key_Escape:
            self.g_map.setFocus()
        elif key == Qt.Key.Key_Right:
            self.map_ll[0] += self.press_delta
            if self.map_ll[0] > 180:
                self.map_ll[0] = self.map_ll[0] - 360
        elif key == Qt.Key.Key_Left:
            self.map_ll[0] -= self.press_delta
            if self.map_ll[0] < 0:
                self.map_ll[0] = self.map_ll[0] + 360
        elif key == Qt.Key.Key_Up:
            if self.map_ll[1] + self.press_delta < 90:
                self.map_ll[1] += self.press_delta
        elif key == Qt.Key.Key_Down:
            if self.map_ll[1] - self.press_delta > -90:
                self.map_ll[1] -= self.press_delta
        else:
            return

        self.refresh_map()

    def refresh_map(self):
        map_params = {
            "ll": ','.join(map(str, self.map_ll)),
            'z': self.map_zoom,
            'theme': self.theme,
            'apikey': API_KEY_STATIC,
        }
        response = make_request('https://static-maps.yandex.ru/v1', params=map_params)
        if not response:
            print('error: could not get map')
            return
        img = QImage.fromData(response.content)
        pixmap = QPixmap.fromImage(img)
        self.g_map.setPixmap(pixmap)

    def search(self):
        x, y = geo_locate(self.g_search.text())
        if x == -1 or y == -1:
            return
        self.map_ll = [x, y]
        self.refresh_map()


def geo_locate(name):
    params = {
        'apikey': '8013b162-6b42-4997-9691-77b7074026e0',
        'geocode': name,
        'format': 'json'
    }
    response = make_request('http://geocode-maps.yandex.ru/1.x/', params=params)
    if not response:
        print(f'error: could not get geo_locate object {name}')
        return -1, -1
    geo_objects = response.json()['response']["GeoObjectCollection"]["featureMember"]
    if not geo_objects:
        print('error: could not get geo_objects')
        return -1, -1
    return list(map(float, geo_objects[0]["GeoObject"]["Point"]["pos"].split()))


def make_request(*args, **kwargs):
    session = requests.Session()
    retry = Retry(total=10, connect=5, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session.get(*args, **kwargs)


def clip(v, _min, _max):
    if v < _min:
        return _min
    if v > _max:
        return _max
    return v


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
