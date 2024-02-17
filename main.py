import webbrowser, argparse, sys

def cli():
    parse = argparse.ArgumentParser()

    parse.add_argument(
        '--google',
        action='store_true',
        help='use google'
    )
    parse.add_argument(
        '--bing',
        action='store_true',
        help='use bing'
    )
    parse.add_argument(
        '--yahoo',
        action='store_true',
        help='use yahoo'
    )
    parse.add_argument(
        '--duckduckgo',
        action='store_true',
        help='use duckduckgo'
    )
    parse.add_argument(
        '--yandex',
        action='store_true',
        help='use yandex'
    )
    parse.add_argument(
        '--baidu',
        action='store_true',
        help='use baidu'
    )
    parse.add_argument(
        '--ecosia',
        action='store_true',
        help='use ecosia'
    )
    parse.add_argument(
        '--qwant',
        action='store_true',
        help='use qwant'
    )
    parse.add_argument(
        '--twitter',
        action='store_true',
        help='use twitter'
    )
    parse.add_argument(
        '--facebook',
        action='store_true',
        help='use facebook'
    )
    parse.add_argument(
        '--tiktok',
        action='store_true',
        help='use tiktok'
    )

    parse.add_argument('search')

    args = parse.parse_args()
    searchdot = args.search

    return args, searchdot

def launcher_search_engine():

    args, searchdot = cli()

    if len(sys.argv) == 2 and args.search:
        try:
            print("✔️ Search with all search engines")
            webbrowser.open("https://www.google.com/search?q=" + searchdot)
            webbrowser.open("https://www.bing.com/search?form=&q=" + searchdot)
            webbrowser.open("https://search.yahoo.com/search?p=" + searchdot + "&ei=UTF-8&fp=1")
            webbrowser.open("https://duckduckgo.com/?t=h_&q=" + searchdot + "&ia=web")
            webbrowser.open("https://yandex.com/search/?text=" + searchdot + "&search_source=yacom_desktop_common")
            webbrowser.open("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd=" + searchdot + "&rn=&fenlei=256&rqlang=en")
            webbrowser.open("https://www.ecosia.org/search?method=index&q=" + searchdot)
            webbrowser.open("https://www.qwant.com/?l=enr&q=" + searchdot + "&t=web")
            webbrowser.open("https://twitter.com/search?q=" + searchdot + "&src=typed_query&f=top")
            webbrowser.open("https://www.facebook.com/search/top/?q=" + searchdot)
            webbrowser.open("https://www.tiktok.com/search?q=" + searchdot)
        except:
            print("❌ Error on search with all search engines")


    if args.google:
        try:
            webbrowser.open("https://www.google.com/search?q=" + searchdot)
            print("✔️ Google")

        except Exception:
            print("❌ Google")


    if args.bing:
        try:
            webbrowser.open("https://www.bing.com/search?form=&q=" + searchdot)
            print("✔️ Bing")

        except Exception:
            print("❌ Bing")
    
    if args.yahoo:
        try:
            webbrowser.open("https://search.yahoo.com/search?p=" + searchdot + "&ei=UTF-8&fp=1")
            print("✔️ Yahoo")

        except Exception:
            print("❌ Yahoo")

    if args.duckduckgo:
        try:
            webbrowser.open("https://duckduckgo.com/?t=h_&q=" + searchdot + "&ia=web")
            print("✔️ Duckduckgo")

        except Exception:
            print("❌ Duckduckgo")

    if args.yandex:
        try:
            webbrowser.open("https://yandex.com/search/?text=" + searchdot + "&search_source=yacom_desktop_common")
            print("✔️ Yandex")

        except Exception:
            print("❌ Yandex")

    if args.baidu:
        try:
            webbrowser.open("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd=" + searchdot + "&rn=&fenlei=256&rqlang=en")
            print("✔️ Baidu")

        except Exception:
            print("❌ Baidu")

    if args.ecosia:
        try:
            webbrowser.open("https://www.ecosia.org/search?method=index&q=" + searchdot)
            print("✔️ Ecosia")

        except Exception:
            print("❌ Ecosia")

    if args.qwant:
        try:
            webbrowser.open("https://www.qwant.com/?l=enr&q=" + searchdot + "&t=web")
            print("✔️ Qwant")

        except Exception:
            print("❌ Qwant")
    
    if args.twitter:
        try:
            webbrowser.open("https://twitter.com/search?q=" + searchdot + "&src=typed_query&f=top")
            print("✔️ Twitter")

        except Exception:
            print("❌ Twitter")

    if args.facebook:
        try:
            webbrowser.open("https://www.facebook.com/search/top/?q=" + searchdot)
            print("✔️ Facebook")

        except Exception:
            print("❌ Facebook")

    if args.tiktok:
        try:
            webbrowser.open("https://www.tiktok.com/search?q=" + searchdot)
            print("✔️ Tiktok")
        
        except Exception:
            print("❌ Tiktok")


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

    launcher_search_engine()

if __name__ == "__main__":
    main()
