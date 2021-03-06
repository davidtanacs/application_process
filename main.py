import querys
from flask import Flask, request, render_template, redirect, url_for
import psycopg2

app = Flask(__name__)


@app.route('/')
def menu():
    try:
        if querys.read_user_datas() is None:
            connect = 'not_ok_yet'
        else:
            connect = "ok"
            return render_template('main.html', connect=connect)
    except OSError:
        dbname = request.args.get('dbname')
        user = request.args.get('user')
        password = request.args.get('password')
    if dbname and user and password:
        try:
            querys.connect_to_db(dbname, user, password)
            querys.store_user_datas(dbname, user, password)
            connect = 'ok'
        except psycopg2.Error:
            connect = 'not_ok'
    else:
        connect = 'not_ok_yet'
    return render_template('main.html', connect=connect)


@app.route('/connect_to_db', methods=['GET', 'POST'])
def get_datas():
    return render_template('connect_to_database.html')


@app.route('/mentors')
def show_mentors():
    datas = querys.read_user_datas()
    conn = querys.connect_to_db(datas[0], datas[1], datas[2])
    rows = querys.show_mentors_name(conn)
    conn.close()
    return render_template('mentors.html', rows=rows)


@app.route('/all_school')
def show_all_school():
    datas = querys.read_user_datas()
    conn = querys.connect_to_db(datas[0], datas[1], datas[2])
    rows = querys.show_all_schools_name(conn)
    conn.close()
    return render_template('all_school.html', rows=rows)


@app.route('/mentors_by_country')
def show_mentors_by_country():
    datas = querys.read_user_datas()
    conn = querys.connect_to_db(datas[0], datas[1], datas[2])
    rows = querys.count_mentors_by_country(conn)
    conn.close()
    return render_template('mentors_by_country.html', rows=rows)


@app.route('/contacts')
def show_school_and_contact():
    datas = querys.read_user_datas()
    conn = querys.connect_to_db(datas[0], datas[1], datas[2])
    rows = querys.show_school_and_contact_person(conn)
    conn.close()
    return render_template('contacts.html', rows=rows)


@app.route('/applicants')
def show_applicants():
    datas = querys.read_user_datas()
    conn = querys.connect_to_db(datas[0], datas[1], datas[2])
    rows = querys.show_applicants_datas(conn)
    conn.close()
    return render_template('applicants.html', rows=rows)


@app.route('/applicants_and_mentors')
def show_applicants_and_mentors():
    datas = querys.read_user_datas()
    conn = querys.connect_to_db(datas[0], datas[1], datas[2])
    rows = querys.show_applicants_and_mentors_datas(conn)
    conn.close()
    return render_template('applicants_and_mentors.html', rows=rows)


@app.route('/quit')
def delete_user_datas_and_quit():
    connect = "not_ok_yet"
    querys.delete_user_datas()
    return render_template('main.html', connect=connect)


if __name__ == '__main__':
    app.run(debug=True)