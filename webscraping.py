url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"

from bs4 import BeautifulSoup
import requests
import pandas as pd

mydata = requests.get(url).text

soup = BeautifulSoup(mydata, "html5lib")

table = soup.find('table')
# print(table)
language = []
salary = []

for row in table.find_all('tr'):  # iterating through rows
    cols = row.find_all('td') # all columns in a specific row
    language_name = cols[1].getText()
    language.append(language_name)
    created_by = cols[2].getText()
    annual_avg_salary = cols[3].getText().replace('$','').replace(',','')
    salary.append(annual_avg_salary)
    learning_diff = cols[4].getText()
    print(f"Language: {language_name},   Annual Average Salary [$]: {annual_avg_salary}")



my_language_dict = {"Language":language, "Salary [$]": salary}
df = pd.DataFrame(my_language_dict)
df = df.iloc[1:,:]
df.sort_values(by = ['Salary [$]'])

print(df)
df.to_csv('popular-languages.csv')