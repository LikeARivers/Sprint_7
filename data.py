class TestDataCreateCourier:

    CREATE_COURIER_BODY = {
        "login": "ninjc",
        "password": "1234",
        "firstName": "saske"
    }

    CREATE_COURIER_BODY_WITHOUT_LOGIN = {
        "password": "1234",
        "firstName": "saske"
    }

    CREATE_COURIER_BODY_WITHOUT_PASSWORD = {
        "login": "ninjc",
        "firstName": "saske"
    }

    CREATE_IDENTICAL_COURIER_BODY = {
        "login": "sandre",
        "password": "1234",
        "firstName": "alex"
    }

class TestDataAuthorization:
    AUTHORIZATION_NONEXISTENT_COURIER_BODY = {
        "login": "likeariver",
        "password": "1234"
    }

    AUTH_COURIER_BODY_WITHOUT_LOGIN = {
        "password": "1234"
    }


class TestDataCreateOrder:
    CREATE_ORDER_BODY = {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "address": "Baker street",
        "metroStation": 4,
        "phone": "+7 800 355 02 21",
        "rentTime": 5,
        "deliveryDate": "2024-06-06",
        "comment": "Elementary Watson",
        "color": [
            "BLACK"
        ]
    }