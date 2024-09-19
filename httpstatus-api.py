import requests

headers = {
    'Host': 'backend-v2.httpstatus.io',
    'Sec-Ch-Ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
    'Accept': 'application/json, text/plain, */*',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://httpstatus.io',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://httpstatus.io/',
    'Priority': 'u=1, i',
}

json_data = {
    'urls': [
        'https://tiktok.com/@316d',
        'https://tiktok.com/@317d',
        'https://tiktok.com/@318d',
        'https://tiktok.com/@303d',
        'https://tiktok.com/@304d',
        'https://tiktok.com/@305d',
        'https://tiktok.com/@306d',
        'https://tiktok.com/@307d',
        'https://tiktok.com/@308d',
        'https://tiktok.com/@309d',
        'https://tiktok.com/@310d',
        'https://tiktok.com/@311d',
        'https://tiktok.com/@312d',
        'https://tiktok.com/@313d',
        'https://tiktok.com/@314d',
        'https://tiktok.com/@315d',
    ],
    'userAgent': 'browser',
    'userName': '',
    'passWord': '',
    'headerName': '',
    'headerValue': '',
    'strictSSL': True,
    'canonicalDomain': False,
    'additionalSubdomains': [
        'www',
    ],
    'followRedirect': True,
    'throttleRequests': 100,
    'escapeCharacters': False,
}

response = requests.post('https://backend-v2.httpstatus.io/api', headers=headers, json=json_data).json()
for res in response:
    print(res['statusCode'])