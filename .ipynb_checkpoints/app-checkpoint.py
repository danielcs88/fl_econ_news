import feedparser
from flask import Flask

app = Flask(__name__)
FEED_URL = "https://news.google.com/rss/search?q=%7Bflorida+economic%7D&hl=en-US&gl=US&ceid=US:en"

feed = feedparser.parse(FEED_URL)

type(feed["entries"][0:9])


@app.route("/")
def print_news():
    feed = feedparser.parse(FEED_URL)
    article = feed["entries"][0:9]  
    
    header = """<html>
        <body>
            <h1>Florida: Economic News</h1>"""
    
    footer = """</body>
        </html>"""
    
    
    body = ""
    
    for entry in article:
           
        template = """
            <b>{0}</b><br/>
            <p>{1}</p>
            <br/>
            <p>
        """.format(
            entry.get("title"), entry.get("description")
        )
        
        
        body += template
    
    html = header + body + footer

    return html

if __name__ == "__main__":
    app.run()
