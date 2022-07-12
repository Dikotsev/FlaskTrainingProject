from models.enums import UserRole
from db import db



class BaseUser(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(250), nullable=False)


class Complainer(BaseUser):
    __tablename__ = "complainers"
    complains = db.relationship("Complaint", backref="complaint", lazy="dynamic")
    role = db.Column(db.Enum(UserRole), default=UserRole.complainer, nullable=False)


class Approval(BaseUser):
    __tablename__ = "approvals"
    role = db.Column(db.Enum(UserRole), default=UserRole.approval, nullable=False)


class Admin(BaseUser):
        __tablename__ = "admin"
        role = db.Column(db.Enum(UserRole), default=UserRole.admin, nullable=False)
