from inference_engine import Inference, Rule
import pymongo

application_client = pymongo.MongoClient("mongodb://localhost:27017/")
application_db = application_client["reflex_pratice"]
application_collection = application_db["ecommerce_rule"]

composite_rules = application_collection.find()
inferences = []
for composite_rule in composite_rules:
    rules = []
    for rule in composite_rule['rules']:
        r = Rule(rule['relation'], rule['percept_ref'], rule['percept_name'], rule['action'])
        rules.append(r)
    inferences.append(Inference(rules, composite_rule['operators'], composite_rule['action']))

# percepts = [
#     {'eccomerce_item': 'RETROSPOT HEART HOT WATER BOTTLE'},
#     {'eccomerce_item': 'SCOTTIE DOG HOT WATER BOTTLE'},
#     {'eccomerce_item': "HEART OF WICKER SMALL"},
# ]

item = input("Qual foi o item comprado? \n")
percepts = [{'eccomerce_item': item}]

for inference in inferences:
    for percept in percepts:
        inference_result = inference.infer(percept)
        if inference_result != 'False':
            print(f" Produto comprado: {percept.get('eccomerce_item')} \n Você pode gostar também do : {inference_result}")
