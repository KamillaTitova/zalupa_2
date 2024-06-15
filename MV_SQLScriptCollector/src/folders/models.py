from mixins import TimestampMixin
from src import db


class Folder(TimestampMixin, db.Model):

    __tablename__ = "folders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    folder_name = db.Column(db.String, nullable=False, default="Undefined")
    private = db.Column(db.Boolean, nullable=False, default=False)
    users = db.relationship("User", back_populates="folder", lazy="select")

    def __init__(self, folder_name="Undefined", private=False):
        self.folder_name = folder_name
        self.private = private

    def __str__(self):
        return f"Folder name: {self.folder_name}"
