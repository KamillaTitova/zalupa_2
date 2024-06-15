from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

from src import db
from src.folders.forms import AddFolderForm
from src.folders.models import Folder

folders_bp = Blueprint('folders', __name__,
                       template_folder='templates',
                       static_folder='static',
                       url_prefix='/folders')


@folders_bp.route('/', methods=['GET'])
@login_required
def folders_list():
    title = 'Список папок - МВ проект \'Scripts DataBase\' - Камила Титова'
    if current_user.is_authenticated:
        folders = Folder.query.all()
        return render_template('folders/folders_list.html', title=title, folders=folders)
    else:
        flash("You do not have permission to view this page.", "danger")
    return render_template('core/index.html', title=title)


@folders_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_folder():
    if current_user.allow_add:
        form = AddFolderForm(request.form)
        if form.validate_on_submit():
            folder = Folder(folder_name=form.folder_name.data, private=form.private.data)
            db.session.add(folder)
            db.session.commit()
            flash(f"Department folder \"{form.folder_name.data}\" was successfully added to DB", "success")
            return redirect(url_for("folders.folders_list"))
        return render_template("folders/add_folder.html", form=form)
    else:
        flash("You do not have permissions to add department.", "danger")
        return render_template("core/index.html")
