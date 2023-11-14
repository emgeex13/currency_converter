from flask import Flask, request, jsonify, render_template,json 
import requests
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():

    if request.method == 'POST':
        # response = get_res()
        # print("fgdsgD: ",response)
        data = request.get_json(force=True)
        source_currency = data['queryResult']['parameters']['unit-currency']['currency']
        amount = data['queryResult']['parameters']['unit-currency']['amount']
        target_currency = data['queryResult']['parameters']['currency-name']

    
        factor = requests.get('https://open.er-api.com/v6/latest/USD').json()
        # print(rate)
    
        rate = factor['rates'][target_currency] / factor['rates'][source_currency]
        value = amount * rate
        value = round(value, 2)

        print(f"{amount} {source_currency} is equal to {value} {target_currency}!")

        response = {'fulfillmentText': f"{amount} {source_currency} is equal to {value} {target_currency}!"} 
        return jsonify(response)
    
    if request.method == 'GET':
        return render_template('index.html')

def get_res():
    # # data = request.get_json(silent=True)
    # data = json.loads(request.data)
    # # source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    # amount = data['queryResult']['parameters']['unit-currency']['amount']
    # target_currency = data['queryResult']['parameters']['currency-name']
    source_currency = "INR"
    amount = 600
    target_currency = "USD"
    
    # get request from api
    # get the conversion rate
    # convert the amount
    factor = requests.get('https://open.er-api.com/v6/latest/USD').json()
    # print(rate)
   
    rate = factor['rates'][target_currency] / factor['rates'][source_currency]
    value = amount * rate
    value = round(value, 2)

    print(f"{amount} {source_currency} is equal to {value} {target_currency}!")

    response = {'fulfillmentText': f"{amount} {source_currency} is equal to {value} {target_currency}!"}
    # response = jsonify(response)
    return response

@app.route('/webhook', methods=['POST'])
def webhook():
    # response = request.get_json(force=True)
    # response = jsonify(response)   
    data = request.get_json(force=True)
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
       
   
    factor = requests.get('https://open.er-api.com/v6/latest/USD').json()
    # print(rate)
   
    rate = factor['rates'][target_currency] / factor['rates'][source_currency]
    value = amount * rate
    value = round(value, 2)

    print(f"{amount} {source_currency} is equal to {value} {target_currency}!")

    response = {'fulfillmentText': f"{amount} {source_currency} is equal to {value} {target_currency}!"} 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')



