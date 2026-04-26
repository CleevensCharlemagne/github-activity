import argparse
from .api import get_user_events
from .services import parse_events

def main():
    parser = argparse.ArgumentParser(description="GitHub Activity CLI")
    parser.add_argument("username", help="GitHub username")

    args = parser.parse_args()

    events = get_user_events(args.username)
    results = parse_events(events)

    for line in results:
        print(line)