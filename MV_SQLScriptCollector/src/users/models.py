from datetime import datetime

from flask_login import UserMixin

from mixins import TimestampMixin
from src import bcrypt, db
from src.folders.models import Folder


class User(TimestampMixin, db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    name = db.Column(db.String, unique=True, nullable=False)
    mv_user_id = db.Column(db.Integer, unique=True, index=True, nullable=False)
    email = db.Column(db.String, unique=True, index=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    last_login_on = db.Column(db.DateTime, default=datetime.now())
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    allow_add = db.Column(db.Boolean, nullable=False, default=True)
    allow_see_others = db.Column(db.Boolean, nullable=False, default=True)
    allow_edit_others = db.Column(db.Boolean, nullable=False, default=False)
    allow_delete_others = db.Column(db.Boolean, nullable=False, default=False)
    scripts = db.relationship("Script", back_populates="user", lazy="dynamic")
    folder_id = db.Column(db.Integer, db.ForeignKey(Folder.id), default=1)
    folder = db.relationship("Folder", back_populates="users", lazy="select")

    def __init__(self, name, mv_user_id, email, password, last_login_on=None, is_admin=False, allow_add=True,
                 allow_see_others=True, allow_edit_others=False, allow_delete_others=False, folder_id=1):
        self.name = name
        self.mv_user_id = mv_user_id
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.last_login_on = last_login_on
        self.is_admin = is_admin
        self.allow_add = allow_add
        self.allow_see_others = allow_see_others
        self.allow_edit_others = allow_edit_others
        self.allow_delete_others = allow_delete_others
        self.folder_id = folder_id

    # def __repr__(self):
    #     return f"<Email {self.email}>, Scripts {self.scripts}"

    def __str__(self):
        # return f"Name: {self.name}, MV UserID: {self.mv_user_id}"
        return f"ID: {self.id}, Name: {self.name}, Scripts: {self.scripts}"
