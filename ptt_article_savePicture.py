import requests, os
from bs4 import BeautifulSoup


def download_img(url, save_path):
    """ 下載圖片 """
    r = requests.get(url)
    with open(save_path, "wb") as f:
        print("正在下載圖片:", url)
        f.write(r.content)


url = "https://www.ptt.cc/bbs/Beauty/M.1695373984.A.1F3.html"

headers = {"Cookie":"over18=1"}
allow_pf = {"jpg", "png", "jpeg", "gif"}
r = requests.get(url, headers=headers)
if r.status_code == 200:      
    # 解析網頁
    r_bs4 = BeautifulSoup(r.text, "html.parser")  # 使用 html 的解析器
    title = r_bs4.find_all("span", class_="article-meta-value")[2].text

    # 建立儲存圖片的資料夾
    os.makedirs(f"Download/{title}", exist_ok=True)  

    # 找到網頁中所有的圖片
    links = r_bs4.find_all("a")  # 網頁中所有的連結
    for link in links:
        href = link.get("href")
        file_format = href.split(".")[-1].lower()
        if file_format in allow_pf:
            file_name = href.split("/")[-1]
            download_img(href, f"Download/{title}/{file_name}")
    print("下載完成")

else:
    print("=== 網址錯誤 ===")