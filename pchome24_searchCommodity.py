import requests, json, prettytable, os


url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results"

end_key = {"0", "離開", "exit", "EXIT", "Exit"}

# 印出搜尋結果的表格型式
table = prettytable.PrettyTable(["商品名稱", "價錢"], encoding="UTF-8")
table.align["商品名稱"] = "l"
table.align["價錢"] = "r"

while True:
    search_word = input("輸入搜尋關鍵字(0: 離開)：").strip()
    if search_word in end_key: # 關閉程式
        break
    page = "1"
    while page not in end_key:                        
        params = {"q":search_word, "page":page, "sort":"rnk/dc"}
        response = requests.get(url, params=params)
        data = json.loads(response.text)  # 找尋到的資料，型態：字典
        if not data["totalRows"]: # 判斷是否有找到相關產品，沒有找到則離開迴圈
            os.system("cls" if os.name == "nt" else "clear")
            print(f"找不到與「{search_word}」有關的產品！")
            break  
            
        table.clear_rows() # 清除上次搜尋頁數的資料
        for d in data["prods"]:  # 儲存搜尋頁數中的資料(在找不到關鍵字時會丟出：KeyError
            table.add_row([d["name"], d["price"]])
        
        circle = 1
        while True: # 印出找到的資料與輸入要前往的頁數
            os.system("cls" if os.name == "nt" else "clear") # 清除前面印出的東西
            print(f"「{search_word}」的搜尋結果：")
            print(table)
            if circle == 2: # 如果輸入的頁數超過搜尋到的最大頁數時的提醒
                circle = 1
                print("超出範圍！")
            in_page = input("前往頁數(0: 搜尋其他商品)：").strip()

            if in_page.isdigit() or in_page in end_key: # 判斷 page 輸入的是否數字或是否離開
                if int(in_page) > data["totalPage"]:            
                    circle = 2
                    continue
                page = in_page
                break 
        

