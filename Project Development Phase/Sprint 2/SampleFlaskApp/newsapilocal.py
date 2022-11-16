from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='cdce6d49832f42e9b3cd2d296424a2a0')

# /v2/top-headlines

def getheadlines():
    top_headlines = newsapi.get_top_headlines(country="us")
    print(top_headlines)
    return top_headlines 