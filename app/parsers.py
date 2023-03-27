def parse_cnab(file_content):
    transactions = []
    for line in file_content.splitlines():
        transaction_data = {
            "transaction_type": int(line[0:1]),
            "date": line[1:9],
            "amount": float(line[9:19])/100,
            "cpf": line[19:30],
            "card": line[30:42],
            "time": line[42:48],
            "owner": line[48:62].strip(),
            "name": line[62:81].strip()
        }
        transactions.append(transaction_data)
    return transactions
