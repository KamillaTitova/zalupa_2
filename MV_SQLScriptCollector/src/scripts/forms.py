from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, validators
from wtforms.widgets.core import TextArea

from src.scripts.models import Script


def get_choices(users):
    all_users = users.query.all()
    return [(user.id, user.email) for user in all_users]


class AddScriptForm(FlaskForm):
    name = StringField("Название скрипта", [validators.Length(max=64), validators.DataRequired()])
    description = StringField("Описание скрипта", [validators.Length(max=128)])
    code = TextAreaField("Код скрипта", [validators.Length(max=4096), validators.DataRequired()],
                         widget=TextArea())
    user_id = SelectField("Автор SQL скрипта", [validators.Optional()])

    def validate(self, extra_validators=None):
        initial_validation = super(AddScriptForm, self).validate(extra_validators)
        if not initial_validation:
            return False
        script = Script.query.filter_by(name=self.name.data).first()
        if script:
            self.name.errors.append("Script already added")
            return False
        return True
