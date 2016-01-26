import conekta
conekta.api_key = "key_hZndwwqd2XtFMZHRPCahgQ"
conekta.locale = 'es'
# prueba directa con python en consola...


def charge_create():
    charge = conekta.Charge.create({
        "description": "Stogies",
        "amount": 20000,
        "currency": "MXN",
        "reference_id": "9839-wolf_pack",
        "card": "tok_test_visa_4242",
        "message_to_purchaser": "hola",
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

    print charge.status

charge_create()


