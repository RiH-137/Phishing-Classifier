# importing required packages for this section
from urllib.parse import urlparse
import ipaddress
import re

# 1. Checks for IP address in URL (Have_IP)
def havingIP(url):
    try:
        ipaddress.ip_address(url)
        return 1
    except:
        return 0

# 2. Checks the presence of '@' in URL (Have_At)
def haveAtSign(url):
    if "@" in url:
        return 1
    else:
        return 0

# 3. Finding the length of URL and categorizing (URL_Length)
def getLength(url):
    if len(url) < 54:
        return 0
    else:
        return 1

# 4. Gives number of '/' in URL (URL_Depth)
def getDepth(url):
    depth = url.count('/')
    return depth

# 5. Checking for redirection '//' in the URL (Redirection)
def redirection(url):
    if '//' in url[7:]:
        return 1
    else:
        return 0

# 6. Existence of "https" in the domain part of the URL (https_Domain)
def httpDomain(url):
    domain = urlparse(url).netloc
    if 'https' in domain:
        return 1
    else:
        return 0

# 7. Checking for Shortening Services in URL (Tiny_URL)
def tinyURL(url):
    shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                          r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                          r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                          r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                          r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                          r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                          r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                          r"tr\.im|link\.zip\.net"
    match = re.search(shortening_services, url)
    if match:
        return 1
    else:
        return 0

# 8. Checking for Prefix or Suffix Separated by (-) in the Domain (Prefix/Suffix)
def prefixSuffix(url):
    domain = urlparse(url).netloc
    if '-' in domain:
        return 1
    else:
        return 0

# Example usage:
# url = "https://www.example.com/path/to/page"
# features = [havingIP(url), haveAtSign(url), getLength(url), getDepth(url), redirection(url), httpDomain(url),
#             tinyURL(url), prefixSuffix(url)]
# print(features)  # Output: [0, 0, 0, 3, 0, 1, 0, 0]
