import json
if __name__ == "__main__":
    book = AddressBook()
    book.deserialize('addressbook.json')

    while True:
        command = input("Введіть команду: ").strip().lower()
        if command == 'add-birthday':
            name = input("Ім'я контакту: ")
            birthday = input("Дата народження (у форматі DD.MM.YYYY): ")
            contact = book.find(name)
            if contact:
                result = contact.add_birthday(birthday)
                print(result)
            else:
                print(f"Контакт {name} не знайдений.")
        elif command == 'show-birthday':
            name = input("Ім'я контакту: ")
            contact = book.find(name)
            if contact and contact.birthday:
                print(f"Дата народження для {name}: {contact.birthday}")
            else:
                print(f"Дата народження для {name} не вказана.")
        elif command == 'birthdays':
            birthdays = book.get_birthdays_per_week()
            if birthdays:
                print("Користувачі, яких потрібно привітати на наступному тижні:")
                for contact in birthdays:
                    print(f"{contact.name}: {contact.birthday}")
            else:
                print("Немає користувачів з днями народження на наступному тижні.")
        elif command == 'exit':
            book.serialize('addressbook.json')
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")
