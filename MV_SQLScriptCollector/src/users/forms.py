from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, IntegerField, validators
from wtforms.validators import DataRequired, Email, EqualTo, Length

from src.users.models import User


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField("Имя", [validators.Length(max=40)])
    email = EmailField(
        "Email", validators=[DataRequired(), Email(message=None), Length(max=40)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=25)]
    )
    confirm = PasswordField(
        "Repeat password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    mv_user_id = IntegerField("Internal MVideo UserID", validators=[DataRequired()])

    def validate(self, extra_validators=None):
        initial_validation = super(RegisterForm, self).validate(extra_validators)
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append("Passwords must match")
            return False
        return True
