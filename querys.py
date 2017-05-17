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


def make_query(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return print(rows)


def hat_owners_name_and_phone(conn):
    pass


def markus_schaffarzyks_datas(conn):
    pass


def update_jemima_phone(conn):
    pass


def del_arsenio_and_friend(conn):
    pass