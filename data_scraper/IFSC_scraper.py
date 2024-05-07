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
    # Find table with all the data in it
    table = soup.find('div', 'flex flex-row gap-6 w-full').find_all('table', 'w-full overflow-hidden text-left')

    # iterate over table to refine search
    for rank in table:
        comp = rank.find('tbody').find_all('td', 'py-2 first:pl-6 px-2 last:pr-6 py-2 whitespace-nowrap text-black d3-ty-body-small uppercase')
        # same same
        for placement in comp:

            # finally found the date
            found_data = placement.find('span')

            # make data cleaner b.string return text from tag
            found_string_data = found_data.string
            # put it in array
            raw_output.append(found_string_data)


# separate array from date and placement
for i, item in enumerate(raw_output):
    if i % 2 == 0:
        date_array.append(item)
    else:
        # y-axis need to be int
        result_array.append(int(item))


print(date_array)
print(result_array)

plt.plot(date_array, result_array, marker='o', linestyle='-')

plt.xlabel('Date of Competition')
plt.ylabel('Placement')
plt.title('Toby Roberts IFSC')
plt.xticks(rotation=45)


plt.show()
