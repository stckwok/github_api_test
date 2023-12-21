from playwright.sync_api import APIRequestContext


def create_repository(
    api_request_context: APIRequestContext,
    repo_name: str,
    is_private: bool,
    api_token: str,
):
    return api_request_context.post(
        "/user/repos",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {api_token}",
        },
        data={"name": repo_name, "private": is_private},
    )


def create_issue(
    api_request_context: APIRequestContext,
    github_user: str,
    repo_name: str,
    api_token: str,
    title: str,
    issue_body: str,
):
    return api_request_context.post(
        f"/repos/{github_user}/{repo_name}/issues",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {api_token}",
        },
        data={"title": title, "body": issue_body},
    )


def get_all_issue(
    api_request_context: APIRequestContext,
    github_user: str,
    repo_name: str,
    api_token: str,
) -> list:
    return api_request_context.get(
        f"/repos/{github_user}/{repo_name}/issues",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {api_token}",
        },
    )


def update_repository(
    api_request_context: APIRequestContext,
    repo_name: str,
    repo_update_name: str,
    username: str,
    description: str,
    is_private: bool,
    api_token: str,
):
    return api_request_context.patch(
        f"/repos/{username}/{repo_name}",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {api_token}",
        },
        data={
            "name": repo_update_name,
            "description": description,
            "private": is_private,
        },
    )


def remove_repository(
    api_request_context: APIRequestContext,
    repo_name: str,
    username: str,
    api_token: str,
):
    return api_request_context.delete(
        f"/repos/{username}/{repo_name}",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {api_token}",
        },
    )
