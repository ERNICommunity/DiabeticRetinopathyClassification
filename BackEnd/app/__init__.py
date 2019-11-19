from flask import Flask
from flask_cors import CORS
from app.retinopathy_classification.retinopathy_classification_controller import retinopathy_classification_module


app = Flask(__name__)
CORS(app)

# Configurations
app.config.from_object('config')

# Register blueprint(s)
app.register_blueprint(retinopathy_classification_module)
