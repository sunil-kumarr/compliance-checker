from flask import Flask
from views import aiBlueprint
import settings

app = Flask(__name__)
app.register_blueprint(aiBlueprint)
     