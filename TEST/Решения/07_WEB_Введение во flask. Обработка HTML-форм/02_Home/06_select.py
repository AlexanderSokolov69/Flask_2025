from flask import Flask

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def choice(planet_name):
    choice_list = [
        'Эта планета близка к Земле;',
        'На ней много необходимых ресурсов;',
        'На ней есть вода и атмосфера;',
        'На ней есть небольшое магнитное поле;',
        'Наконец, она просто красива!'
    ]
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {}</h1>
                    <h3>{}</h3>
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
                </html>""".format(planet_name, *choice_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
