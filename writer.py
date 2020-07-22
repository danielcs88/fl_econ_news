import feedparser

FEED_URL = "https://news.google.com/rss/search?q=%7Bflorida+economic%7D&hl=en-US&gl=US&ceid=US:en"


def print_news():
    feed = feedparser.parse(FEED_URL)
    article = feed["entries"][0:10]

    header = """<html>
        <body>
            <h1>Florida: Economic News</h1>"""

    footer = """</body>
        </html>"""

    body = ""

    for entry in article:

        template = """
            <b>{0}</b><br/>
            <p>{1} -> {2}</p>
            <br/>
            <p>
        """.format(
            entry.get("title"), entry.get("description"), entry.get("published")[:25]
        )

        body += template

    html = header + body + footer

    return html


with open("../danielcs88.github.io/cues/econ_news.html", "w") as file:
    site = print_news()
    print(site, sep="\n", file=file)
