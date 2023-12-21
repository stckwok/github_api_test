import os
import time
import datetime
from playwright.sync_api import APIRequestContext
from github_api import create_repository, create_issue, get_all_issue,\
        update_repository, remove_repository

# export API_PWRIGHT="Personal-Access-Token-(classic)"
API_TOKEN = os.getenv('API_PWRIGHT')
USER_NAME = os.getenv('USER_NAME')
REPO_NAME = "test-ghapi-repo"
NEW_REPO_NAME = "new-test-ghapi-repo"
UPDATE_REPO_NAME = "test-ghapi-repo-update"
REPO_DESCRIPTION = f"Updated description of {UPDATE_REPO_NAME}"
NUM_ISSUES = 5

issues_list=[]

def test_create_scenario(api_request_context: APIRequestContext):
    # Create a new repository
    response_create_repo = create_repository(
                                api_request_context=api_request_context,
                                repo_name=REPO_NAME, is_private=True,
                                api_token=API_TOKEN)
    assert response_create_repo.status == 201
    assert response_create_repo.status_text == 'Created'

def test_create_issue_scenario(api_request_context: APIRequestContext):
    # Create issues
    for i in range(NUM_ISSUES):
        title_i = "[BUG {}] At Time: {}".format(i, datetime.datetime.now().strftime("%H:%M:%S"))
        issue_body_i = f"Test {i} failed when executed at time"
        issues_list.append({title_i:issue_body_i})
        response_create_issue = create_issue(
                                    api_request_context=api_request_context,
                                    github_user=USER_NAME, repo_name=REPO_NAME,
                                    api_token=API_TOKEN,
                                    title = title_i,
                                    issue_body = issue_body_i
                                    )
        assert response_create_issue.status == 201
        assert response_create_issue.status_text == 'Created'

def test_issue_in_repo_scenario(api_request_context: APIRequestContext):
    # Get issues
    response_all_issues = get_all_issue(
                                    api_request_context=api_request_context,
                                    github_user=USER_NAME, repo_name=REPO_NAME,
                                    api_token=API_TOKEN
    )
    new_issues_list = [ {issue["title"]:issue["body"]} for issue in response_all_issues.json() if "BUG" in issue["title"] ]
    # print(new_issues_list)
    # print("\n")
    # print(issues_list)
    assert [i for i in issues_list if i not in new_issues_list] == []

def test_remove_scenario(api_request_context: APIRequestContext):
    # Remove the repository
    response_delete_a_repo = remove_repository(
                                api_request_context=api_request_context,
                                repo_name=REPO_NAME,
                                username=USER_NAME,
                                api_token=API_TOKEN)
    assert response_delete_a_repo.status == 204


def test_create_update_remove_scenario(api_request_context: APIRequestContext):
    # Create a new repository
    response_create_repo = create_repository(
                                api_request_context=api_request_context,
                                repo_name=NEW_REPO_NAME, is_private=True,
                                api_token=API_TOKEN)
    assert response_create_repo.status == 201
    assert response_create_repo.status_text == 'Created'
    # print(response_create_repo)

    # Update name and description of the repository
    response_update_repo = update_repository(
                                api_request_context=api_request_context,
                                repo_name=NEW_REPO_NAME,
                                repo_update_name=UPDATE_REPO_NAME,
                                username=USER_NAME,
                                description=REPO_DESCRIPTION,
                                is_private=False,
                                api_token=API_TOKEN)
    response_body_update_repo = response_update_repo.json()
    assert response_update_repo.status == 200
    assert response_body_update_repo["name"] == UPDATE_REPO_NAME
    assert response_body_update_repo["description"] == REPO_DESCRIPTION
    assert response_body_update_repo['private'] == False
    # print(response_body_update_repo)

    # Remove the repository
    response_delete_a_repo = remove_repository(
                                api_request_context=api_request_context,
                                repo_name=UPDATE_REPO_NAME,
                                username=USER_NAME,
                                api_token=API_TOKEN)
    assert response_delete_a_repo.status == 204