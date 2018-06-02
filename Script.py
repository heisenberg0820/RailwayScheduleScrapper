from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

train_no = input("Enter the train number : ")
rail_page = "https://www.cleartrip.com/trains/"+train_no

page = urlopen(rail_page)
soup = BeautifulSoup(page, "html.parser")
table_box = soup.find("table", attrs={"class": "results"})

file_name = train_no+".csv"
with open(file_name, "a") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["No", "Station", "Arrival", "Departure", "StopTime", "Distance", "Day", "Route"])
i = 1
lim = 0

for row in table_box.findAll("tbody"):
    for y in row.findAll("tr"):
        lim+=1

for row in table_box.findAll("tbody"):
    for x in row.findAll("tr"):
        col = x.findAll("td")
        no = col[0].string.strip()
        stn = col[1].find("a")
        stnname = stn.string.strip()
        arObj = col[2]
        arr = ""
        if(i==1):
            arrSt = arObj.find("strong")
            arr = arrSt.string.strip()
        else:
            arr = arObj.string.strip()
        depObj = col[3]
        dep = ""
        if (i == lim):
            depSt = depObj.find("strong")
            dep = depSt.string.strip()
        else:
            dep = depObj.string.strip()
        stoptime = col[4].string.strip()
        distance = col[5].string.strip()
        day = col[6].string.strip()
        route = col[7].string.strip()
        i+=1
        with open(file_name,"a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([no,stnname,arr,dep,stoptime,distance,day,route])




