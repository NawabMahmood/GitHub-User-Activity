#!/usr/bin/env python3

import sys
import json
import urllib.request
import urllib.error

GITHUB_API_URL = "https://api.github.com/users/{username}/events"

def fetch_user_activity(username):
    """
    Fetch the recent activity for a GitHub user using the GitHub API.
    Returns the parsed JSON response or None if an error occurs.
    """
    url = GITHUB_API_URL.format(username=username)
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = response.read().decode("utf-8")
                return json.loads(data)
            else:
                print(f"Error: Received status code {response.status}")
                return None
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def parse_event(event):
    """
    Parse a single GitHub event and return a readable string describing the event.
    """
    event_type = event.get("type", "")
    repo_name = event.get("repo", {}).get("name", "Unknown/Repository")

    if event_type == "PushEvent":
        commit_count = len(event.get("payload", {}).get("commits", []))
        return f"Pushed {commit_count} commits to {repo_name}"

    elif event_type == "IssuesEvent":
        action = event.get("payload", {}).get("action", "did something with an issue")
        issue_number = event.get("payload", {}).get("issue", {}).get("number", "")
        return f"{action.capitalize()} issue #{issue_number} in {repo_name}"

    elif event_type == "WatchEvent":
        # Typically WatchEvent means the user starred a repo
        return f"Starred {repo_name}"

    else:
        # Fallback for events not explicitly handled
        return f"{event_type} on {repo_name}"

def display_activity(events):
    """
    Display the GitHub activity events in the terminal.
    """
    if not events:
        print("No recent activity found or an error occurred.")
        return

    for event in events:
        description = parse_event(event)
        print(f"- {description}")

def main():
    if len(sys.argv) < 2:
        print("Usage: github_activity <username>")
        sys.exit(1)

    username = sys.argv[1].strip()
    events = fetch_user_activity(username)
    if events is not None:
        display_activity(events)
    else:
        print("Failed to fetch user activity.")

if __name__ == "__main__":
    main()
