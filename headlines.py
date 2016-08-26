import feedparser

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {'eldiario': 'feed://www.eldiario.es/rss/',
			'publico': 'feed://www.publico.es/rss/',
			'ctxt': 'feed://ctxt.es/es/?tpl=87'}



@app.route("/")

def get_news():
	query = request.args.get("publication")
	if not query or query.lower() not in RSS_FEEDS:
		publication = "publico"
	else:
		publication = query.lower()
	
	feed = feedparser.parse(RSS_FEEDS[publication])
	return render_template("home.html", 
							articles=feed['entries'])

if __name__ == '__main__':
	app.run(port=5000, debug=True)