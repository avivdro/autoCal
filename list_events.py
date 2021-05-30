import datetime
from cal_setup import get_calendar_service


def main():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting List of 20 events')
    events_result = service.events().list(
        calendarId='c_gjgaqdjibjd14j93eannsmps3c@group.calendar.google.com', timeMin=now,
        maxResults=20, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        event_time = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'], "TIME: ", event_time)


if __name__ == '__main__':
    main()