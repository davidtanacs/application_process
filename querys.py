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
    # setup connection string
    connect_str = "dbname='tanacs' user='tanacs' host='localhost' password='buggyanás'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    return conn


def mentors_name(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    rows = cursor.fetchall()
    return(print(rows))


def miskolc_mentors_nicks():
    pass


def carols_name_and_phone():
    pass


def hat_owners_name_and_phone():
    pass


def markus_schaffarzyks_datas():
    pass


def update_jemima_phone():
    pass


def del_arsenio_and_friend():
    pass