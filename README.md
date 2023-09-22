# 爬蟲練習紀錄
 
1. ptt_articleTitle
    - html
    - 爬取指定分類的 ptt 標題、人氣、時間
    - 並將資訊儲存在 .json 或 .xml 檔案中
2. ptt_article_savePicture
    - 取得指定 ptt 文章中的 jpg, png, jpeg, gif 圖檔
    - 並將其一在網頁上的名稱儲存在指定的資料夾中
3. pchome24_searchCommodity
    - json
    - 輸入商品名稱，並取的相關商品的標題與價格
    - 使用 prettytable 將每一頁的資訊用表格的方式呈現
    - 可以切換不同的頁數來取得更多商品資訊
    - 使用 os.system("cls" if os.name == "nt" else "clear") 將舊訊息刷掉，顯示新的資訊
4. cwa_tempTop
    - Ajax
    - 取的各縣市溫度
    - 使用 prettytable 套件將各縣市的名稱、華氏與攝氏已表格的方式成
5. Hahow_crawler
    - Ajax
    - 取得現有課程的名稱、評價、價格、購買人數
    - 並將資訊儲存在 .xml 檔案中
6. yahooMovies
    - html
    - 取得上映中的電影資訊
    - 分別為電影名稱、上映日期、期待值、滿意度
    - 遇到取下來的資訊有空格與換行，使用 strip() 解決即可