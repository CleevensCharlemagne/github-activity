from .api import get_commit_count

def parse_events(events):
    results = []

    for event in events:
        repo = event["repo"]["name"]

        if event["type"] == "PushEvent":
            payload = event["payload"]

            if "commits" in payload:
                count = len(payload["commits"])
            else:
                owner, repo_name = repo.split("/")
                count = get_commit_count(
                    owner,
                    repo_name,
                    payload["before"],
                    payload["head"]
                )

            results.append(f"Pushed {count} commits to {repo}")

        elif event["type"] == "IssuesEvent" and event["payload"]["action"] == "opened":
            results.append(f"Opened a new issue in {repo}")

        elif event["type"] == "WatchEvent":
            results.append(f"Starred {repo}")

        elif event["type"] == "ForkEvent":
            results.append(f"Forked {repo}")

        elif event["type"] == "PullRequestEvent" and event["payload"]["action"] == "opened":
            results.append(f"Opened a pull request in {repo}")

    return results