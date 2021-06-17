"""
aviv drori
config file for globals
"""
# c_gjgaqdjibjd14j93eannsmps3c@group.calendar.google.com
# import googleapiclient.errors
import json

# Setup files
PATH_TO_COLOR_FILE = 'SETUP/Colors.json'
PATH_TO_SETUP_FILE = 'SETUP/SETUP.txt'
PATH_TO_FILTER = 'SETUP/Filter.txt'
PATH_TO_TOKEN_FILE = 'token.pickle'
# Default number of event to take
HOW_MANY_EVENTS = 120
colors_dict = {}



def my_exit():
    input("Press enter to exit and close program.")
    exit()


def write_color_file(new_dict):
    try:
        for key in new_dict:
            if new_dict[key] == ['']:
                new_dict[key] = []
        with open(PATH_TO_COLOR_FILE, 'w', encoding='utf-8') as f:
            j = json.dumps(new_dict)
            f.write(j)
    except FileNotFoundError:
        print("The colors file was not found.")
        my_exit()


def read_color_file():
    global colors_dict
    try:
        with open(PATH_TO_COLOR_FILE, encoding='utf-8') as f:
            x = f.read()
            colors_dict = json.loads(x)
            return colors_dict
    except FileNotFoundError:
        print("The colors file was not found.")
        my_exit()


def get_color_filter(color_str):
    """
    return the string of words with \n in between
    :param color_str: a string representing Yellow, Green, Red, Cyan, Purple
                      or White
    :return: String of the words, ready to put in the text box
    """
    global colors_dict
    if color_str in colors_dict:
        return '\n'.join(colors_dict[color_str])
    return None


def set_color_filter(words, color):
    """
    :param words: words, with \n in between
    :param color: a string of Yellow/Green/Red/Cyan/Purple/White
    :return: True iff worked
    """
    print("SET COLOR FILTER", words, color)
    global colors_dict
    new_colored_words = words.split('\n')
    print(new_colored_words)
    if color in colors_dict:
        colors_dict[color] = new_colored_words
        print("TRUE and the new dict is", colors_dict)
        write_color_file(colors_dict)
        return True
    return False


def get_bad_words_str():
    """
    return the filter list, ready to put in text box
    """
    return '\n'.join(read_setup_files()[2])


def set_bad_words(str_bad_words):
    """
    :param str_bad_words: string straight from the text
    :return:
    """
    try:
        with open(PATH_TO_FILTER, 'w', encoding='utf-8') as f:
            f.write(str_bad_words)
            f.close()
            return True
    except:
        return False


def set_cal_id(str_id):
    """
    rewrite the calendar id
    :param str_id: string of calendar id
    :return: True iff worked
    """
    try:
        text = 'ERROR'
        with open(PATH_TO_SETUP_FILE, 'r', encoding='utf-8') as f:
            text = f.read()
            print(text)
            f.close()
        with open(PATH_TO_SETUP_FILE, 'w', encoding='utf=8') as f:
            print(text.rsplit(' ', 1)[0] + " " + str_id)
            f.write(text.rsplit(' ', 1)[0] + " " + str_id)
            f.close()
        return True
    except:
        return False


def get_cal_id():
    return read_setup_files()[1]


def read_setup_files():
    """
    read the SETUP folder - SETUP.txt, Filter.txt
    :return: (database file name, calendar id, bad_words)
    """
    try:
        setup_dict = {}
        # Setup file
        with open(PATH_TO_SETUP_FILE, encoding='utf-8') as f:
            for line in f:
                (key, val) = line.split()
                setup_dict[key] = val
        bad_words = []
        # Bad Words
        with open(PATH_TO_FILTER, encoding='utf-8') as f:
            connected_bad_words = f.read()
            bad_words = connected_bad_words.split('\n')
        return setup_dict['database_file:'], setup_dict['calendar_id:'], bad_words

    except FileNotFoundError:
        print("One of the SETUP files is missing, read the manual for info")
        my_exit()
    except ValueError:
        print("The SETUP.txt file is in incorrect format."
              "Read the manual and try again.")
        my_exit()


def get_database_file_name():
    return read_setup_files()[0]


if __name__ == '__main__':
    pass
