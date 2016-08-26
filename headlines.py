import feedparser

from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {'eldiario': 'feed://www.eldiario.es/rss/',
			'publico': 'feed://www.publico.es/rss/',
			'ctxt': 'feed://ctxt.es/es/?tpl=87'}



@app.route("/")
@app.route("/<publication>")



def get_news(publication="ctxt"):

	feed = feedparser.parse(RSS_FEEDS[publication])
	first_article = feed['entries'][0]
	return render_template("home.html", articles=feed['entries'])

if __name__ == '__main__':
	app.run(port=5000, debug=True)