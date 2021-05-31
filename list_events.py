"""
aviv drori, may 2021
base from: https://karenapp.io/articles/how-to-automate-google-calendar-with-python-using-the-calendar-api/
"""

from datetime import datetime, time, date, timedelta
from cal_setup import get_calendar_service
import re
# TODO  regex needed?


CALENDAR_ID = 'c_gjgaqdjibjd14j93eannsmps3c@group.calendar.google.com'
HOW_MANY_EVENTS = 20


def new_get_time(dtm_string):
    """
    @:param: dtm_string: string representing datetime, from google calendar
    @:return: dtm: datetime object of the input
    """
    if len(dtm_string) == 10:   # like 2021-05-31
        # print("Full-day event.")
        return datetime(2020, 1, 1, 1, 1, 1)
    # time_ = time_string[11:19]
    time_obj = time(int(dtm_string[11:13]), int(dtm_string[14:16], 0))
    # print(time_obj)
    date_obj = date(int(dtm_string[0:4]), int(dtm_string[5:7]), int(dtm_string[8:10]))
    # print(date_obj)
    dtm = datetime.combine(date_obj, time_obj)
    # print(dtm)
    return dtm


def main():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time  // datetime.datetime?
    print('Getting List of 10 events')
    events_result = service.events().list(
        calendarId=CALENDAR_ID, timeMin=now,
        maxResults=HOW_MANY_EVENTS, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        event_time = event['end'].get('dateTime', event['end'].get('date'))
        # print(start, event['summary'], "TIME: ", event_time)
        print(event['summary'])
        # print(start, "---", end)
        dtm_start = new_get_time(start)
        dtm_end = new_get_time(end)
        dlt = dtm_end - dtm_start
        print("LENGTH: ", dlt)
        print("____________________________")


if __name__ == '__main__':
    main()
