import requests

BASE_URL = "https://api.github.com"

def get_user_events(username):
    url = f"{BASE_URL}/users/{username}/events"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}")

    return response.json()


def get_commit_count(owner, repo, base, head):
    url = f"{BASE_URL}/repos/{owner}/{repo}/compare/{base}...{head}"
    response = requests.get(url)

    if response.status_code != 200:
        return 0

    return response.json().get("total_commits", 0)