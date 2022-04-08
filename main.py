import pandas as pd
from apriori_2_algorithm import *

basket_data = pd.read_csv('data/basket.csv')
items_by_transaction = basket_data.groupby('Transaction')['Item'].apply(set)
itemset = basket_data['Item'].unique()
print('Items sold by market: ', len(itemset))
print('Itemset: ', itemset)

rules = apriori_2(itemset, items_by_transaction, 0.05, 0.1)

print(rules[1])