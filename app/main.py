from flask import Blueprint, render_template as render

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render('index.html')
