from flask import jsonify, Blueprint, render_template
from flask_cors import CORS
from .models import Project

api_bp = Blueprint('api', __name__)
CORS(api_bp)

@api_bp.route('/', methods=['GET'])
def api():
    return render_template('api.html', title='API Reference') 

@api_bp.route('/projects', methods=['GET'])
def projects():

    projects = [i.serialize() for i in Project.query.all()]
    
    return jsonify(projects)

@api_bp.route('/projects/<category>', methods=['GET'])
def projects_filtered(category=None):

    projects = [i.serialize() for i in Project.query.filter_by(category=category)]

    return jsonify(projects)