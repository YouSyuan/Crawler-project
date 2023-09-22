import requests
import pandas as pd

url = "https://hahow.in/group?filter=PUBLISHED"
url = "https://api.hahow.in/api/products/search?category=COURSE&filter=PUBLISHED&limit=24&page=0&sort=TRENDING"

headers = {"User-Agent":"Mozilla/5.0"}
r = requests.get(url, headers=headers)
datas_list = []
if r.status_code == 200:      
    data = r.json()
    products = data["data"]["courseData"]["products"]
    for product in products:
        course_data = {
            "課程名稱":product["title"],
            "評價":product["averageRating"],
            "價格":product["price"],
            "購買人數":product["numSoldTickets"],
        }
        datas_list.append(course_data)
    df = pd.DataFrame(datas_list)
    df.to_excel("Hahow_course.xlsx", index=False, engine="openpyxl")
else:
    print("=== 網址錯誤 ===")