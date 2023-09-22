import requests, prettytable
from bs4 import BeautifulSoup


# 中央氣象署
url = " https://www.cwb.gov.tw/V8/C/W/County_TempTop.html"
# 存取各縣市氣溫的位置
url_tem = "https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html"

hd = {"User-Agent":"Mozilla/5.0"}
table = prettytable.PrettyTable(["城市", "攝氏溫度 °C", "華氏溫度 °F"])

t = requests.get(url_tem, headers=hd) 
t_bs4 = BeautifulSoup(t.text, "html.parser")
t_data = t_bs4.find_all("tr")
for d in t_data:
    city = d.find("th").text
    tem_C = d.find("span", class_="tem-C").text
    tem_F = d.find("span", class_="tem-F").text
    table.add_row([city, tem_C, tem_F])
print(table)

