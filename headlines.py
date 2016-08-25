import feedparser

from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {'eldiario': 'feed://www.eldiario.es/rss/',
			'publico': 'feed://www.publico.es/rss/',
			'ctxt': 'feed://ctxt.es/es/?tpl=87'}



@app.route("/")
@app.route("/<publication>")



def get_news(publication="ctxt"):

	feed = feedparser.parse(RSS_FEEDS[publication])
	first_article = feed['entries'][0]
	return """<html>
		<body>
			<h1> Titulares </h1>
			<b>{0}</b> <br/>
			<i>{1}</i> <br/>
			<p>{2}</p> <br/>
		</body>
		</html>""".format(first_article.get("title"), first_article.get("published"),first_article.get("summary"))

if __name__ == '__main__':
	app.run(port=5000, debug=True)