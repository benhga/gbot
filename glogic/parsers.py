import json
from .models import Items


# parsers for seeding the database, called from manager
def questions_parse(json_string, db_table):
    questions = []
    questions_dicts = json.loads(json_string).get("products")
    print(question_dicts)
    for question_dict in questions_dicts:
        print("************************")
        print(question_dict)
        name = question_dict["name"]
        number = question_dict["number"]
        questions.append(db_table(name=name, number=number))
    return questions


def products_parse(json_string):
    products = []
    products_dicts = json.loads(json_string).get("products")
    print(products_dicts)

    for product_dict in products_dicts:
        name = product_dict["name"]
        number = product_dict["number"]
        products.append(Items(name, number))

    return products
