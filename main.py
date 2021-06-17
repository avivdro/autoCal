"""
aviv drori
main code
calls for get_events and then writes to database
"""

import list_events
import database
from config import *
import googleapiclient
import google.auth.exceptions
import os


def main_program():
    try:
        update_database()
    except googleapiclient.errors.HttpError:
        print("ERROR! The calendar ID is unrecognized.")
        my_exit()
    except google.auth.exceptions.RefreshError:
        print("Token has expired. Restarting.")
        # automatically delete the token file and restart program
        os.remove(PATH_TO_TOKEN_FILE)
        main_program()


def update_database():
    print("UPDATE DATABASE", read_setup_files())
    database_file_name, calendar_id, bad_words = read_setup_files()
    database.setup_settings(database_file_name, bad_words)

    events = list_events.get_events(calendar_id, HOW_MANY_EVENTS)
    database.write_events_to_db(events)
    # input("Press enter to exit.")  # enter then close program.


def tests():
    print(read_setup_files())


if __name__ == '__main__':
    # tests()
    main_program()
