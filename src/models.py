from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    birth_year = db.Column(db.String(120), unique=False)
    eye_color = db.Column(db.String(120))
    gender = db.Column(db.String(120))
    hair_color = db.Column(db.String(120))
    height = db.Column(db.String(120))
    mass = db.Column(db.String(120))
    skin_color = db.Column(db.String(120))
    homeworld = db.Column(db.String(120))
    
    def __repr__(self):
        return '<People %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "homeworld": self.homeworld,   
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.String(120))
    rotation_period = db.Column(db.String(120))
    orbital_period = db.Column(db.String(120))
    population = db.Column(db.String(120))
    climate = db.Column(db.String(120))
    terrain = db.Column(db.String(120))
    surface_water = db.Column(db.String(120))
    
    def __repr__(self):
        return '<Planets %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,  
        }

class userFavoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))

    def __repr__(self):
        return '<userFavoritos %r>' % self.username

    def serialize(self):
        return {
            "id_user": self.id_user,
            "id_people": self.id_people,
            "id_planets": self.id_planets, 
        }

class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    fav_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    fav_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))

    def __repr__(self):
        return '<Favoritos %r>' % self.username

    def serialize(self):
        return {
            "id_user": self.id_user,
            "fav_people": self.fav_people,
            "fav_planets": self.fav_planets, 
        }

