import psycopg2


def show_menu():
    choice = input("""
            Press 1 to Mentors' name\n
            Press 2 to Mentors' nickname at Miskolc\n
            Press 3 to Carol's full name and phone number\n
            Press 4 to hat-owner's full name and phone number\n
            Press 5 to Markus Schaffarzyk's datas\n
            Press 6 to update Jemima Foreman's phone number and see it\n
            Press 7 to delete Arsenio and his friend from the database""")
    return choice


def connect_to_db():
    connect_str = "dbname='tanacs' user='tanacs' host='localhost' password='buggyanás'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    return conn


def make_query_for_print(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return print("Here you are: ", rows)


def make_query_for_db_change(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)


def show_mentors_name(conn):
    make_query_for_print("""SELECT first_name, last_name FROM mentors;""", conn)


def show_mentors_nick_miskolc(conn):
    make_query_for_print("""SELECT nick_name FROM mentors WHERE city='Miskolc';""", conn)


def show_carols_data(conn):
    make_query_for_print("""SELECT concat(first_name, ' ', last_name),
        phone_number FROM applicants WHERE first_name='Carol';""", conn)


def hat_owners_data(conn):
    make_query_for_print("""SELECT concat(first_name, ' ', last_name),
    phone_number FROM  applicants WHERE email like '%@adipiscingenimmi.edu';""", conn)


def insert_markus_datas(conn):
    make_query_for_print("""SELECT * FROM applicants WHERE application_code=54823;""", conn)


def update_jemimas_data(conn):
    make_query_for_db_change("""UPDATE applicants SET phone_number='003670/223-7459'
    WHERE first_name='Jemima' and last_name='Foreman';""", conn)
    make_query_for_print("""SELECT first_name, last_name, phone_number from applicants
    WHERE first_name='Jemima' and last_name='Foreman';""", conn)


def del_arsenio_and_friend(conn):
    make_query_for_db_change("""DELETE FROM applicants WHERE email LIKE '%mauriseu.net';""", conn)