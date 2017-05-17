import querys


def main():
    choice = querys.show_menu()
    conn = querys.connect_to_db()
    if choice == "1":
        querys.make_query_for_print("""SELECT first_name, last_name FROM mentors;""", conn)
    elif choice == "2":
        querys.make_query_for_print("""SELECT nick_name FROM mentors WHERE city='Miskolc';""", conn)
    elif choice == "3":
        querys.make_query_for_print("""SELECT concat(first_name, ' ', last_name),
         phone_number FROM applicants WHERE first_name='Carol';""", conn)
    elif choice == "4":
        querys.make_query_for_print("""SELECT concat(first_name, ' ', last_name),
         phone_number FROM  applicants WHERE email like '%@adipiscingenimmi.edu';""", conn)
    elif choice == "5":
        querys.make_query_for_print("""SELECT * FROM applicants WHERE application_code=54823;""", conn)
    elif choice == "6":
        querys.make_query_for_db_change("""UPDATE ;""", conn)
    elif choice == "7":
        querys.make_query(conn)

if __name__ == '__main__':
    main()