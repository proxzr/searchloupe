import webbrowser
                   
print("""
┌─────────────────────────────────────────────────────────────┐
│ ____                      _     _                           │
│/ ___|  ___  __ _ _ __ ___| |__ | |    ___  _   _ _ __   ___ │
│\___ \ / _ \/ _` | '__/ __| '_ \| |   / _ \| | | | '_ \ / _ \│
│ ___) |  __/ (_| | | | (__| | | | |__| (_) | |_| | |_) |  __/│
│|____/ \___|\__,_|_|  \___|_| |_|_____\___/ \__,_| .__/ \___|│
│                                                 |_|         │
└─────────────────────────────────────────────────────────────┘
Made by Prox --- https://twitter.com/OsintTheWorld
""")

searchdot = input("👋🏻 What is your search today ? : ")

while not searchdot:
    print("🤖 : You forgot to write something. Please do a search !")
    searchdot = input("👋🏻 What is your search today ? : ")

webbrowser.open("https://www.google.com/search?q=" + searchdot +"&sca_esv=586707143&source=hp&ei=zOdoZci8IKKrkdUPzqCXyAg&iflsig=AO6bgOgAAAAAZWj13BSrYg41mAM-nxwxHFJTRco1YQZ7&ved=0ahUKEwjI0uLXv-yCAxWiVaQEHU7QBYkQ4dUDCAo&uact=5&oq=test&gs_lp=Egdnd3Mtd2l6IgR0ZXN0MhAQABgDGI8BGOUCGOoCGIwDMhAQLhgDGI8BGOUCGOoCGIwDMhAQABgDGI8BGOUCGOoCGIwDMhAQABgDGI8BGOUCGOoCGIwDMhAQABgDGI8BGOUCGOoCGIwDMhAQABgDGI8BGOUCGOoCGIwDMhAQLhgDGI8BGOUCGOoCGIwDMhAQABgDGI8BGOUCGOoCGIwDMhAQABgDGI8BGOUCGOoCGIwDMhAQABgDGI8BGOUCGOoCGIwDSJAJUIcFWOMGcAF4AJABAJgBAKABAKoBALgBA8gBAPgBAagCCg&sclient=gws-wiz")

webbrowser.open("https://www.bing.com/search?form=&q=" + searchdot + "&form=QBLH&sp=-1&lq=1&pq=&sc=0-0&qs=n&sk=&cvid=74B6895DB48342D3B8892A5AFE5C5881&ghsh=0&ghacc=0&ghpl=")

webbrowser.open("https://search.yahoo.com/search?p=" + searchdot + "&fr=yfp-t&fr2=p%3Afp%2Cm%3Asb&ei=UTF-8&fp=1")

webbrowser.open("https://duckduckgo.com/?t=h_&q=" + searchdot + "&ia=web")

webbrowser.open("https://yandex.com/search/?text=" + searchdot + "&lr=21081&search_source=yacom_desktop_common")

webbrowser.open("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd=" + searchdot + "&rn=&fenlei=256&oq=&rsv_pq=0x8f99c62900020204&rsv_t=dd74Oy0Y3JEDSDl8GFz3pNCzyve%2B2z7C1BdKNCH%2BiyWtsQ6oncphqvblpuVh&rqlang=en")

webbrowser.open("https://www.ecosia.org/search?method=index&q=" + searchdot)

webbrowser.open("https://www.qwant.com/?l=enr&q=" + searchdot + "&t=web")

webbrowser.open("https://twitter.com/search?q=" + searchdot + "&src=typed_query&f=top")

webbrowser.open("https://www.facebook.com/search/top/?q=" + searchdot)

webbrowser.open("https://www.tiktok.com/search?q=" + searchdot)





