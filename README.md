A simple command-line interface (CLI) tool, written in Python, for fetching and displaying the recent public activity of any GitHub user. It uses only Python’s built-in libraries (urllib, json, sys) and does not require any external dependencies.

Features
Fetch Recent GitHub Events: Displays events such as push commits, opened issues, and repository stars.
No External Dependencies: Relies on Python’s standard library only.
Error Handling: Gracefully manages HTTP errors or invalid usernames.
Easy to Extend: Add or modify event types as you see fit.
Requirements
Python 3 installed on your system.
A stable internet connection to fetch data from the GitHub API.
Installation
Clone or Download this Repository
bash
Copy
git clone https://github.com/<your-username>/GitHub-User-Activity.git
Navigate into the Project Directory
bash
Copy
cd GitHub-User-Activity
(Optional) Make the Script Executable (macOS/Linux)
bash
Copy
chmod +x github_activity.py
Usage
1. Using Python Directly
bash
Copy
python3 github_activity.py <username>
Replace <username> with the GitHub username you want to fetch activity for. Example:

bash
Copy
python3 github_activity.py torvalds
2. Running as an Executable (macOS/Linux)
bash
Copy
./github_activity.py <username>
Example:

bash
Copy
./github_activity.py torvalds
Output Example
text
Copy
- Pushed 3 commits to torvalds/linux
- Opened issue #5 in torvalds/linux
- Starred torvalds/subsurface
...
How It Works
Fetch Data: The script uses urllib.request to call the GitHub Events API endpoint:
bash
Copy
https://api.github.com/users/<username>/events
Parse JSON: It parses the returned JSON data (list of events).
Display Activity: Each event is checked for its type (e.g., PushEvent, IssuesEvent, WatchEvent) and printed in a human-readable format.
Customization
Add Event Types: In parse_event(event), you can handle more GitHub event types (like PullRequestEvent, ForkEvent, etc.).
Filter Results: You can implement additional command-line arguments (e.g., --type=PushEvent) to filter event types.
Caching: Implement caching to reduce API calls if you plan to run the script frequently.
Error Handling
Invalid Username: If GitHub returns a 404, the script prints an error message.
Network Issues: urllib.error.URLError is caught and shows a brief error message.
Status Codes: If the status code isn’t 200, the script prints out the received status code.


Idea By:
https://roadmap.sh/projects/github-user-activity




