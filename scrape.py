import requests

def get_csv(url, params, headers):
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Error fetching CSV file: {response.status_code}")


boats_url = "https://www.fitclub.site/api/report/club/equipment/inventoryboats"
boats_params = {
    "clubUid": "e41298f4-6ef2-4f08-b887-fedd5d12f3e9"
}

repairs_url = "https://www.fitclub.site/api/report/club/equipment/repairs"
repairs_params = {
    "clubUid": "e41298f4-6ef2-4f08-b887-fedd5d12f3e9",
    "statuses": ["REPORTED", "PARTS_ORDERED", "IN_PROGRESS", "COMPLETE"]
}

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJodW50ZXJhbm5hbkBnbWFpbC5jb20iLCJpYXQiOjE3MjY0ODA0ODIsImV4cCI6MTcyNjQ4MTM4MiwiYXVkIjoiQUNDRVNTX1RPS0VOIn0.icXN8s4b-sn6fnJS4OeA6u5p_FmbYeaGRYBz6ttl4_s"
}

repairs = get_csv(repairs_url, repairs_params, headers)
print(type(repairs))


# response = requests.get(url, params=params, headers=headers)

# if response.status_code == 200:
#     with open("CurlewRowingClubEquipmentRepairs.csv", "wb") as f:
#         f.write(response.content)   
#     print("File downloaded successfully.")
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)