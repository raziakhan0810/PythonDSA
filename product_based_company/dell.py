first_data = {
    "name": "test",
    "microcode": "1.2.1",
    "children": [
        {"name": "test2", "microcode": "1.2.2"},
        {"name": "test3", "microcode": "1.2.3"}
    ]
}

second_data = [
    {"id": 1, "microcode": "1.2.1"},
    {"id": 2, "microcode": "1.2.2"},
    {"id": 3, "microcode": "1.2.3"}
]

microcode_to_id = {item['microcode']: item["id"] for item in second_data}

result1 = [
    {"name": child["name"], "microcode": child["microcode"]}
    for child in first_data["children"]
]
if {"name": "test", "microcode": "1.2.1"} not in result1:
    result1.append({"name": "test", "microcode": "1.2.1"})

result1 = sorted(result1, key=lambda x: x["microcode"], reverse=True)

result2 = [
    {"id": microcode_to_id[item["microcode"]], "name": item["name"], "microcode": item["microcode"]}
    for item in result1
    if item["microcode"] in microcode_to_id
]

print("Result1:", result1)
print("Result2:", result2)