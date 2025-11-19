import re
from urllib.parse import urlparse

def extract_features(url: str) -> dict:
    if not isinstance(url, str):
        url = str(url)

    url = url.strip()
    if url == "" or url == ".":
        url = "invalid-url"

    features = {}
    features["url_length"] = len(url)
    features["num_dots"] = url.count('.')
    features["num_hyphens"] = url.count('-')
    features["num_slash"] = url.count('/')
    features["num_question"] = url.count('?')
    features["num_equals"] = url.count('=')
    features["num_at"] = url.count('@')
    features["num_percent"] = url.count('%')
    features["has_https"] = int(url.lower().startswith("https"))
    features["has_ip"] = int(bool(re.search(r"\d+\.\d+\.\d+\.\d+", url)))

    # SAFE domain parsing
    try:
        parsed = urlparse(url if url.startswith(("http://", "https://")) else "http://" + url)
        domain = parsed.netloc

        # Handle invalid/missing domain
        if not domain or domain.strip() == "" or domain == ".":
            domain = "unknown-domain"

    except Exception:
        domain = "unknown-domain"

    features["domain_length"] = len(domain)
    features["subdomain_count"] = domain.count(".")

    return features
