import psycopg2
import csv
import os


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


def delete_user_datas():
    os.remove('user_datas.csv')


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


def show_applicants_datas(conn):
    rows = make_query("""SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                    FROM applicants JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
                    WHERE applicants_mentors.creation_date > '2016/01/01'
                    ORDER BY applicants_mentors.creation_date DESC;""", conn)
    return rows


def show_applicants_and_mentors_datas(conn):
    rows = make_query("""SELECT applicants.first_name, applicants.application_code, CONCAT(mentors.first_name, ' ', mentors.last_name)
                    FROM applicants FULL JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
                    LEFT JOIN mentors ON applicants_mentors.mentor_id = mentors.id;""", conn)
    print(rows)
    return rows
