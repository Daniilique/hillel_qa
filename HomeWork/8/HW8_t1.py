import csv
currency_exchange_rate = 0.025 #todays rate thu,24
with open('test_file.csv', 'r') as file:
    data = [line for line in csv.reader(file)]
for row in data[1:]:
    for i in range(1, len(row)):
        row[i] = round(float(row[i]) * currency_exchange_rate, 2)
with open('salaries_uah.csv', 'w', newline='') as file:
    csv.writer(file).writerows(data)

