import re

sites = [ "toumei.co.jp", "example.com" ]

test_urls = [
    "https://example.com/",
    "https://www.example.com/",
    "https://dummy.com/example.com/"
]

for url in test_urls:
    for site in sites:
        pattern = re.compile(r'https?://\w*\.?{0}/.*'.format(site), flags=re.IGNORECASE)
        match = re.search(pattern, url)

        print(url)
        print(site)
        if match:
            print("あり")
        else:
            print("なし")
