import json



firts_pattern_results_array = [] # просрочен аккаунт
second_pattern_results_array = [] # просрочен паспорт
third_pattern_results_array = [] # родился после транзакции
fourth_pattern_results_array = [] # получил паспорт раньше 14 лет
fifth_pattern_results_array = [] # младше 14 лет

with open('transactions.json') as f:
    transactions = json.load(f)["transactions"]

for i in transactions.keys():
    date = transactions[i]['date']
    account_valid_to = transactions[i]['account_valid_to']
    date_of_birth = transactions[i]['date_of_birth']
    passport_valid_to = transactions[i]['passport_valid_to']
    if date > account_valid_to:
        firts_pattern_results_array.append(i)
    if date > passport_valid_to:
        second_pattern_results_array.append(i)
    if date < date_of_birth:
        third_pattern_results_array.append(i)

#print(firts_pattern_results_array)
#print(len(firts_pattern_results_array))
#print(second_pattern_results_array)
#print(len(second_pattern_results_array))
#print(third_pattern_results_array)
#print(len(firts_pattern_results_array))
two_res = sorted(second_pattern_results_array)
one_res = sorted(firts_pattern_results_array)
with open ('first_result.txt') as f1:
    for s in one_res:
        f1.write(s)
        f1.write(', ')
    f1.write('\n')
    for s in two_res:
        f1.write(s)
        f1.write(', ')