"""
aviv drori
may 2021
This file uses opnenpyxl to read and write to the excel
"""

import openpyxl
from openpyxl import load_workbook
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
ROW_EVENTS_END = 13
# EXCEL SHEET STARTUP
DB = load_workbook(DATABASE_FILE)
SHEET1 = DB[SHEET1_NAME]
SHEET_DICT = {23: DB[WEEK_23_NAME], 24: DB[WEEK_24_NAME], 25: DB[WEEK_25_NAME],
              26: DB[WEEK_26_NAME], 1: DB[WEEK_1_NAME], 2: DB[WEEK_2_NAME]}

# TODO init the other sheets


def should_write(event_summary):
    """
    checks if event contains a forbidden substring like "without studies"
    :param event_summary: string of the name of the event
    :return: BOOL - True if event should be written, False otherwise
    """
    return True
    # todo write the function...


def dtm_str_to_obj(dtm_string):
    """
    :param dtm_string: string representing datetime, from google calendar
    :return: dtm: datetime object of the input
    """
    if len(dtm_string) == 10:   # like 2021-05-31
        # print("Full-day event.")
        return datetime(2020, 1, 1, 1, 1, 1)  # arbitrary time
    # time_ = time_string[11:19]
    time_obj = time(int(dtm_string[11:13]), int(dtm_string[14:16], 0))
    # print(time_obj)
    date_obj = date(int(dtm_string[0:4]), int(dtm_string[5:7]),
                    int(dtm_string[8:10]))
    # print(date_obj)
    dtm = datetime.combine(date_obj, time_obj)
    # print(dtm)
    return dtm


def choose_sheet(dtm_event):
    """
    returns the sheet corresponding to the week of the event
    :param dtm_event: datetime obj of the event
    :return: execl sheet - if event shouldn't be written, return 0
    """
    if dtm_event == datetime(2020, 1, 1, 1, 1, 1):   # this is the arbitrary datetime for whole day events
        return 0
    week_num = dtm_event.isocalendar()[1] + 1
    # TODO check this around week 26, 1...
    if choose_day(dtm_event) == 1:
        week_num += 1  # small error fix for sundays
    week_num = week_num % 27
    if week_num == 0:
        week_num = 1
    # print("DEBUG ", week_num)
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


def write_event(sheet, i, day, dtm_start, dtm_end, name, elapsed_time):
    """
    writes everything to the given sheet and to the SHEET1 - overlook
    :param sheet: Excel sheet to write to
    :param i: int - row
    :param day: int - 1=sunday, 2=monday..
    :param dtm_start: datetime of event start
    :param dtm_end: datetime of event end
    :param name: name of the event
    :param elapsed_time: elapsed time of event
    :return: none
    """
    i_ = str(i)
    # write from:
    SHEET1['A' + i_] = str(dtm_start.time())[0:5]
    sheet[COL_FROM_DICT[day] + i_] = str(dtm_start.time())[0:5]
    # write to:
    SHEET1['B' + i_] = str(dtm_end.time())[0:5]
    sheet[COL_TO_DICT[day] + i_] = str(dtm_end.time())[0:5]
    # write name:
    SHEET1['C' + i_] = name
    sheet[COL_NAME_DICT[day] + i_] = name
    # write length:
    SHEET1['D' + i_] = str(elapsed_time)[0:4]  # time up to 9:59
    sheet[COL_LEN_DICT[day] + i_] = str(elapsed_time)[0:4]
    # increment i


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
        print("Received event: ", event['summary'], end="")
        dtm_start = dtm_str_to_obj(start)
        dtm_end = dtm_str_to_obj(end)
        elapsed_time = dtm_end - dtm_start
        correct_sheet = choose_sheet(dtm_start)

        if correct_sheet != 0:
            print(" to sheet ", correct_sheet)
            day = choose_day(dtm_start)
            if day != prev_day:
                i = ROW_EVENTS_START
                prev_day = day
            if i == ROW_EVENTS_END:
                print("ERROR: Overflow: Too many events to write.")
            else:
                write_event(correct_sheet, i, day, dtm_start, dtm_end, str(event['summary']), elapsed_time)
                i += 1
        else:
            print(" - Event not written.")

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
