from flask import Flask, url_for

app = Flask(__name__)


@app.route('/promotion_image')
def promotion():
    promotion_list = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    url_pic = url_for('static', filename='img/mars_1.gif')
    url_style = url_for('static', filename='css/style.css')
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{}" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert-dark" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-success" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-secondary" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-warning" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-danger" role="alert">
                      <br><h3>{}</h3>
                    </div>
                  </body>
                </html>""".format(url_style, url_pic, *promotion_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
