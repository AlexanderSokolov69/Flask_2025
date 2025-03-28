from flask import jsonify, Blueprint, request, make_response
from werkzeug.security import generate_password_hash

from data import db_session
from data.users import User

blueprint = Blueprint('users_api', __name__, template_folder='templates')


def set_password(password):
    return generate_password_hash(password)


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify({'users': [item.to_dict(
        only=('id', 'name', 'surname', 'age', 'position',
              'speciality', 'address', 'email', 'hashed_password', 'city_from')
    )
        for item in users]})


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(user_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify({'users': users.to_dict(
        only=('id', 'name', 'surname', 'age', 'position',
              'speciality', 'address', 'email', 'hashed_password',
              'city_from')
    )})


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in ['name', 'surname', 'age', 'position',
                                                 'speciality', 'address', 'email',
                                                 'hashed_password']):
        return make_response(jsonify({'error': 'Bad request'}), 400)

    db_sess = db_session.create_session()
    users = User(
        name=request.json['name'],
        surname=request.json['surname'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
        hashed_password=set_password(request.json['hashed_password']),
        city_from=request.json['city_from']
    )

    db_sess.add(users)
    db_sess.commit()
    return jsonify({'id': users.id})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(user_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 400)
    db_sess.delete(users)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['POST'])
def edit_user(user_id):
    db_sess = db_session.create_session()
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in ['name', 'surname', 'age', 'position',
                                                 'speciality', 'address', 'email',
                                                 'hashed_password']):
        return make_response(jsonify({'error': 'Bad request'}), 400)

    users = User(
        name=request.json['name'],
        surname=request.json['surname'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
        hashed_password=set_password(request.json['hashed_password']),
        city_from=request.json['city_from']
    )
    user_to_edit = db_sess.query(User).filter(User.id == user_id).first()
    if not user_to_edit:
        return make_response(jsonify({'error': 'Not found'}), 404)
    if user_to_edit:
        user_to_edit.name = users.name
        user_to_edit.surname = users.surname
        user_to_edit.age = users.age
        user_to_edit.position = users.position
        user_to_edit.speciality = users.speciality
        user_to_edit.address = users.address
        user_to_edit.email = users.email
        user_to_edit.hashed_password = set_password(users.hashed_password)
        user_to_edit.city_from = users.city_from
    db_sess.commit()
    return jsonify({'success': 'OK'})
