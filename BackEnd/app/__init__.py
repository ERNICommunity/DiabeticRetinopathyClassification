from flask import Flask
from flask_cors import CORS
from app.retinopathy_classification.retinopathy_classification_controller import retinopathy_classification_module


application = Flask(__name__)
CORS(application, resources={r"/*": {"origins": "*"}})

# Configurations
application.config.from_object('config')

# Register blueprint(s)
application.register_blueprint(retinopathy_classification_module)
