from flask import Flask

from data.news import News
from data.users import User
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # app.run()
    # user = User()
    # user.name = "Пользователь "
    # user.about = "биография пользователя 1"
    # user.email = "email@email.ru"
    db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
    user = db_sess.query(User).first()
    print(user.name)
    for user in db_sess.query(User).all():
        print(user)
    for user in db_sess.query(User).filter(User.id > 1, User.email.notilike("%1%")):
        print(user)
    db_sess.query(User).filter(User.id >= 2).delete()
    db_sess.commit()
    news = News(title="Первая новость", content="Привет блог!", user_id=1, is_private=False)
    db_sess.add(news)
    db_sess.commit()
    user = db_sess.query(User).filter(User.id == 1).first()
    news = News(title="Вторая новость", content="Уже вторая запись!", user=user, is_private=False)
    db_sess.add(news)
    db_sess.commit()


if __name__ == '__main__':
    main()
