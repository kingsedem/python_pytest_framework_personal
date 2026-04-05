def build_request_headers(content_type="application/json", access_token=None):
    headers = {"Content-Type": content_type}
    if access_token:
        headers["Authorization"] = f"Bearer {access_token}"
    return headers