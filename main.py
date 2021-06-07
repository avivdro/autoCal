"""
aviv drori
main code
calls for get_events and then writes to database
"""
import list_events
import database

HOW_MANY_EVENTS = 110


def main():
    events = list_events.get_events(HOW_MANY_EVENTS)
    database.write_events_to_db(events)


if __name__ == '__main__':
    main()
