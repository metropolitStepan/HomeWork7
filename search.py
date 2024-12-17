import csv

class Client:
    def __init__(self, name, device_type, browser, sex, age, bill, region):
        self.name = name
        self.device_type = device_type
        self.browser = browser
        self.sex = sex
        self.age = float(age)
        self.bill = float(bill)
        self.region = region

    def __str__(self):
        gender = "мужского" if self.sex == "male" else "женского"
        return f"Пользователь {self.name} {gender} пола, {self.age:.0f} лет совершила покупку на {self.bill:.0f} у.е. с {self.device_type} браузера {self.browser}. Регион, из которого совершалась покупка: {self.region}."


def load_clients(filepath):
    clients = []
    try:
        with open(filepath, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', fieldnames=['name', 'device_type', 'browser', 'sex', 'age', 'bill', 'region'])
            next(reader)

            for row in reader:
                client = Client(row['name'], row['device_type'], row['browser'], row['sex'], float(row['age']), float(row['bill']), row['region'])
                clients.append(client)
    except Exception as e:
        print(f"Ошибка в прочтении csv файла: {e}")
        return []
    return clients

def client_descriptions(clients):
    return [str(client) for client in clients]

def savetxt(descriptions, filepath):
    try:
        with open(filepath, 'w', encoding='utf-8') as txtfile:
            txtfile.write('\n'.join(descriptions))
    except Exception as e:
        print(f"Ошибка в записи файла: {e}")

def main():
    csv_filepath = "web_clients_correct.csv"
    txt_filepath = "client_descriptions.txt"

    clients = load_clients(csv_filepath)
    if clients:
        descriptions = client_descriptions(clients)
        savetxt(descriptions, txt_filepath)
        print(f"Описание сохранено в '{txt_filepath}'.")

if __name__ == "__main__":
    main()