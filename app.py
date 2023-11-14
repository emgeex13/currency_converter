from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    
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
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



# 1 USD = 83.50 INR
# 1 INR = 0.012 USD
# 
