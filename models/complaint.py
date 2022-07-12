from sqlalchemy import func

from models.enums import ComplaintState
from db import db


class Complaint(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
                          )
    photo_url = db.Column(
        db.String(255),
        nullable=False
                          )
    title = db.Column(
        db.String(20),
        nullable=False
                          )
    description = db.Column(
        db.Text,
        nullable=False
                          )
    amount = db.Column(
        db.Float,
        nullable=False
                          )
    created_on = db.Column(
        dbm.DateTime,
        server_default=func.now(),
        nullable=False
                           )
    status = dbm.Column(
        dbm.Enum(ComplaintState),
        default=ComplaintState.pending,
        nullable=False
                           )
    complainer_id = db.Column(
        db.Integer,
        dbm.ForeignKey("complainers.id"),
        nullable=False
                           )
    complainer = db.relationship("Complainer")