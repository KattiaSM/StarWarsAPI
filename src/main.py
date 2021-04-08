"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Favoritos, userFavoritos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def user():

    # get all the people
    user_query = User.query.all()

    # get only the ones named "Joe"
    #people_query = Person.query.filter_by(name='Joe')

    # map the results and your list of people  inside of the all_people variable
    all_user = list(map(lambda x: x.serialize(), user_query))

    return jsonify(all_user), 200

@app.route('/people', methods=['GET'])
def people():

    # get all the people
    people_query = People.query.all()

    # get only the ones named "Joe"
    #people_query = Person.query.filter_by(name='Joe')

    # map the results and your list of people  inside of the all_people variable
    all_people = list(map(lambda x: x.serialize(), people_query))

    return jsonify(all_people), 200

@app.route('/planets', methods=['GET'])
def planets():

    # get all the people
    planets_query = Planets.query.all()

    # get only the ones named "Joe"
    #people_query = Person.query.filter_by(name='Joe')

    # map the results and your list of people  inside of the all_people variable
    all_planets = list(map(lambda x: x.serialize(), planets_query))

    return jsonify(all_planets), 200

@app.route('/user_favoritos/<int:id>', methods=['GET'])
def user_favoritos():

    # get all the people
    user_favoritos_query = userFavoritos.query.all()

    # get only the ones named "Joe"
    #people_query = Person.query.filter_by(name='Joe')

    # map the results and your list of people  inside of the all_people variable
    all_userfavoritos = list(map(lambda x: x.serialize(), user_favoritos_query))

    return jsonify(all_userfavoritos), 200


@app.route('/favoritos', methods=['POST'])
def favoritos():

    request_body = request.get_json()
    fav = Favoritos(id_user=request_body["id_user"], fav_people=request_body["fav_people"], fav_planets=request_body["fav_planets"])
    db.session.add(fav)
    db.session.commit()

    return jsonify("Agregado a tus favoritos"), 200

@app.route('/delete_favoritos/<int:id>', methods=['DELETE'])
def delete_favoritos():

    fav = Favoritos.query.get(id)
    if fav is None:
        raise APIException('Favoritos not found', status_code=404)

    db.session.delete(fav)
    db.session.commit()

    return jsonify("Eliminado de tus favoritos"), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
