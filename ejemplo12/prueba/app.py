from flask import Flask
from blueprint_app import app_bp

app = Flask(__name__)
app.register_blueprint(app_bp)

if __name__ == '__main__':
    app.run(debug=True)