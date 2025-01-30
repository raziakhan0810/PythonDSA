import requests

base_url = 'www.example'

# first api call
first_api_response = requests.get(base_url+'/user')
first_data_response = first_api_response.json()

# second api call
second_api_response = requests.get(base_url+'/child')
second_data_response = second_api_response.json()

microcode_to_id = {item['microcode']: item["id"] for item in second_data_response}

result1 = [
    {"name": child["name"], "microcode": child["microcode"]}
    for child in first_data_response["children"]
]
if {"name": "test", "microcode": "1.2.1"} not in result1:
    result1.append({"name": "test", "microcode": "1.2.1"})

result1 = sorted(result1, key=lambda x: x["microcode"], reverse=True)

result2 = [
    {"id": microcode_to_id[item["microcode"]], "name": item["name"], "microcode": item["microcode"]}
    for item in result1
    if item["microcode"] in microcode_to_id
]

# third api call
headers = {"Content-Type": "application/json"}
third_api_response = requests.post(base_url+'/child', json=result2, headers=headers)
third_data_response = third_api_response.json()

if third_api_response.status_code == 201:
    print("Data created successfully:")
    third_data_response = third_api_response.json()
    print(third_data_response)
else:
    print("Failed to create data. Status code:", third_api_response.status_code)

