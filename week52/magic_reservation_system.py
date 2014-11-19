import sqlite3
import config
import cinema


def main():
    db = sqlite3.connect(config.DATABASE)
    db.row_factory = sqlite3.Row
    Cinema = cinema.Cinema(db)
    command = input("> ")
    command_properties = command.split(' ')

    if command_properties[0] == "show_movies":
        Cinema.show_movies()
    elif command_properties[0] == "show_movie_projections":
        id = command_properties[1]
        if len(command_properties) > 2:
            date = command_properties[2]
            Cinema.show_projections(id, date)
        else:
            Cinema.show_projections(id)
    elif command_properties[0] == "make_reservation":
        Cinema.make_reservation()
    else:
        print('Invalid Command')
    main()

if __name__ == '__main__':
    main()
