"""
aviv drori
main code
calls for get_events and then writes to database
"""

# TODO - better gui instead of console?
# TODO - edit config from program
# TODO - gui with actions - settings, update, clear, info...
# TODO - recognize tests and projs, and change color to yellow
# TODO - recognize weekend stay in base/ go home
"""
UPDATE: run the main program
SETTINGS: edit filter and which calendar id to write to
CLEAR: clear all the luz
INFO: user manual / dev info
"""

import list_events
import database
import config
import googleapiclient

HOW_MANY_EVENTS = 120


def main_program():
    try:
        update_database()
    except googleapiclient.errors.HttpError:
        print("ERROR! The calendar ID is unrecognized.")
        config.my_exit()


def update_database():
    database_file_name, calendar_id, bad_words = config.read_setup_files()
    database.setup_settings(database_file_name, bad_words)

    events = list_events.get_events(calendar_id, HOW_MANY_EVENTS)
    database.write_events_to_db(events)
    input("Press enter to exit.")  # enter then close program.


def tests():
    print(config.read_setup_files())


if __name__ == '__main__':
    main_program()
