from flask import Flask
from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(input())

    session = create_session()
    # dictionary of job_id and len of collaboration
    collaborations = {x.id: len(x.collaborators.split())
                      for x in session.query(Jobs).all()}

    max_size = max(collaborations.values())
    # job_id if len collaboration is max
    ids = [x for x in collaborations if collaborations[x] == max_size]

    # teamleader id if job id in ids
    temp = [x.team_leader for x in session.query(Jobs).all() if x.id in ids]

    # result
    teamleaders = session.query(User).filter(User.id.in_(temp)).all()

    for member in teamleaders:
        print(member.name, member.surname)


if __name__ == '__main__':
    main()
