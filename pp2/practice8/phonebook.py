from connect import get_connection

conn = get_connection()
cur = conn.cursor()


def search():
    pattern = input("Enter search pattern: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def paginate():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def upsert():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    print("Inserted/Updated.")


def bulk_insert():
    cur.execute("CALL insert_many()")
    conn.commit()
    print("Bulk insert done.")


def delete():
    value = input("Enter name or phone to delete: ")
    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()
    print("Deleted.")


def menu():
    while True:
        print("\n--- Practice 8 Menu ---")
        print("1 - Search (function)")
        print("2 - Pagination (function)")
        print("3 - Upsert (procedure)")
        print("4 - Bulk Insert (procedure)")
        print("5 - Delete (procedure)")
        print("0 - Exit")

        choice = input("Choose: ")

        if choice == '1':
            search()
        elif choice == '2':
            paginate()
        elif choice == '3':
            upsert()
        elif choice == '4':
            bulk_insert()
        elif choice == '5':
            delete()
        elif choice == '0':
            break
        else:
            print("Invalid choice")


menu()

cur.close()
conn.close()