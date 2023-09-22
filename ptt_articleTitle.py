import requests, json
import pandas as pd
from bs4 import BeautifulSoup


# ptt 網址
url = "https://www.ptt.cc/bbs/iOS/index.html"
# url = "https://www.ptt.cc/bbs/Beauty/index.html"
# 要爬取的頁數
pages = 3
# 儲存檔案名
file_name = "ptt_test"
# 檔案格式
file_format = "xml"
save = "F"

headers = {"Cookie":"over18=1"}
datas_list = []  # 用來儲存要存成檔案所爬取到的資料
for page in range(1, pages+1):
    print(f"第 {page} 頁 ==========")
    r = requests.get(url, headers=headers)

    # 判斷網址是否正確取得資訊
    if r.status_code == 200:      
        # 解析網頁
        r_bs4 = BeautifulSoup(r.text, "html.parser")  # 使用 html 的解析器
        # 取得指定的全部標籤(返回列表)
        r_datas = r_bs4.find_all("div", class_="r-ent")

        for data in r_datas:
            data_dic = {}
            title = data.find("div", class_="title")
            # 判斷標題是否被刪除
            if title.a:
                popular = data.find("div", class_="nrec").text
                date = data.find("div", class_="date").text
                title = title.text.strip()
                if not popular:
                    popular = "0"
                print(date, popular.ljust(2), title)

                data_dic["title"] = title
                data_dic["popular"] = popular
                data_dic["date"] = date
                datas_list.append(data_dic)
            else:
                print("文章已被刪除")

        # 進入上一頁
        last_url = r_bs4.find('a', class_='btn wide', string='‹ 上頁')["href"]
        url = "https://www.ptt.cc" + last_url
    else:
        print("=== 網址錯誤 ===")
        break

# 儲存檔案
if datas_list and save=="T":
    if file_format == "json":
        with open(f"{file_name}.json", "w", encoding="utf-8") as f:
            json.dump(datas_list, f, ensure_ascii=False, indent=4)
    elif file_format == "xml":
        df = pd.DataFrame(datas_list)
        df.to_excel(f"{file_name}.xlsx", index=False, engine="openpyxl")
    print("儲存成功")