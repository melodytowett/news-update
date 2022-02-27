import urllib.request,json
from flask.templating import render_template
from .models import Article,Source

api_key = None
category_url = None
source_url = None
headline_url = None

def configure_request(app):
    '''
    Fuctiona to configure request
    '''
    global api_key,category_url,source_url,headline_url
    api_key = app.config['NEWS_API_KEY']
    category_url = app.config['CATEGORY_URL']
    source_url = app.config['SOURCE_URL']
    headline_url = app.config['HEADLINE_URL']


def get_headlines():
    '''
    funtcion that gets response from json url request
    '''
    get_headline_url = headline_url.format(api_key)
    with urllib.request.urlopen(get_headline_url) as url:
        get_headline_data = url.read()
        get_headline_response = json.loads(get_headline_data)
        headline_results = None
        if get_headline_response['articles']:
            headline_results_list = get_headline_response['articles']
            headline_results = process_headlines_results(headline_results_list)

        return headline_results

def process_headlines_results(headline_list):
    '''
    funtion to process headlines results
    '''
    headline_results = []
    for headline_item in headline_list:
        image = headline_item.get('urlToImage')
        title = headline_item.get('title')
        author = headline_item.get('author')
        description = headline_item.get('description')
        time = headline_item.get('publishedAt')
        url = headline_item.get('url')

        if image:
            if description:
                if time:
                  headline_object = Article(image,title,author,description,time,url)
                  headline_results.append(headline_object)

    return headline_results

def get_category(category):
    '''
    Fuction that gets the json respone to the url request
    '''
    get_category_url = category_url.format(category,api_key)
    with urllib.request.urlopen(get_category_url)as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)

        category_results = None

        if get_category_response['sources']:
            category_results_list = get_category_response['sources']
            category_results = process_headlines_results(category_results_list)

    return category_results

def get_source():
    '''
    Function that gets json response
    '''
    get_source_url = source_url.format(api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_article_data = url.read()
        get_source_article_respone = json.loads(get_source_article_data)

        source_article_results = None
        
        if get_source_article_respone['sources']:
            source_results_list = get_source_article_respone['sources']
            source_article_results = process_source_results(source_results_list)

    return source_article_results

def process_source_results(source_list):
    '''
    funtion tha processes the source results
    '''

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        url = source_item.get('url')
        description = source_item.get('description')

        if id:
            source_object = Source(id,name,url,description)
            source_results.append(source_object)

    return source_results

def get_source_articles(id):
    get_source_article_url = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'.format(id,api_key)
    with urllib.request.urlopen(get_source_article_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_articles = None
        if get_source_response:
            source_results_list = get_source_response
            source_articles = process_source_article_results(source_results_list)

    return source_articles

def process_source_article_results(article_list):
    '''
    funtion to process source articles
    '''
    article_results = []
    for article_item in article_list:
        image = article_item.get('urlToImage')
        title = article_item.get('title')
        author = article_item.get('author')
        description = article_item.get('description')
        time = article_item.get('publishedAt')
        url = article_item.get('url')

        if title:
            if description:
                if image:
                    if author:

                        article_object = Article(image,title,author,description,time,url)
                        article_results.append(article_object)

    return article_results

def search_topic(topic_name):
    '''
    funtion to search  from json
    '''
    search_topic_url = ' https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'.format(api_key,topic_name)
    with urllib.request.urlopen(search_topic_url) as url:
        search_topic_data = url.read()
        search_topic_response = json.loads(search_topic_data)

        topic_results = None
        if search_topic_response['articles']:
            search_topic_list = search_topic_response['articles']
            topic_results = process_headlines_results(search_topic_list)
        return topic_results

        
  