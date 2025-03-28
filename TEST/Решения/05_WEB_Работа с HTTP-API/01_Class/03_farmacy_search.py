import sys

from business import find_business
from distance import lonlat_distance
from geocoder import get_coordinates
from mapapi_PG import show_map


def main():
    toponym_to_find = " ".join(sys.argv[1:])

    lat, lon = get_coordinates(toponym_to_find)
    address_ll = f"{lat},{lon}"
    span = "0.005,0.005"

    # Получаем координаты ближайшей аптеки.
    organization = find_business(address_ll, span, "аптека")
    point = organization["geometry"]["coordinates"]
    org_lat = float(point[0])
    org_lon = float(point[1])
    point_param = f"pt={org_lat},{org_lon},pm2dgl"

    show_map(f"ll={address_ll}&spn={span}", add_params=point_param)

    # Добавляем на карту точку с исходным адресом.
    points_param = point_param + f"~{address_ll},pm2rdl"

    show_map(f"ll={address_ll}&spn={span}", add_params=points_param)

    # Автопозиционирование
    show_map("", add_params=points_param)

    # Сниппет
    # Название организации.
    name = organization["properties"]["CompanyMetaData"]["name"]
    # Адрес организации.
    address = organization["properties"]["CompanyMetaData"]["address"]
    # Время работы
    time = organization["properties"]["CompanyMetaData"]["Hours"]["text"]
    # Расстояние 
    distance = round(lonlat_distance((lon, lat), (org_lon, org_lat)))

    snippet = f"Название:\t{name}\nАдрес:\t{address}\nВремя работы:\t{time}\n" \
              f"Расстояние:\t{distance}м."
    print(snippet)


if __name__ == "__main__":
    main()
