from flask import Flask
from config import config
from routes import Footballer


app = Flask(__name__)

def page_not_found():
    return "Page not found",404
    
if __name__ == '__main__':
    app.config.from_object(config['development'])
    #Blueprints donde asigno rutas
    app.register_blueprint(Footballer.main, url_prefix='/api/footballers')
    #Manejador de errores 
    app.register_error_handler(404, page_not_found)
    app.run()