from flask import render_template, Blueprint

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def index():
    return render_template('api.html', title='API Reference')