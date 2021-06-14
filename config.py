"""
aviv drori
config file for globals
"""

# TODO database file name - read it here??
import googleapiclient.errors

PATH_TO_SETUP_FILE = 'SETUP/SETUP.txt'
PATH_TO_FILTER = 'SETUP/Filter.txt'


def my_exit():
    input("Press enter to exit and close program.")
    exit()



def read_setup_files():
    """
    read the SETUP folder - SETUP.txt, Filter.txt
    :return: (database file name, calendar id, bad_words)
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
        my_exit()
    except ValueError:
        print("The SETUP.txt file is in incorrect format."
              "Read the manual and try again.")
        my_exit()


def get_database_file_name():
    return read_setup_files()[0]

# calendar id - not sure needed

# bad_words - not sure needed
