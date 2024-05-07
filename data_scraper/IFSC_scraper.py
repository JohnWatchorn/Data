import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://www.ifsc-climbing.org/athlete/11490/toby-roberts"
# GET PAGE URL

response = requests.get(url)

# my arrays and dictionary
date_array = []
result_array = []
raw_output = []
rankings = []

# if page is up GO
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')  # parses
    table = soup.find('div', 'flex flex-row gap-6 w-full').find_all('table', 'w-full overflow-hidden text-left')
    for rank in table:
        comp = rank.find('tbody').find_all('td',
                                           'py-2 first:pl-6 px-2 last:pr-6 py-2 whitespace-nowrap text-black d3-ty-body-small uppercase')
        for placement in comp:
            found_data = placement.find('span')
            found_string_data = found_data.string
            raw_output.append(found_string_data)

for i, item in enumerate(raw_output):
    if i % 2 == 0:
        date_array.append(item)
    else:
        result_array.append(item)

date_array, result_array = zip(rankings)
    #rankings.append((date, result))


print(rankings)
print(date_array)
print(result_array)

plt.plot(date_array, result_array, marker='o', linestyle='-')

plt.xlabel('Date of Competition')
plt.ylabel('Placement')
plt.title('Toby Roberts IFSC')
plt.xticks(rotation=45)


plt.show()
