"""
aviv drori
may 2021
This file uses opnenpyxl to read and write to the excel
"""

import openpyxl
from openpyxl import load_workbook
from list_events import dtm_str_to_obj

# EXCEL FILE CONSTANTS:
DATABASE_FILE = 'database.xlsx'  # this file needs to be in same dir
SHEET1_NAME = 'Sheet1'           # this sheet needs to be in the file
WEEK_23_NAME = 'week23'
WEEK_24_NAME = 'week24'
WEEK_25_NAME = 'week25'
WEEK_26_NAME = 'week26'
WEEK_1_NAME = 'week1'
WEEK_2_NAME = 'week2'
# add more as i go...


# SHEET1:
COL_A = 'A'

# COL_DAYS
COL_D1_START = 'A'  # sunday
COL_D1_END = 'B'
COL_D1_NAME = 'C'
COL_D1_LEN = 'D'



# ROWS
ROW_EVENTS_START = 5
ROW_EVENTS_END = 20
# EXCEL SHEET STARTUP
DB = load_workbook(DATABASE_FILE)
SHEET1 = DB[SHEET1_NAME]
WEEK_23_SHEET = DB[WEEK_23_NAME]
# TODO init the other sheets


def write_events_to_db(events):
    """
    writes the event to the excel database
    :param events: list of event string as received from google calendar
    :return:
    """
    i = ROW_EVENTS_START
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        print("Writing event: ", event['summary'])
        dtm_start = dtm_str_to_obj(start)
        dtm_end = dtm_str_to_obj(end)
        elapsed_time = dtm_end - dtm_start
        # write from:
        SHEET1[COL_D1_START + str(i)] = str(dtm_start)
        # write to:
        SHEET1[COL_D1_END + str(i)] = str(dtm_end)
        # write name:
        SHEET1[COL_D1_NAME + str(i)] = str(event['summary'])
        # write length:
        SHEET1[COL_D1_LEN + str(i)] = elapsed_time
        i += 1
    save()


def save():
    DB.save(DATABASE_FILE)
    return


def tests():
    # tests:
    print(SHEET1[COL_A + str(1)].value)   # output should be test
    print(SHEET1['A2'].value)       # output should be 2
    SHEET1[COL_A + str(5)] = "write test"
    save()


if __name__ == '__main__':
    tests()
