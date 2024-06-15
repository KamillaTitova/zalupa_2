from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.fields.choices import RadioField
from wtforms.fields.simple import BooleanField
from wtforms.validators import InputRequired

from src.folders.models import Folder


class AddFolderForm(FlaskForm):
    folder_name = StringField("Название отдела", [validators.Length(max=64), validators.DataRequired()])
    private = RadioField("Закрытая папка",
                         choices=[(1, "Да"),
                                  (0, "Нет")],
                         coerce=int,
                         validators=[InputRequired(message="Выберите режим папки отдела")],
                         default=0)

    def validate(self, extra_validators=None):
        initial_validation = super(AddFolderForm, self).validate(extra_validators)
        if not initial_validation:
            return False
        script = Folder.query.filter_by(folder_name=self.folder_name.data).first()
        if script:
            self.folder_name.errors.append("Department already added")
            return False
        return True
