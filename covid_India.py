import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.mygov.in/covid-19/"
html_page = requests.get(url).text
soup = BeautifulSoup(html_page, "html.parser")
table = soup.find("table", id="state-covid-data")
table_data = table.tbody.find_all("tr")
dicts = {}
for data in range(len(table_data)):
    key = table_data[data].find_all("td")[0].string
    values = [j.string for j in table_data[data].find_all('td')]
    dicts[key] = values
live_data = pd.DataFrame(dicts).drop(0).T
live_data.index.name = "States/ UTs"
live_data.columns = ["Confirmed", "Active", "Recovered", "Deceased"]
live_data.iloc[:, :].to_csv("covidIndia.csv")
print("done")
