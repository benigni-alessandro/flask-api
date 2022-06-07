import imp
from re import I
from flask import Blueprint
from flask import jsonify
from flask import request
from models.FootballerModel import FootballerModel
from models.entities.Footballer import Footballer

main = Blueprint('footballers_blueprint', __name__)

messagerror_filter = '''Non hai passato i parametri correti nella url: [*] inserire role=<id del ruolo che vuoi filtrare> se vuoi filtrare per piu ruoli separali per una virgola [*] inserire rarity=<id di rarity che vuoi filtrare> se vuoi filtrare per piu rarity separali per una virgola'''
#creo la ruta principal
@main.route('/')
def get_footballers():
    try:
        footballers = FootballerModel.get_footballers()
        return jsonify(footballers)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_footballer(id):
    try:
        footballer = FootballerModel.get_footballer(id)
        if footballer != None:
            return footballer.convert_to_json()
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_footballer():
    try:
        name = request.json['name']
        role = request.json['role']
        rarity =request.json['rarity']
        price = request.json['price']
        quantity= request.json['quantity'] 
        affected_rows = FootballerModel.add_footballer(name,role,rarity,price,quantity)
        if affected_rows == 1:
            return jsonify({'message': 'Footballer inserted'})
        else:
            return jsonify({'message': 'Error on insert'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/filter-price/disc')
def ord_desc_price():
    try:
        footballers = FootballerModel.get_footballers_prices_disc()
        return jsonify(footballers)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/filter-price/asc')
def ord_asc_price():
    try:
        footballers = FootballerModel.get_footballers_prices_asc()
        return jsonify(footballers)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/filter-quantity/disc')
def ord_desc_quantity():
    try:
        footballers = FootballerModel.get_footballers_quantity_disc()
        return jsonify(footballers)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/filter-quantity/asc')
def ord_asc_quantity():
    try:
        footballers = FootballerModel.get_footballers_quantity_asc()
        return jsonify(footballers)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


#roles and rarity
# GET requests will be blocked
@main.route('/json-filter')
def filter_role_rarity():
    request_data = request.args
    role = None
    rarity = None
    is_role = False
    is_rarity = False
    roles_arr=[]
    rarity_arr=[]
    try:
        if request_data:
            try:
                if 'role' in request_data:
                    role = request_data['role']
                    role = str(role)
                    role =role.split(',')
                    for i in range(len(role)):
                        roles_arr.append(role[i])
                    is_role=True
                if 'rarity' in request_data:
                    rarity = request_data['rarity']
                    rarity = str(rarity)
                    rarity = rarity.split(',')
                    for i in range(len(rarity)):
                        rarity_arr.append(rarity[i])
                    is_rarity=True

                if is_role == True:
                    footballers = FootballerModel.get_footballers_role(roles_arr)
                if is_rarity == True:
                    footballers = FootballerModel.get_footballers_rarity(rarity_arr)
                
                return jsonify(footballers)
                
            except Exception as ex:
                return jsonify({'message': messagerror_filter}), 500
    except Exception as ex:
        return jsonify({'message': messagerror_filter}), 400