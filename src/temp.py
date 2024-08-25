import requests
from datetime import datetime
repo_name = "readme-generator"


def get_github_property_value(url, get_property):
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        if get_property == "latest_release":
            return json_response['tag_name'] 
        elif get_property == "commits":
            return json_response[0]['commit']['committer']['date']
        else:
            return None
    else:
        return None


url_latest_release = f"https://api.github.com/repos/charudatta10/{repo_name}/releases/latest"

# Replace 'username' and 'repository' with the actual username and repository name
url_commits = f"https://api.github.com/repos/charudatta10/{repo_name}/commits"

# Example usage

latest_release_value =  get_github_property_value(url_latest_release, "latest_release")
commits_date =  get_github_property_value(url_commits, "commits" )
days_since_commit = (datetime.now() - datetime.strptime(commits_date, '%Y-%m-%dT%H:%M:%SZ')).days
print(f"Latest tag: {latest_release_value}, Latest commit: {days_since_commit} days ")