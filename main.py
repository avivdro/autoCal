"""
aviv drori
main code
calls for get_events and then writes to database
"""
import list_events
import database


def main():
    events = list_events.get_events()
    database.write_events_to_db(events)


if __name__ == '__main__':
    main()
