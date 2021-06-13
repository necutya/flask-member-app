from datetime import datetime

from flask import Blueprint, request, jsonify, make_response
from flask import current_app as app
from flask import render_template
from .models import members
from .forms import RegistrationForm

from .utils import is_email_unique

member_bp = Blueprint(
    "member_bp", __name__, url_prefix='',
    template_folder="templates", static_folder="static", static_url_path='%s/member_bp' % app.static_url_path
)


@member_bp.route("/", methods=["GET", "POST"])
def index():
    """
    View to show members table and create new members via ajax
    """
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if is_email_unique(members, form.email.data):
                return make_response(jsonify({
                    'status': 'fail',
                    'message': 'Please, check correctness of your data.',
                    'errors': {
                        'email': ['Member with this email has been already registered. Please, use another one.']
                    }
                }), 403)

            members.append({
                'name': form.name.data,
                'email': form.email.data,
                'registration_date': datetime.now().strftime('%d-%m-%Y'),

            })
            return make_response(jsonify({
                'status': 'success',
                'message': 'Member has been added successfully.',
                'user_data': {
                    'name': members[-1]['name'],
                    'email': members[-1]['email'],
                    'registration_date': members[-1]['registration_date'],
                    'index': len(members),
                }
            }), 200)
        else:
            print(form.errors)
            return make_response(jsonify({
                'status': 'fail',
                'message': 'Please, check correctness of your data.',
                'errors': form.errors
            }), 403)

    return render_template(
        "index.html",
        title="Flask Member Club",
        members=members,
        form=form
    )
