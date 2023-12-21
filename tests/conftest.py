import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://api.github.com"

@pytest.fixture()
def api_request_context():
    with sync_playwright() as pw:
        request_context = pw.request.new_context(base_url=BASE_URL)
        yield request_context
        request_context.dispose()