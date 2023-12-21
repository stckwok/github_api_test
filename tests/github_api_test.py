import os
import pytest
from playwright.sync_api import APIRequestContext, sync_playwright
from github_api import create_repository, update_repository, remove_repository

# export API_PWRIGHT="Personal-Access-Token-(classic)"
API_TOKEN = os.getenv('API_PWRIGHT')
USER_NAME = os.getenv('USER_NAME')

@pytest.fixture()
def api_request_context():
    with sync_playwright() as pw:
        request_context = pw.request.new_context(base_url="https://api.github.com")
        yield request_context
        request_context.dispose()

def test_create_remove_scenario(api_request_context: APIRequestContext):
    # Create a new repository
    response_create_repo = create_repository(
                                api_request_context=api_request_context,
                                repo_name="test-ghapi-repo", is_private=True,
                                api_token=API_TOKEN)
    assert response_create_repo.status == 201
    assert response_create_repo.status_text == 'Created'
    # print(response_create_repo)

    # Update name and description of the repository
    response_update_repo = update_repository(
                                api_request_context=api_request_context,
                                repo_name="test-ghapi-repo",
                                repo_update_name="test-ghapi-repo-update",
                                username=USER_NAME,
                                description="Update description",
                                is_private=False,
                                api_token=API_TOKEN)
    response_body_update_repo = response_update_repo.json()
    assert response_update_repo.status == 200
    assert response_body_update_repo["name"] == "test-ghapi-repo-update"
    assert response_body_update_repo["description"] == "Update description"
    assert response_body_update_repo['private'] == False
    # print(response_body_update_repo)

    import time
    time.sleep(10)
    # Remove the repository
    response_delete_a_repo = remove_repository(
                                api_request_context=api_request_context,
                                repo_name="test-ghapi-repo-update",
                                username=USER_NAME,
                                api_token=API_TOKEN)
    assert response_delete_a_repo.status == 204