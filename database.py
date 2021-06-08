"""
aviv drori
may 2021
This file uses opnenpyxl to read and write to the excel
"""

from openpyxl import load_workbook
from datetime import datetime, time, date

# EXCEL FILE CONSTANTS:
DATABASE_FILE = 'database.xlsx'  # this file needs to be in same dir

# WEEKS:
WEEK_24_NAME = 'week24'
WEEK_25_NAME = 'week25'
WEEK_26_NAME = 'week26'
WEEK_1_NAME = 'week1'
WEEK_2_NAME = 'week2'
WEEK_3_NAME = 'week3'
WEEK_4_NAME = 'week4'
# add more as i go...

# WRITE HISTORY:
SHEET_HISTORY_NAME = 'WriteHistory'
LAST_WRITE_CELL = 'G3'

# COL_DAYS
COL_FROM_DICT = {1: 'A', 2: 'E', 3: 'I', 4: 'M', 5: 'Q', 6: 'U', 7: 'Y'}
COL_TO_DICT = {1: 'B', 2: 'F', 3: 'J', 4: 'N', 5: 'R', 6: 'V', 7: 'Z'}
COL_NAME_DICT = {1: 'C', 2: 'G', 3: 'K', 4: 'O', 5: 'S', 6: 'W', 7: 'AA'}
COL_LEN_DICT = {1: 'D', 2: 'H', 3: 'L', 4: 'P', 5: 'T', 6: 'X', 7: 'AB'}
# ROWS
ROW_EVENTS_START = 7
ROW_EVENTS_END = 15
# EXCEL SHEET STARTUP
DB = load_workbook(DATABASE_FILE)
SHEET_HISTORY = DB[SHEET_HISTORY_NAME]

SHEET_DICT = {24: DB[WEEK_24_NAME], 25: DB[WEEK_25_NAME], 26: DB[WEEK_26_NAME],
              1: DB[WEEK_1_NAME], 2: DB[WEEK_2_NAME], 3: DB[WEEK_3_NAME],
              4: DB[WEEK_4_NAME]}
# TODO init the other sheets
# FILTER
BAD_STRINGS = ["ללא לימודים", "יום הולדת"]
FILTERED_SHEET_NAME = 'filtered'
SHEET_FILTERED = DB[FILTERED_SHEET_NAME]
FILTER_LAST_ROW = 'H2'


def should_write(event_obj):
    """
    checks if event contains a forbidden substring like "without studies",
     or whole day/zero time
    :param event_obj: event object
    :return: BOOL - True if event should be written, False otherwise
    """
    start = event_obj['start'].get('dateTime', event_obj['start'].get('date'))
    dtm_start = dtm_str_to_obj(start)
    correct_sheet = choose_sheet(dtm_start)
    if correct_sheet == 0:
        print("    Event not written: Filtered: whole day event")
        write_to_filtered_list(event_obj, "whole day event")
        return False
    event_summary = event_obj['summary']
    for bad_word in BAD_STRINGS:
        if bad_word in event_summary:
            print("    Event not written: Filtered: contains string ", bad_word)
            write_to_filtered_list(event_obj, "contains string" + bad_word)
            return False
    return True


def write_to_filtered_list(event_obj, why):
    """
    writes the filtered events to the 'filtered' worksheet
    :param event_obj: the object that was filtered
    :param why: string representing reason event was filtered
    :return: None
    """
    row = int(SHEET_FILTERED[FILTER_LAST_ROW].value)
    row += 1
    row_ = str(row)
    dtm_start, dtm_end = event_to_datetime(event_obj)
    SHEET_FILTERED["A" + row_] = event_obj['summary']
    SHEET_FILTERED["B" + row_] = choose_week(dtm_start)
    SHEET_FILTERED["C" + row_] = str(dtm_start.date())
    SHEET_FILTERED["D" + row_] = str(dtm_start.time())[0:5]
    SHEET_FILTERED["E" + row_] = why
    SHEET_FILTERED[FILTER_LAST_ROW] = row


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
    week_num = choose_week(dtm_event)
    if week_num == 0:
        return 0
    return SHEET_DICT[choose_week(dtm_event)]


