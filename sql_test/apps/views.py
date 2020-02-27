from flask import Blueprint,render_template

cms_bp = Blueprint("cms",__name__,url_prefix='/')

@cms_bp.route('/')
def index():
    return render_template("index.html")