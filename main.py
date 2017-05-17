import querys
import sys


def main():
    choice = 8
    while choice > 0 and choice <= 8:
        choice = querys.show_menu()
        conn = querys.connect_to_db()
        if choice == 1:
            querys.show_mentors_name(conn)
        elif choice == 2:
            querys.show_mentors_nick_miskolc(conn)
        elif choice == 3:
            querys.show_carols_data(conn)
        elif choice == 4:
            querys.hat_owners_data(conn)
        elif choice == 5:
            querys.insert_markus_datas(conn)
        elif choice == 6:
            querys.update_jemimas_data(conn)
        elif choice == 7:
            querys.del_arsenio_and_friend(conn)
        elif choice == 0:
            sys.exit
    choice = int(8)

if __name__ == '__main__':
    main()