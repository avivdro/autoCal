"""
aviv drori, may 2021
base from: https://karenapp.io/articles/
how-to-automate-google-calendar-with-python-using-the-calendar-api/
"""

from datetime import datetime, time, date, timedelta

import database
from cal_setup import get_calendar_service

CALENDAR_ID = 'c_gjgaqdjibjd14j93eannsmps3c@group.calendar.google.com'
HOW_MANY_EVENTS = 50


def get_events(how_many=HOW_MANY_EVENTS):
    service = get_calendar_service()  # Call the Calendar API
    # getting the time of this morning, 6 A.M
    this_morning = datetime.utcnow().replace(hour=6, minute=0, second=0).isoformat() + 'Z'
    # now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting List of ', how_many, ' events:')
    events_result = service.events().list(
        calendarId=CALENDAR_ID, timeMin=this_morning,
        maxResults=how_many, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return []
    else:
        return events


if __name__ == '__main__':
    get_events()
