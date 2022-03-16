from urllib.parse import urlparse
from urllib.parse import parse_qs

url = 'https://www.example.com/some_path?response-content-disposition=some_value'
parsed_url = urlparse(url)
captured_value = parse_qs(parsed_url.query)['response-content-disposition'][0]

print(captured_value)