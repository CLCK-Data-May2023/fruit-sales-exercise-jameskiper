import pandas as pd

fruit_sale =pd.DataFrame({'Apples': [35, 41],
                          'Bananas': [21, 34]},
index=['2017 Sales', '2018 Sales'])
fruit_sale
fruit_sale.to_csv('fruit.csv')