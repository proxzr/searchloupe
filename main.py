import webbrowser
import argparse

def cli():
    parse = argparse.ArgumentParser()

    parse.add_argument('search', nargs='+', help='search query')

    parse.add_argument('--google', action='store_true', help='use google')
    parse.add_argument('--bing', action='store_true', help='use bing')
    parse.add_argument('--yahoo', action='store_true', help='use yahoo')
    parse.add_argument('--duckduckgo', action='store_true', help='use duckduckgo')
    parse.add_argument('--yandex', action='store_true', help='use yandex')
    parse.add_argument('--baidu', action='store_true', help='use baidu')
    parse.add_argument('--ecosia', action='store_true', help='use ecosia')
    parse.add_argument('--qwant', action='store_true', help='use qwant')
    parse.add_argument('--twitter', action='store_true', help='use twitter')
    parse.add_argument('--facebook', action='store_true', help='use facebook')
    parse.add_argument('--tiktok', action='store_true', help='use tiktok')

    args = parse.parse_args()

    search_query = ' '.join(args.search)

    return args, search_query

def launcher_search_engine():
    args, search_query = cli()

    if args.google:
        webbrowser.open("https://www.google.com/search?q=" + search_query)

    if args.bing:
        webbrowser.open("https://www.bing.com/search?form=&q=" + search_query)

    if args.yahoo:
        webbrowser.open("https://search.yahoo.com/search?p=" + search_query + "&ei=UTF-8&fp=1")

    if args.duckduckgo:
        webbrowser.open("https://duckduckgo.com/?t=h_&q=" + search_query + "&ia=web")

    if args.yandex:
        webbrowser.open("https://yandex.com/search/?text=" + search_query + "&search_source=yacom_desktop_common")

    if args.baidu:
        webbrowser.open("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd=" + search_query + "&rn=&fenlei=256&rqlang=en")

    if args.ecosia:
        webbrowser.open("https://www.ecosia.org/search?method=index&q=" + search_query)

    if args.qwant:
        webbrowser.open("https://www.qwant.com/?l=enr&q=" + search_query + "&t=web")

    if args.twitter:
        webbrowser.open("https://twitter.com/search?q=" + search_query + "&src=typed_query&f=top")

    if args.facebook:
        webbrowser.open("https://www.facebook.com/search/top/?q=" + search_query)

    if args.tiktok:
        webbrowser.open("https://www.tiktok.com/search?q=" + search_query)

def print_boxed_text(text):
    max_length = max(len(line) for line in text)
    border = '┌' + '─' * (max_length + 2) + '┐'
    print(border)
    for line in text:
        print('│ ' + line + ' ' * (max_length - len(line)) + ' │')
    print('└' + '─' * (max_length + 2) + '┘')

def main(): 
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


    print("-" * 61)
    print()
    print_boxed_text(["Thanks for using my tool",
                      "Hoping it will be of great help to you"])
    print()
    print("-" * 61)



    launcher_search_engine()

if __name__ == "__main__":
    main()
