from flask import Blueprint, render_template

maps_bp = Blueprint('maps',__name__)

@maps_bp.route('/mappp')
def maps():
    return render_template("maps.html")