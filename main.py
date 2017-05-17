import querys


def main():
    choice = querys.show_menu()
    conn = querys.connect_to_db()
    if choice == "1":
        querys.show_mentors_name(conn)
    elif choice == "2":
        querys.show_mentors_nick_miskolc(conn)
    elif choice == "3":
        querys.show_carols_data(conn)
    elif choice == "4":
        querys.hat_owners_data(conn)
    elif choice == "5":
        querys.insert_markus_datas(conn)
    elif choice == "6":
        querys.update_jemimas_data(conn)
    elif choice == "7":
        querys.del_arsenio_and_friend(conn)

if __name__ == '__main__':
    main()