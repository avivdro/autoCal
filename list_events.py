"""
aviv drori, may 2021
base from: https://karenapp.io/articles/
how-to-automate-google-calendar-with-python-using-the-calendar-api/
"""

from datetime import datetime, time, date, timedelta

import database
from cal_setup import get_calendar_service


CALENDAR_ID = 'c_gjgaqdjibjd14j93eannsmps3c@group.calendar.google.com'
HOW_MANY_EVENTS = 60
WEEK_DELTA = 1


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


def main():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting List of 10 events')
    events_result = service.events().list(
        calendarId=CALENDAR_ID, timeMin=now,
        maxResults=HOW_MANY_EVENTS, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    else:
        database.write_events_to_db(events)
    """
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        print(event['summary'])
        dtm_start = dtm_str_to_obj(start)
        dtm_end = dtm_str_to_obj(end)
        elapsed_time = dtm_end - dtm_start
        print("LENGTH: ", elapsed_time)
        print("WEEK NUMBER: ", dtm_start.isocalendar()[1]+1)
        # TODO if the event is all day it translates to week number 1 (+1 =2)
        # need to fix it.
        print("____________________________")
    """


if __name__ == '__main__':
    main()
