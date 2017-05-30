import psycopg2
import csv


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


def show_all_schools_name(conn):
    rows = make_query("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                            FROM mentors
                            RIGHT JOIN schools on mentors.city = schools.city;""", conn)
    return rows


def count_mentors_by_country(conn):
    rows = make_query("""SELECT country, COUNT(mentors) FROM mentors
                        FULL JOIN schools ON mentors.city = schools.city
                        GROUP BY country ORDER BY country;""", conn)
    return rows


def show_school_and_contact_person(conn):
    rows = make_query("""SELECT name, CONCAT(first_name, ' ', last_name) FROM mentors
                        INNER JOIN schools ON mentors.id = schools.contact_person
                        ORDER BY name;""", conn)
    return rows


def insert_markus_datas(conn):
    make_query_for_print("""SELECT * FROM applicants WHERE application_code=54823;""", conn)


def update_jemimas_data(conn):
    make_query_for_db_change("""UPDATE applicants SET phone_number='003670/223-7459'
    WHERE first_name='Jemima' and last_name='Foreman';""", conn)
    make_query_for_print("""SELECT first_name, last_name, phone_number from applicants
    WHERE first_name='Jemima' and last_name='Foreman';""", conn)


def del_arsenio_and_friend(conn):
    make_query_for_db_change("""DELETE FROM applicants WHERE email LIKE '%mauriseu.net';""", conn)


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
