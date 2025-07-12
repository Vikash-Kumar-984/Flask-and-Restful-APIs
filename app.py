from flask import Flask,jsonify
import requests

API_KEY="ab6d708b5b4142cba5f61839b74b9e3b"
url="https://newsapi.org/v2/everything?q=tesla&from=2025-06-12&sortBy=publishedAt&apiKey=ab6d708b5b4142cba5f61839b74b9e3b"

app=Flask(__name__)


@app.route('/api/news',methods=['GET'])
def get_news():
    response = requests.get(url)
    if response.status_code==200:
        news_data = response.json()
        total_articles = len(news_data['articles'])
        first_article = news_data['articles'][0]
        author = first_article['author']
        title=first_article['title']
        publishedAt = first_article['publishedAt']

        output_data={"Total Article Counts":total_articles,
                    "Title":title,
                    "Author":author,
                    "Published Date":publishedAt}
        return jsonify(output_data)
    
    else:
        return jsonify({"msg":"Invalid API Key"})


if __name__=='__main__':
    app.run(debug=True)