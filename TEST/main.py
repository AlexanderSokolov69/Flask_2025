# noinspection PyUnresolvedReferences
import json

from flask import Flask, render_template, url_for, redirect

from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def train(prof):
    param = {}
    if 'инженер'in prof or 'строитель' in prof:
        param['naim'] = 'Инженерные тренажеры'
        param['pic'] = url_for('static', filename='img/ing.png')
    else:
        param['naim'] = 'Научные тренажеры'
        param['pic'] = url_for('static', filename='img/sci.png')
    return render_template('train.html', **param)


@app.route('/list_prof/<lst>')
def list_prof(lst):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    return render_template('list_prof.html', list=lst, professions=professions)


if __name__ == '__main__':
    app.run(port=8080, host='172.16.1.33')
