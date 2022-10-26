import json


#with open('transactions_final.json') as f:
with open('test.json') as f:
    transactions = json.load(f)

# "459270924": {
#             "date": "2020-05-01T00:00:29",
#             "card": "59649132026167121328",
#             "account": "40817810000001139973",
#             "account_valid_to": "2036-01-16T00:00:00",
#             "client": "3-95179",
#             "last_name": "\u041c\u0438\u0441\u0438\u043a",
#             "first_name": "\u0421\u0435\u0440\u0433\u0435\u0439",
#             "patronymic": "\u041d\u0438\u043a\u043e\u043b\u0430\u0435\u0432\u0438\u0447",
#             "date_of_birth": "1938-06-25T00:00:00",
#             "passport": 7076445954,
#             "passport_valid_to": "2022-11-09T00:00:00",
#             "phone": "+79497481039",
#             "oper_type": "\u041f\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435",
#             "amount": 31576.6,
#             "oper_result": "\u041e\u0442\u043a\u0430\u0437",
#             "terminal": "POS43792",
#             "terminal_type": "POS",
#             "city": "\u0421\u043b\u0430\u0432\u044f\u043d\u0441\u043a-\u043d\u0430-\u041a\u0443\u0431\u0430\u043d\u0438",
#             "address": "\u0421\u043b\u0430\u0432\u044f\u043d\u0441\u043a-\u043d\u0430-\u041a\u0443\u0431\u0430\u043d\u0438, \u0443\u043b. \u041a\u043b\u0435\u0446\u043a\u0430\u044f, \u0434. 86"

list_trans_id = []

dict_transactions = {}

for key, transaction in transactions['transactions'].items():
    list_trans_id.append(key)
    for k, v in transaction.items():
        if not dict_transactions.get(k):
            dict_transactions[k] = []
            dict_transactions[k].append(v)
        else:
            dict_transactions[k].append(v)

dict_transactions['transaction_id'] = list_trans_id

fios = {}
for i in transactions["transactions"].keys():
    fio = transactions["transactions"][i]['last_name'] + ' ' + transactions["transactions"][i]['first_name'] + ' ' + transactions["transactions"][i]['patronymic']
    if not(fios.get(fio)):
        fios[fio] = [transactions["transactions"][i]]
    else:
        fios[fio].append(transactions["transactions"][i])

cnt = 0

print(fios.keys())

