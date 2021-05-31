from datetime import datetime, time, date, timedelta
from cal_setup import get_calendar_service
import re


def new_get_time(dtm_string):
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


"""
def add_time(element):
    datetime_ = element['start'].get('dateTime')
    time_pattern = re.compile("..:..:..")
    added_time_pattern = re.compile("\+..:..")
    full_time_pattern = re.compile("..:..:..\+..:..")

    time = time_pattern.search(datetime_).group(0)
    added_time = added_time_pattern.search(datetime_).group(0)

    added_time_obj = datetime.strptime(added_time[1:], "%H:%M")
    time_obj = datetime.strptime(time, "%H:%M:%S")
    print(added_time_obj, " --- ", time_obj)
"""


def main():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time  // datetime.datetime?
    print('Getting List of 10 events')
    events_result = service.events().list(
        calendarId='c_gjgaqdjibjd14j93eannsmps3c@group.calendar.google.com', timeMin=now,
        maxResults=20, singleEvents=True,
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
