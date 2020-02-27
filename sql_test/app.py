from flask import Flask
import config
from exts import db
from apps.views import cms_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(cms_bp)

    db.init_app(app)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True,port=8000)
