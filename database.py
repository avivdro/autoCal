"""
aviv drori
may 2021
This file uses opnenpyxl to read and write to the excel
"""

import openpyxl
from openpyxl import load_workbook
from list_events import dtm_str_to_obj
from datetime import datetime, time, date

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
COL_FROM_DICT = {1: 'A', 2: 'E', 3: 'I', 4: 'M', 5: 'Q', 6: 'U', 7: 'Y'}
COL_TO_DICT = {1: 'B', 2: 'F', 3: 'J', 4: 'N', 5: 'R', 6: 'V', 7: 'Z'}
COL_NAME_DICT = {1: 'C', 2: 'G', 3: 'K', 4: 'O', 5: 'S', 6: 'W', 7: 'AA'}
COL_LEN_DICT = {1: 'D', 2: 'H', 3: 'L', 4: 'P', 5: 'T', 6: 'X', 7: 'AB'}
# ROWS
ROW_EVENTS_START = 3
ROW_EVENTS_END = 20
# EXCEL SHEET STARTUP
DB = load_workbook(DATABASE_FILE)
SHEET1 = DB[SHEET1_NAME]
SHEET_DICT = {23: DB[WEEK_23_NAME], 24: DB[WEEK_24_NAME], 25: DB[WEEK_25_NAME]}

# TODO init the other sheets


def choose_sheet(dtm_event):
    """
    returns the sheet corresponding to the week of the event
    :param dtm_event: datetime obj of the event
    :return: execl sheet - if event shouldn't be written, return 0
    """
    if dtm_event == datetime(2020, 1, 1, 1, 1, 1):   # this is the arbitrary datetime for whole day events
        return 0
    week_num = dtm_event.isocalendar()[1] + 1
    if choose_day(dtm_event) == 1:
        week_num += 1  # small error fix for sundays
    print(week_num)
    return SHEET_DICT[week_num]


def choose_day(dtm_event):
    """
    returns the day of the week properly
    :param dtm_event:
    :return: 1 for sunday, 2 for monday...
    """
    day = dtm_event.date().isoweekday()
    if day == 7:
        day = 0
    day += 1
    return day


def write_events_to_db(events):
    """
    writes the event to the excel database
    :param events: list of event string as received from google calendar
    :return: n/a
    """
    i = ROW_EVENTS_START
    prev_day = 0
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        print("Writing event: ", event['summary'])
        dtm_start = dtm_str_to_obj(start)
        dtm_end = dtm_str_to_obj(end)
        elapsed_time = dtm_end - dtm_start
        correct_sheet = choose_sheet(dtm_start)
        print("the sheet is ", correct_sheet)
        if correct_sheet != 0:
            day = choose_day(dtm_start)
            if day != prev_day:
                i = ROW_EVENTS_START
                prev_day = day
            i_ = str(i)
            # write from:
            SHEET1['A' + i_] = str(dtm_start.time())[0:5]
            correct_sheet[COL_FROM_DICT[day] + i_] = str(dtm_start.time())[0:5]
            # write to:
            SHEET1['B' + i_] = str(dtm_end.time())[0:5]
            correct_sheet[COL_TO_DICT[day] + i_] = str(dtm_end.time())[0:5]
            # write name:
            SHEET1['C' + i_] = str(event['summary'])
            correct_sheet[COL_NAME_DICT[day] + i_] = str(event['summary'])
            # write length:
            SHEET1['D' + i_] = str(elapsed_time)[0:4]  # time up to 9:59
            correct_sheet[COL_LEN_DICT[day] + i_] = str(elapsed_time)[0:4]
            # increment i
            i += 1
    save()


def save():
    DB.save(DATABASE_FILE)
    return


def tests():
    # tests:
    print(SHEET1[COL_A + str(1)].value)   # output should be test
    print(SHEET1['A2'].value)       # output should be 2
    SHEET1[COL_A + str(5)] = "write test22222"
    save()


if __name__ == '__main__':
    tests()
