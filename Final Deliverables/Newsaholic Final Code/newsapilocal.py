from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='cdce6d49832f42e9b3cd2d296424a2a0')

# /v2/top-headlines

def getheadlines():
    top_headlines = newsapi.get_top_headlines(country="us")
    print(top_headlines)
    return top_headlines 

def getbusinessheadlines():
    business_headlines = newsapi.get_top_headlines(category="business")
    return business_headlines

def getsportsheadlines():
    sports_headlines = newsapi.get_top_headlines(category="sports")
    return sports_headlines

def getentertainmentheadlines():
    entertainment_headlines = newsapi.get_top_headlines(category="entertainment")
    return entertainment_headlines

def gettechheadlines():
    tech_news = newsapi.get_top_headlines(category="technology")
    return tech_news

def gethealthheadlines():
    health_news = newsapi.get_top_headlines(category="health")
    return health_news    