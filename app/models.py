from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import login


@login.user_loader
def load_user(id):
    return Therapist.query.get(int(id))


class PatientsStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10), index=True, unique=True)


class Therapist(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(16), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    tz_id = db.Column(db.String(9), index=True, nullable=False)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)

    phone = db.Column(db.String(15))
    address_city = db.Column(db.String(64))
    address_street = db.Column(db.String(64))
    address_house_num = db.Column(db.String(64))
    houses = db.relationship('House', backref='therapist', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Therapist {}>'.format(self.username)


class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    main_first_name = db.Column(db.String(64), nullable=False)
    main_last_name = db.Column(db.String(64), nullable=False)
    main_birth_year = db.Column(db.Integer)
    main_phone = db.Column(db.String(15))
    main_is_dutch = db.Column(db.Boolean)
    main_status_id = db.Column(db.Integer, db.ForeignKey('patients_status.id'))

    second_first_name = db.Column(db.String(64))
    second_last_name = db.Column(db.String(64))
    second_birth_year = db.Column(db.Integer)
    second_phone = db.Column(db.String(15))
    second_is_dutch = db.Column(db.Boolean)
    second_status_id = db.Column(db.Integer, db.ForeignKey('patients_status.id'))

    address_city = db.Column(db.String(64), nullable=False)
    address_street = db.Column(db.String(64), nullable=False)
    address_house_num = db.Column(db.String(64), nullable=False)

    therapist_id = db.Column(db.Integer,
                             db.ForeignKey('therapist.id'),
                             nullable=False)

    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint(main_first_name,
                                          main_last_name,
                                          address_city,
                                          address_street,
                                          address_house_num),)

    def __repr__(self):
        return '<House {}>'.format(self.main_first_name, self.main_last_name)