def choose_week(dtm_event):
    """
    :param dtm_event: datetime object of event
    :return: int representing air force week of the date
    """
    if dtm_event == datetime(2020, 1, 1, 1, 1, 1):   # this is the arbitrary datetime for whole day events
        return 0
    week_num = dtm_event.isocalendar()[1] + 1
    # TODO check this around week 26, 1... need to make something smaller?
    if choose_day(dtm_event) == 1:
        week_num += 1  # small error fix for sundays
    if week_num > 26:
        week_num -= 26
    if week_num == 0:
        week_num = 1
    return week_num


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


def write_event(event, i):
    """
    :param event: event obj to write to the file
    :param i: integer - the row to write to
    :return:
    """
    dtm_start, dtm_end = event_to_datetime(event)
    elapsed_time = (dtm_end - dtm_start).seconds / 3600  # hours
    # todo try and catch for nonexistent sheet
    sheet = choose_sheet(dtm_start)
    day = choose_day(dtm_start)
    i_ = str(i)
    week_num = choose_week(dtm_start)
    # write from:
    sheet[COL_FROM_DICT[day] + i_] = str(dtm_start.time())[0:5]
    # write to:
    sheet[COL_TO_DICT[day] + i_] = str(dtm_end.time())[0:5]
    # write name:
    sheet[COL_NAME_DICT[day] + i_] = str(event['summary'])
    # write length:
    sheet[COL_LEN_DICT[day] + i_] = elapsed_time
    print("  Writing to sheet %s, wk:%d, day:%d, hr:%s, len:%d"
          % (sheet, week_num, day, str(dtm_start.time())[0:5], elapsed_time))


def event_to_datetime(event):
    """
    Parses the info, just for cleaner code. JSON style.
    :param event: event object
    :return: datetime of start, datetime of end
    """
    start = event['start'].get('dateTime', event['start'].get('date'))
    end = event['end'].get('dateTime', event['end'].get('date'))
    dtm_start = dtm_str_to_obj(start)
    dtm_end = dtm_str_to_obj(end)
    return dtm_start, dtm_end


def log(how_many_events):
    """
    logs to the WriteHistory sheet
    :return: None
    """
    row = int(SHEET_HISTORY[LAST_WRITE_CELL].value)
    row += 1
    row_ = str(row)
    SHEET_HISTORY["A" + row_] = str(datetime.now())
    SHEET_HISTORY["B" + row_] = how_many_events
    SHEET_HISTORY[LAST_WRITE_CELL] = row
    SHEET_FILTERED[FILTER_LAST_ROW] = 1  # ready for next time
    print("Successfully logged to history.")


def write_events_to_db(events):
    """
    receives list of event and manages the filtering and writing.
    :param events: list of events as received from google calendar
    :return: n/a
    """
    events_written = 0
    i = ROW_EVENTS_START
    prev_day = 0
    for event in events:
        print("Received event: ", event['summary'])
        if should_write(event):
            dtm_start, dtm_end = event_to_datetime(event)
            day = choose_day(dtm_start)
            if day != prev_day:
                i = ROW_EVENTS_START
                prev_day = day
            if i == ROW_EVENTS_END:
                print("ERROR: Overflow: Too many events to write.")
                write_to_filtered_list(event, "OVERFLOW")
            else:
                write_event(event, i)
                i += 1
                events_written += 1
    log(len(events))
    save()
    print("--------------------------------------------------------------")
    print("Finished.\nGot ", len(events), " events, wrote ", events_written, " of them.")


def save():
    DB.save(DATABASE_FILE)
    print("Excel database saved.")
    return


def tests():
    # tests:
    save()


if __name__ == '__main__':
    tests()
