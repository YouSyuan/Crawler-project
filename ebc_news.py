import requests
from bs4 import BeautifulSoup


url = "https://news.ebc.net.tw/realtime"

hd = {"User-Agent":"Mozilla/5.0"}
n = 1

for page in range(1,3):
    pr = {"page":page}
    response = requests.get(url, headers=hd, params=pr)  
    d_html = response.text
    d_bs4 = BeautifulSoup(d_html, "html.parser")
    d_title = d_bs4.find_all("div", class_="style1 white-box")
    for d in d_title:
        if d.find("span", class_="title"):
            cf = d.find("div", class_="news-category").text
            d_time = d.find("span", class_="small-gray-text").text
            title = d.find("span", class_="title").text
            print(cf+"：", d_time)
            print(title)
            c_url = url2 + d.find("a").attrs["href"]
            c_response = requests.get(c_url, headers=hd)
            c_html = c_response.text
            c_bs4 = BeautifulSoup(c_html, "html.parser")
            c_text = c_bs4.find("content-ad").find_all("p")
            content = ""
            n_img = 1
            for c in c_text:
                if c.find("img"):
                    img_response = requests.get(c.find("img").attrs["src"], hd)
                    with open(f"new{n}-{n_img}.jpg", "wb") as f:
                        f.write(img_response.content)
                else:
                    content += c.text + "\r\n"
            with open(f"news{n}.text", "w", encoding = "UTF-8") as f:
                f.write(cf+"：" + d_time + "\r\n")
                f.write(title + "\r\n")
                f.write(c_url + "\r\n")
                f.write("======================================================================" + "\n")
                f.write(content)
            n += 1
            print("================================================================================================")
            # break