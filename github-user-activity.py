import requests
import sys

username = sys.argv[1] if len(sys.argv) > 1 else input("Enter GitHub username: ")
if not username:
    print("Username cannot be empty.")
    exit(1)

try:
    r = requests.get(f'https://api.github.com/users/{username}/events')
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    exit(1)

if r.status_code != 200:
    print(f"Failed to retrieve data: {r.status_code} - {r.reason}")
    exit(1)

events = r.json()
if not isinstance(events, list):
    print("Unexpected response format.")
    exit(1)

for event in events:
    if event['type'] == 'PushEvent':
        print(f"commit in the repo  {event['repo']['name']},at {event['created_at']}")
    elif event['type'] == 'PullRequestEvent':
        print(f"pull request in the repo {event['repo']['name']}, at {event['created_at']}")
    elif event['type'] == 'IssuesEvent':
        print(f"issue in the repo {event['repo']['name']}, at {event['created_at']}")
    elif event['type'] == 'ForkEvent':
        print(f"forked the repo {event['repo']['name']}, at {event['created_at']}")
    elif event['type'] == 'IssueCommentEvent':
        print(f"commented on an issue in the repo {event['repo']['name']}, at {event['created_at']}")