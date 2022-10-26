import json
with open('transactions_final.json') as f:
    transactions = json.load(f)["transactions"]

res = [] # many FIO`s in one accaunt 
# тест русского языка


accounts = []


for i in transactions.keys():
    account = transactions[i]['account']
    accounts.append(account)
    fio = transactions[i]['last_name']+transactions[i]['first_name']+transactions[i]['patronymic']


fake_accs = []
for acc in accounts:
    temp = []
    for i in transactions.keys():
        if acc == transactions[i]['account']:
            temp.append(transactions[i]['last_name']+transactions[i]['first_name']+transactions[i]['patronymic'])
        if len(set(temp)) > 1:
            fake_accs.append(acc)
            break

for f_acc in fake_accs:
    for i in transactions.keys():

        if f_acc == transactions[i]['account']:
            res.append(i)
