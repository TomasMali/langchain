import requests



def get_header():

    # Define the login endpoint and payload
    login_url = "http://localhost:8080/synergy2-ws/ws/base/login"
    login_payload = {
        "entity": {
            "lgnUsr": "devel",
            "lgnPsw": "d",
            "lngUid": 1
        }
    }
    headers = {"Content-Type": "application/json"}

    # Perform the login request
    response = requests.put(login_url, json=login_payload, headers=headers)
    if response.status_code != 200:
        print("Login failed")
        exit()

    # Extract the token from the response
    token = response.json()["result"]



    cookies = {
        # 'Idea-5b6939c2': 'c5f1510c-937f-4c5c-9833-364ff517994a',
        'token_Synergy2__IT01712150240-DEVEL-ENV-SVILUPPO': token,
    }

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'it-IT,it;q=0.9,la;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'http://localhost:4200/synergy/synergy-fis/global-options',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'token': token,
    }
    return headers

# response = requests.get('http://localhost:4200/synergy2-ws/ws/spec/sys/opt/SynergyOptions', cookies=cookies, headers=headers)



