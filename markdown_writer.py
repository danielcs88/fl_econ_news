import feedparser

FEED_URL = "https://news.google.com/rss/search?q=%7Bflorida+economic%7D&hl=en-US&gl=US&ceid=US:en"

feed = feedparser.parse(FEED_URL)

feed.keys()

feed["entries"][0].published[:25]


def print_news():
    feed = feedparser.parse(FEED_URL)
    article = feed["entries"][0:10]

    header = """# Florida: Latest Economic News \n"""

    body = ""

    for entry in article:

        template = """## [{0}]({1}) -> {2} \n""".format(
            entry.get("title"), entry.get("link"), entry.get("published")[:25]
        )

        body += template

    md = header + body

    return md


with open("README.md", "w") as file:
    site = print_news()
    print(site, sep="\n", file=file)
