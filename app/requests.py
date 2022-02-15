import json, urllib.request
from .models import Sources, Article

api_key = None
base_url = None
category = None

def config_request(app):
    global api_key, base_url, category
    api_key = app.config['API_KEY']
    base_url = app.config['NEWS_API_URL']

def get_source(news):
    source_url = base_url.format(news,api_key)
    with urllib.request.urlopen(source_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)
        sources_result = None
        if sources_response['sources']:
            sources_list = sources_response['sources']
            sources_result = process_sources_result(sources_list)
    return sources_result

def process_sources_result(list_source):
    sources_result = []
    for item in list_source:
        id = item.get('id')
        name = item.get('name')
        description = item.get('description')
        url = item.get('url')
        if id:
            source_object = Sources(id,name,description,url)
            sources_result.append(source_object)

    return sources_result

def get_articles(id):
    article_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(article_url)
    with urllib.request.urlopen(article_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)
        articles_result = None
        if articles_response['articles']:
            articles_list = articles_response['articles']
            articles_result = process_articles_result(articles_list)

    return articles_result

def process_articles_result(list_article):
    article_result = []
    for item in list_article:
        id = item.get('article_id')
        image = item.get('urlToImage')
        title = item.get('title')
        author = item.get('author')
        description = item.get('description')
        time = item.get('publishedAt')
        url = item.get('url')
        if id:
            article_object = Article(id, image, title, author, description, time, url)
            article_result.append(article_object)
    return article_result

def get_headlines():
    '''
    function that gets the response to the category json
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(
        api_key)
    print(get_headlines_url)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if headlines_response['articles']:
            get_headlines_list = headlines_response['articles']
            headlines_results = process_articles_result(get_headlines_list)

    return headlines_results

def article_source(article_id):
    ''' function to get artcles '''
    # art is use to refert o article
    art_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(
        article_id, api_key)
    print(art_source_url)
    with urllib.request.urlopen(art_source_url) as url:
        art_source_data = url.read()
        art_source_response = json.loads(art_source_data)
        art_source_results = None
        if art_source_response['articles']:
            art_source_list = art_source_response['articles']
            art_source_results = process_articles_result(art_source_list)

    return art_source_results

def get_category(category):
    category_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(category,api_key)
    with urllib.request.urlopen(category_url) as url:
        category_data = url.read()
        category_response = json.loads(category_data)
        category_result = None
        if category_response['articles']:
            category_list = category_response['articles']
            category_result = process_articles_result(category_list)
    
    return category_result
        
