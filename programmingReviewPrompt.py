import requests
import csv

from requests.api import head

url = "https://datausa.io/api/data?drilldowns=State&measures=Population"


headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url,headers=headers,data={})
myjson = response.json()
ourdata =[]
csvheader = ['ID STATE', 'STATE', 'ID YEAR', 'YEAR', 'POPULATION', 'SLUG STATE']

for x in myjson['data']:
    listing =[x['ID State'],x['State'],x['ID Year'],x['Year'],x['Population'],x['Slug State']]
    ourdata.append(listing)

with open('data.csv','w',encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    
    writer.writerow(csvheader)
    writer.writerows(ourdata)


print(ourdata)