from github import Github
import requests
# using an access token

# Github Enterprise with custom hostname
g = Github(base_url="https://github.com/CyberJackGit/build-test/api/v3", login_or_token="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")


g.get_repo(id)