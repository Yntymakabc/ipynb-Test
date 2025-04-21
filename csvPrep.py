from csv import reader
from collections import defaultdict

with open("synthetic_data_real_products.csv", 'r') as file:
    dat = reader(file)
    headers = next(dat)  # Extract the header row
    name_index = headers.index("customer_name")
    date_index = headers.index("date")
    cost_index = headers.index("cost")
    data = list(dat)  # Extract the remaining rows (actual data)

def total_profit():
    profit = 0
    for i in data:
        profit += int(float(i[cost_index]))  # Convert cost to float first, then to int
    return profit

def who_boutghtMost():
    dic = defaultdict(float)
    for i in data:
        try:
            dic[i[name_index]]+= float(i[cost_index])
        except:
            dic[i[name_index]]+= 0
    return dic
print(who_boutghtMost())


 