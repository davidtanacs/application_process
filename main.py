import querys


def main():
    choice = querys.show_menu()
    conn = querys.connect_to_db()
    if choice == "1":
        querys.make_query("""SELECT first_name, last_name FROM mentors;""", conn)
    elif choice == "2":
        querys.make_query("""SELECT nick_name FROM mentors WHERE city='Miskolc';""", conn)
    elif choice == "3":
        querys.make_query("""SELECT concat(first_name, ' ', last_name), phone_number FROM applicants WHERE first_name='Carol';""", conn)
    elif choice == "4":
        querys.make_query(conn)
    elif choice == "5":
        querys.make_query(conn)
    elif choice == "6":
        querys.make_query(conn)
    elif choice == "7":
        querys.make_query(conn)

if __name__ == '__main__':
    main()