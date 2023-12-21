from playwright.sync_api import APIRequestContext

def create_repository(api_request_context: APIRequestContext,
                      repo_name: str, is_private: bool, api_token: str):
    return api_request_context.post(
        "/user/repos",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {api_token}",
        },
        data={"name": repo_name, "private": is_private},
    )

def update_repository(api_request_context: APIRequestContext,
                            repo_name: str, repo_update_name: str,
                            username: str, description: str,
                            is_private: bool, api_token: str):
    return api_request_context.patch(
        f"/repos/{username}/{repo_name}",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {api_token}",
        },
        data={"name": repo_update_name, "description": description, 
              "private": is_private},
    )

def remove_repository(api_request_context: APIRequestContext, 
                      repo_name: str, username: str, api_token: str):
    return api_request_context.delete(
        f"/repos/{username}/{repo_name}",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {api_token}",
        },
    )

