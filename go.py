import requests

cookies = {
    'Idea-5b6939c2': 'c5f1510c-937f-4c5c-9833-364ff517994a',
    'token_Synergy2__IT01712150240-DEVEL-ENV-SVILUPPO': 'eyJhbGciOiJFUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjEzMDU1NjkxOTQyNiwiaWF0IjoxNzA3OTAwNjA2LCJpc3MiOiJJVDAxNzEyMTUwMjQwLURFVkVMLUVOVi1TVklMVVBQTyIsInN1YiI6ImRldmVsb3BlciIsImp0aSI6IjViMzU2MmQ5LWM2YjAtNGViMS1hOTgyLWI1OTFiOTFkNjAxYSIsIm5hbWUiOiJTdmlsdXBwYXRvcmUiLCJvcmlnaWQiOjUsIm5pY2tuYW1lIjoiZGV2ZWwiLCJhdWQiOlsiYXV0aCJdLCJjbmYiOiJJVDAxNzEyMTUwMjQwLURFVkVMLUVOVi1TVklMVVBQTyIsInNjb3BlIjoiU3luZXJneTIifQ.AMrmiEtDoFTxAZDAyQF1v5lrCevzVlFZ_3XAxzP7nxH74b3QQb732XLOuwaCnBM0sZMj4oSsCoVIpKzbV-jymUDrAErLwb7yjg0YcRK2Asn66GcxT_j0VvHQjZEshCxf9IbZVY60WpExdFFS1659Me-XleAqj-dIR7d2nKEf7H8di_4e',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'it-IT,it;q=0.9,la;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': 'Idea-5b6939c2=c5f1510c-937f-4c5c-9833-364ff517994a; token_Synergy2__IT01712150240-DEVEL-ENV-SVILUPPO=eyJhbGciOiJFUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjEzMDU1NjkxOTQyNiwiaWF0IjoxNzA3OTAwNjA2LCJpc3MiOiJJVDAxNzEyMTUwMjQwLURFVkVMLUVOVi1TVklMVVBQTyIsInN1YiI6ImRldmVsb3BlciIsImp0aSI6IjViMzU2MmQ5LWM2YjAtNGViMS1hOTgyLWI1OTFiOTFkNjAxYSIsIm5hbWUiOiJTdmlsdXBwYXRvcmUiLCJvcmlnaWQiOjUsIm5pY2tuYW1lIjoiZGV2ZWwiLCJhdWQiOlsiYXV0aCJdLCJjbmYiOiJJVDAxNzEyMTUwMjQwLURFVkVMLUVOVi1TVklMVVBQTyIsInNjb3BlIjoiU3luZXJneTIifQ.AMrmiEtDoFTxAZDAyQF1v5lrCevzVlFZ_3XAxzP7nxH74b3QQb732XLOuwaCnBM0sZMj4oSsCoVIpKzbV-jymUDrAErLwb7yjg0YcRK2Asn66GcxT_j0VvHQjZEshCxf9IbZVY60WpExdFFS1659Me-XleAqj-dIR7d2nKEf7H8di_4e',
    'Referer': 'http://localhost:4200/synergy/synergy-fis/global-options',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'token': 'eyJhbGciOiJFUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjEzMDU1NjkxOTQyNiwiaWF0IjoxNzA3OTAwNjA2LCJpc3MiOiJJVDAxNzEyMTUwMjQwLURFVkVMLUVOVi1TVklMVVBQTyIsInN1YiI6ImRldmVsb3BlciIsImp0aSI6IjViMzU2MmQ5LWM2YjAtNGViMS1hOTgyLWI1OTFiOTFkNjAxYSIsIm5hbWUiOiJTdmlsdXBwYXRvcmUiLCJvcmlnaWQiOjUsIm5pY2tuYW1lIjoiZGV2ZWwiLCJhdWQiOlsiYXV0aCJdLCJjbmYiOiJJVDAxNzEyMTUwMjQwLURFVkVMLUVOVi1TVklMVVBQTyIsInNjb3BlIjoiU3luZXJneTIifQ.AMrmiEtDoFTxAZDAyQF1v5lrCevzVlFZ_3XAxzP7nxH74b3QQb732XLOuwaCnBM0sZMj4oSsCoVIpKzbV-jymUDrAErLwb7yjg0YcRK2Asn66GcxT_j0VvHQjZEshCxf9IbZVY60WpExdFFS1659Me-XleAqj-dIR7d2nKEf7H8di_4e',
}

response = requests.get('http://localhost:4200/synergy2-ws/ws/spec/sys/opt/SynergyOptions', cookies=cookies, headers=headers)

# Handle the response
if response.status_code == 200:
    print("Request successful")
    try:
        print(response.json())
    except ValueError:
        print("Response content is not in JSON format:", response.content)
else:
    print("Request failed")
    print("Status code:", response.status_code)
    print("Response content:", response.content)