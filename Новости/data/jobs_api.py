import flask
from flask import jsonify, make_response, request

from . import db_session
from .jobs_data import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=['GET'])
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return make_response(jsonify(
        {
            'jobs': [item.to_dict(only=['id', 'team_leader', 'job', 'work_size',
                                        'collaborators', 'start_date', 'end_date',
                                        'is_finished']) for item in jobs]
        }
    ), 200)


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_job(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Jobs not found'}), 404)
    return jsonify(
        {
            'jobs': jobs.to_dict(only=['id', 'team_leader', 'job', 'work_size',
                                        'collaborators', 'start_date', 'end_date',
                                        'is_finished'])
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    print(request.json)
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    jobs = Jobs(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators']
    )
    start_date = request.json.get('start_date', None)
    end_date = request.json.get('end_date', None)
    is_finished = request.json.get('is_finished', None)
    if start_date:
        jobs.start_date = start_date
    if end_date:
        jobs.end_date = end_date
    if is_finished:
        jobs.is_finished = is_finished
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'id': jobs.id})

