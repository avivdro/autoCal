"""
aviv drori
main code
calls for get_events and then writes to database
"""

# TODO - setup file for: database file name
# TODO - setup file for: list_events.CALENDAR_ID
# TODO - setup file for: database.BAD_STRINGS
# TODO - icon :)
# TODO - better gui instead of console.
# TODO - user manual for KATA

import list_events
import database

HOW_MANY_EVENTS = 120
PATH_TO_SETUP_FILE = 'setup/SETUP.txt'
PATH_TO_FILTER = 'setup/Filter.txt'


def read_setup_files():
    """
    read the SETUP folder - SETUP.txt, Filter.txt
    :return: (database file name, calendar id)
    """
    try:
        d = {}
        with open(PATH_TO_SETUP_FILE, encoding='utf-8') as f:
            for line in f:
                (key, val) = line.split()
                d[key] = val
        bad_words = []
        with open(PATH_TO_FILTER, encoding='utf-8') as f:
            for line in f:
                bad_words.append(line[:-1])
        return d['database_file:'], d['calendar_id:'], bad_words
    except FileNotFoundError:
        print("One of the SETUP files is missing, read the manual for info")
        exit()


def main():
    database_file_name, calendar_id, bad_words = read_setup_files()
    database.set_bad_words(bad_words)
    events = list_events.get_events(calendar_id, HOW_MANY_EVENTS)
    database.write_events_to_db(database_file_name, events)
    input("Press enter to exit.")  # enter then close program.


def tests():
    print(read_setup_files())


if __name__ == '__main__':
    main()
