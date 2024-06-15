from flask import Blueprint, render_template

contacts_bp = Blueprint('contact_bp', __name__,
                        template_folder='templates',
                        static_folder='static',
                        url_prefix='/contacts')


@contacts_bp.route('/')
def contacts():
    title = 'Контакты - МВ проект \'Scripts DataBase\' - Камила Титова'
    return render_template('contacts/contacts.html', title=title)
