import psycopg2
import csv


def show_menu():
    choice = input("""
            Press 1 to see Mentors' name\n
            Press 2 to see Mentors' nickname at Miskolc\n
            Press 3 to see Carol's full name and phone number\n
            Press 4 to see hat-owner's full name and phone number\n
            Press 5 to see Markus Schaffarzyk's datas\n
            Press 6 to update Jemima Foreman's phone number and see it\n
            Press 7 to delete Arsenio and his friend from the database
            Or 0 to quit""")
    return int(choice)


def make_query_readable(rows):
    readable_data = ""
    for item in rows:
        for word in item:
            readable_data += str(word)
            if word != item[-1]:
                readable_data += ", "
        if item != rows[-1]:
            readable_data += " ; "
    return readable_data


def connect_to_db(dbname, user, password):
    connect_str = "dbname=%s user=%s host='localhost' password=%s" % (dbname, user, password)
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    return conn


def make_query(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


def store_user_datas(dbname, user, password):
    datas = [dbname, user, password]
    with open('user_datas.csv', mode='w') as file:
        for word in datas:
            file.write(word)
            file.write('\n')


def read_user_datas():
    datas = []
    with open('user_datas.csv', mode='r') as file:
        for word in file:
            datas.append(word)
    return datas


def make_query_for_db_change(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)


def show_mentors_name(conn):
    rows = make_query("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                        FROM mentors 
                        LEFT JOIN schools ON mentors.city = schools.city;""", conn)
    return rows


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