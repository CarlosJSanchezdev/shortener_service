from . import db

class Link(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    original_url = db.Column(db.String(500),nullable=False)
    short_code = db.Column(db.String(10),unique=True,nullable=False)
    clicks = db.relationship('Click', backref='link', lazy=True)

class Click(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    Link_id = db.Column(db.Integer, primary_key=True)
    Link_id =db.Column(db.Integer, db.ForeignKey('link.id'), nullable=False)
    click_time = db.Column(db.DateTime, nullable=False, default=db.func.now())
    ip_address = db.Column(db.String(50),nullable=False)
    user_agent = db.Column(db.String(200),nullable=False)
