import querys
from flask import Flask, request, render_template, redirect, url_for
import psycopg2

app = Flask(__name__)


@app.route('/')
def menu():
    connect = 'not_ok_yet'
    dbname = request.args.get('dbname')
    user = request.args.get('user')
    password = request.args.get('password')
    if dbname:
        try:
            querys.connect_to_db(dbname, user, password)
            querys.store_user_datas(dbname, user, password)
            connect = 'ok'
        except psycopg2.Error:
            connect = 'not_ok'
    return render_template('main.html', connect=connect)


@app.route('/connect_to_db', methods=['GET', 'POST'])
def get_datas():
    return render_template('connect_to_database.html')


@app.route('/mentors')
def show_mentors():
    datas = querys.read_user_datas()
    conn = querys.connect_to_db(datas[0], datas[1], datas[2])
    rows = querys.show_mentors_name(conn)
    return render_template('mentors.html', rows=rows)


@app.route('/all_school')
def show_all_school():
    datas = querys.read_user_datas()
    conn = querys.connect_to_db(datas[0], datas[1], datas[2])
    rows = querys.show_all_schools_name(conn)
    return render_template('all_school.html', rows=rows)


@app.route('/mentors_by_country')
def show_mentors_by_country():
    datas = querys.read_user_datas()
    conn = querys.connect_to_db(datas[0], datas[1], datas[2])
    rows = querys.count_mentors_by_country(conn)
    return render_template('mentors_by_country.html', rows=rows)


@app.route('/contacts')
def show_school_and_contact():
    datas = querys.read_user_datas()
    conn = querys.connect_to_db(datas[0], datas[1], datas[2])
    rows = querys.show_school_and_contact_person(conn)
    return render_template('contacts.html', rows=rows)





#def main():
#    choice = 8
#    while choice > 0 and choice <= 8:
#        choice = querys.show_menu()
#        conn = querys.connect_to_db()
#        if choice == 1:
#            querys.show_mentors_name(conn)
#        elif choice == 2:
#            querys.show_mentors_nick_miskolc(conn)
#        elif choice == 3:
#            querys.show_carols_data(conn)
#        elif choice == 4:
#            querys.hat_owners_data(conn)
#        elif choice == 5:
#            querys.insert_markus_datas(conn)
#        elif choice == 6:
#            querys.update_jemimas_data(conn)
#        elif choice == 7:
#            querys.del_arsenio_and_friend(conn)
#        elif choice == 0:
#            sys.exit
#    choice = int(8)

if __name__ == '__main__':
    app.run(debug=True)