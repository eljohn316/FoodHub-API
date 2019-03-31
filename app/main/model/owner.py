from .. import db, flask_bcrypt

class Owner(db.Model):
    """ Owner Model for storing owner related details """
    __tablename__ = "owner"

    owner_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.String(11))
    gender = db.Column(db.String(6), nullable=False)
    password_hash = db.Column(db.String(80))
    #restaurants = db.relationship('Restaurant', backref='restaurant_owner')

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Owner '{}'>".format(self.username)