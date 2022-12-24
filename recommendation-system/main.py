from flask import Flask, request
from flask_restful import Api, Resource
from functions_package import collab_filtering_function, content_base_function

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():  
    return "Hello world!"


@app.route('/api/getSimilarProductsBasedUserByCBR', methods = ['POST'])
def getSimilarProductsBasedUserByCBR():
    data = {}
    results = []
    _json = request.json

    #Get Products
    products = _json['products']

    #Get User
    user = _json['user']

    #Get similar products by CBR
    results = content_base_function.content_base_recommendation(products, user)

    data['result'] = results
    print('Finished calculate similarities')
    return data
    
    
@app.route('/api/getSimilarProductsByCFR', methods = ['POST'])
def getSimilarProductsByCFR():
    data = {}
    results = []
    _json = request.json

    #Get Products
    products = _json['products']

    #Get Users
    users = _json['users']

    #Get User
    user = _json['user']

    #Get similar products by FR
    results = collab_filtering_function.collab_filtering_recommendation(products, users, user)

    data['result'] = results
    print('Finished calculate similarities')
    return data

@app.route('/api/getSimilarProductBySelectedProduct', methods = ['POST'])
def getSimilarProductBySelectedProduct():
    data = {}
    results = []
    _json = request.json

    #Get Products
    products = _json['products']

    #Get Product
    product = _json['product']

    #Get similar products by FR
    results = content_base_function.getSimilarProductsBySelectedProduct(products, product)

    data['result'] = results
    print('Finished calculate similarities')
    return data

if __name__ == "__main__":
    app.run(debug=True)