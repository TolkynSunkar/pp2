import csv
from connect import get_connection

conn = get_connection()
cur = conn.cursor()



def insert_from_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row['name'], row['phone'])
            )
    conn.commit()
    print("CSV data inserted.")



def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Contact added.")



def query_contacts():
    print("1 - Show all")
    print("2 - Search by name")
    print("3 - Search by phone prefix")

    choice = input("Choose: ")

    if choice == '1':
        cur.execute("SELECT * FROM phonebook")
    elif choice == '2':
        name = input("Enter name: ")
        cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    elif choice == '3':
        prefix = input("Enter prefix: ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (prefix + '%',))
    else:
        return

    rows = cur.fetchall()
    for row in rows:
        print(row)



def update_contact():
    name = input("Enter name to update: ")
    new_name = input("New name (or press enter): ")
    new_phone = input("New phone (or press enter): ")

    if new_name:
        cur.execute("UPDATE phonebook SET name=%s WHERE name=%s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, name))

    conn.commit()
    print("Updated.")


# 5️⃣ 删除
def delete_contact():
    print("1 - Delete by name")
    print("2 - Delete by phone")

    choice = input("Choose: ")

    if choice == '1':
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))
    elif choice == '2':
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))

    conn.commit()
    print("Deleted.")


# 🎯 主菜单
def menu():
    while True:
        print("\nPhoneBook Menu:")
        print("1 - Insert from CSV")
        print("2 - Insert from console")
        print("3 - Query")
        print("4 - Update")
        print("5 - Delete")
        print("0 - Exit")

        choice = input("Choose: ")

        if choice == '1':
            insert_from_csv('contacts.csv')
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            query_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '0':
            break
        else:
            print("Invalid choice")


menu()

cur.close()
conn.close()