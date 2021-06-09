"""
aviv drori, may 2021
base from: https://karenapp.io/articles/
how-to-automate-google-calendar-with-python-using-the-calendar-api/
"""

from datetime import datetime
from cal_setup import get_calendar_service

# todo remove commented id
DEFAULT_CALENDAR_ID = 'c_gjgaqdjibjd14j93eannsmps3c@group.calendar.google.com'
HOW_MANY_EVENTS = 50


def get_events(calendar_id, how_many=HOW_MANY_EVENTS):
    service = get_calendar_service()  # Call the Calendar API
    # getting the time of this morning, 6 A.M
    this_morning = datetime.utcnow().replace(hour=6, minute=0, second=0)\
        .isoformat() + 'Z'
    print('Getting List of ', how_many, ' events:')
    events_result = service.events().list(
        calendarId=calendar_id, timeMin=this_morning,
        maxResults=how_many, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return []
    else:
        return events


"""
if __name__ == '__main__':
    get_events()
"""
