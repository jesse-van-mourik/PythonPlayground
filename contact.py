from flask import Blueprint, render_template

application = Blueprint('contact', __name__)


@application.route('/contact')
def show_contact_page():
    return render_template('contact.html')
