import getpass
from dotenv import load_dotenv
from flask.cli import FlaskGroup

from src import app, db
from src.users.models import User

load_dotenv()
cli = FlaskGroup(app)


@cli.command("create_admin")
def create_admin():
    """Creates the admin user."""
    name = input("Enter admin name: ")
    email = input("Enter email address: ")
    mv_user_id = input("Enter internal MVideo UserID:")
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Enter password again: ")
    if password != confirm_password:
        print("Passwords don't match")
        return 1
    try:
        user = User(name=name,
                    email=email,
                    mv_user_id=mv_user_id,
                    password=password,
                    is_admin=True,
                    allow_add=True,
                    allow_see_others=True,
                    allow_edit_others=True,
                    allow_delete_others=True,
                    )
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(f"Couldn't create admin user. Some error occurred - {e}")


if __name__ == "__main__":
    cli()
