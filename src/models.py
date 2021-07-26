from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    lastName = db.Column(db.String(120), unique=False, nullable=False)
    team = db.Column(db.String(120), unique=False, nullable=False),
    age = db.Column(db.Integer, unique=False, nullable=False),
    birthday = db.Column(db.String(20), unique=False, nullable=False)
    generations = db.relationship('Generation', backref='member', lazy=True)

    def __repr__(self):
        return '<Member %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastName": self.lastName,
            "team": self.team,
            "age": self.name,
            "birthday": self.birthday
            # do not serialize the password, its a security breach
        }

class Generation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<Generation %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
