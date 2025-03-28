from flask import Flask, url_for

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {}:</h2>
                    <div class="alert-success" role="alert">
                      <br><h3>Поздравляем! Ваш рейтинг после {} этапа отбора</h3>
                    </div>
                    <br><h3>составляет {}!</h3>
                    <div class="alert-warning" role="alert">
                       <br><h2>Желаем удачи!</h2>
                    </div>
                  </body>
                </html>""".format(nickname, level, rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
