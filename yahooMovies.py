import requests
import pandas as pd
from bs4 import BeautifulSoup


def fetch_data(url):
    print("爬取：", url)
    r = requests.get(url)
    r_bs4 = BeautifulSoup(r.text, "html.parser")
    movies = r_bs4.find_all("div", class_="release_info")
    data_list = []
    for movie in movies:
        name = movie.find("div", class_="release_movie_name")
        name = name.a.text.strip()
        date = movie.find("div", class_="release_movie_time")
        date = date.text.strip().replace("上映日期：\n                ", "")
        level = movie.find("div", class_="leveltext")
        level = level.span.text
        satisfaction = movie.find("span", class_="count")
        satisfaction = satisfaction and satisfaction.get("data-num")
        data_list.append([name, date, level, satisfaction])
    
    next_page = r_bs4.find("li", class_="nexttxt")
    if next_page.a:
        next_url = next_page.a.get("href")
        data_list += fetch_data(next_url)

    return data_list


url = "https://movies.yahoo.com.tw/movie_intheaters.html"

Movie_datas = fetch_data(url)

df = pd.DataFrame(Movie_datas, columns=["電影名稱","上映時間", "期待值", "滿意度"])
df.to_excel("YahooMovie.xlsx", index=False, engine="openpyxl")