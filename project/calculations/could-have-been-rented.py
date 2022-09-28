import json
from datetime import datetime, timedelta
file_name_1st = "sep3.json"

file_name_2nd = "sep11.json"
file2_collection_day = 11
file2_collection_month = 9
file2_collection_year = 2022
# second file collection data minus 30 days ( original 2022-09-11)
date2_minus_30 = datetime(file2_collection_year, file2_collection_month, file2_collection_day) - timedelta(30)

possible_counter = 0
links = []
unrented_counter = 0

with open(file_name_1st, "r") as f:
    result_file_1 = json.load(f)

for listing in result_file_1:
    file1_year, file1_month, file1_day = listing["publish_date"].split("-")
    date1 = datetime(int(file1_year), int(file1_month), int(file1_day))
    if date1 >= date2_minus_30:
        possible_counter += 1
        links.append(listing["link"])

with open(file_name_2nd, "r") as f:
    result_file_2 = json.load(f)

for listing in result_file_2:
    for link in links:
        if link == listing["link"]:
            unrented_counter += 1


def get_percentage(num1, num2):
    return f"{round((num1 / num2) * 100, 2)}%"

rented = possible_counter - unrented_counter

print(f"Could have been rented: {possible_counter}")
print(f"Haven't been rented: {unrented_counter}, {get_percentage(unrented_counter, possible_counter)}")
print(f"Successfully rented: {rented}, {get_percentage(rented, possible_counter)}")





