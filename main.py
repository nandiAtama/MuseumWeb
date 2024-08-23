from flask import Flask
from controllers.home import home_bp
from controllers.about import about_bp
from controllers.maps import maps_bp

app = Flask(__name__, template_folder = "template")

app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(maps_bp)

if __name__ == '__main__':
    app.run()
