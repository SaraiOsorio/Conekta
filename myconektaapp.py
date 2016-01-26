# prueba con html, javascript y python
from flask import Flask
from flask import render_template
from flask import request
import conekta

app = Flask(__name__)
app.debug = True


@app.route('/')
@app.route('/index')
@app.route('/charge')
def index():
    return render_template('charge.html')


@app.route('/charges', methods=["POST"])
def charge_create():
    conekta.api_key = "key_hZndwwqd2XtFMZHRPCahgQ"

    charge = conekta.Charge.create({
        "description": request.form['description'],
        "amount": request.form['amount'],
        "currency": "MXN",
        "reference_id": "9839-wolf_pack",
        "card": request.form['token_id'],
        'message_to_purchaser': "hola",
        "message": "hola",
        "details": {
            "name": "Arnulfo Quimare",
            "phone": "403-342-0642",
            "email": "logan@x-men.org",
            "customer": {
                "logged_in": True,
                "successful_purchases": 14,
                "created_at": 1379784950,
                "updated_at": 1379784950,
                "offline_payments": 4,
                "score": 9
            },
            "line_items": [{
                "name": "Box of Cohiba S1s",
                "description": "Imported From Mex.",
                "unit_price": 20000,
                "quantity": 1,
                "sku": "cohb_s1",
                "category": "food"
            }],
            "billing_address": {
                "street1": "77 Mystery Lane",
                "street2": "Suite 124",
                "street3": None,
                "city": "Darlington",
                "state": "NJ",
                "zip": "10192",
                "country": "Mexico",
                "tax_id": "xmn671212drx",
                "company_name": "X-Men Inc.",
                "phone": "77-777-7777",
                "email": "purshasing@x-men.org"
            }
        }
    })

    return render_template('charge_status.html', charge=charge)
