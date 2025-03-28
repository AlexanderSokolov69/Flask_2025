from flask import Flask
from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# ##### Это надо отправить -- начало{
def main():
    global_init(input())

    session = create_session()

    for job in session.query(Jobs).filter((Jobs.work_size < 20),
                                          Jobs.is_finished == 0):
        print(job)


if __name__ == '__main__':
    main()
# ##### Это надо отправить -- конец}