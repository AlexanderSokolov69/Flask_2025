from flask import Flask
from flask_restful import Api

from data import jobs_resources, db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)


def main():
    db_session.global_init("db/mars_explorer.sqlite")

    api.add_resource(jobs_resources.JobsListResource, '/api/v2/jobs')  # для списка объектов
    api.add_resource(jobs_resources.JobsResource, '/api/v2/jobs/<int:job_id>')  # для одного объекта

    app.run()


if __name__ == '__main__':
    main()
