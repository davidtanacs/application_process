import querys


def main():
    choice = querys.show_menu()
    conn = querys.connect_to_db()
    if choice == "1":
        querys.mentors_name(conn)
    elif choice == "2":
        querys.miskolc_mentors_nicks(conn)
    elif choice == "3":
        querys.carols_name_and_phone(conn)
    elif choice == "4":
        querys.hat_owners_name_and_phone(conn)
    elif choice == "5":
        querys.markus_schaffarzyks_datas(conn)
    elif choice == "6":
        querys.update_jemima_phone(conn)
    elif choice == "7":
        querys.del_arsenio_and_friend(conn)

if __name__ == '__main__':
    main()