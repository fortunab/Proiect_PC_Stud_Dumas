from app import db
from flask_login import UserMixin
from sqlalchemy.exc import IntegrityError

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    lastn = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, name, lastn, username, email, password):
        self.name = name
        self.lastn = lastn
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r - %s>' % (self.id) % (self.email)

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return self

class Server(UserMixin, db.Model):
    __tablename__ = 'server'
    id_serv = db.Column(db.Integer, primary_key=True)
    name_serv = db.Column(db.String(15), unique=True, nullable=False)
    ip_serv = db.Column(db.String(20), nullable=False)
    port_serv = db.Column(db.String(6), unique=True, nullable=False)
    username_fk = db.Column(db.Integer, db.ForeignKey('user.username'), nullable=False)

    def __init__(self, name_serv, ip_serv, port_serv, username_fk):
        self.name_serv = name_serv
        self.ip_serv = ip_serv
        self.port_serv = port_serv
        self.username_fk = username_fk

    def __repr__(self):
        return '<Server %r>' % (self.id_serv)

    def save1(self):
        db.session.add(self)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return self 

    def rmv(self):
        db.session.delete(self)
        db.session.commit()
        return self
