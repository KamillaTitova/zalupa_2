from flask import Blueprint, render_template, request
from flask_login import login_required

from src.folders.models import Folder
from src.users.models import User
from src.scripts.models import Script

from src.scripts.forms import AddScriptForm
from src.users.models import User

core_bp = Blueprint('core', __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/core/static'
                    )


@core_bp.route('/')
# @login_required
def home():
    title = 'Главная - МВ проект \'Scripts DataBase\' - Камила Титова'
    folders = Folder.query.all()
    for folder in folders:
        users = User.query.filter_by(folder_id=folder.id).all()
        for user in users:
            scripts = Script.query.filter_by(user_id=user.id).all()
            print(user.scripts)
            # print(folder.folder_name, users, scripts)
    if folders:
        return render_template('core/index.html', folders=folders, scripts=scripts, title=title)
    return render_template('core/index.html', title=title)

