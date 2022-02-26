import urllib.request,json

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
    get_headlines_url = headline_url.format(api_key)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)
        headlines_results = None
        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_headlines_results(headlines_results_list)

        return headlines_results

def process_headlines_results(headline_list):
    '''
    funtion to process headlines results
    '''
    headlines_results = []
    for headline_item in headline_list:
        image = headline_item.get('urlToImage')
        title = headline_item.get('title')
        author = headline_item.get('author')
        description = headline_item.get('description')
        time = headline_item.get('publishedAt')
        url = headline_item.get('url')

        if image:
            headline_object = Article(image,title,author,description,time,url)
            headlines_results.append(headline_object)

    return headlines_results



def get_category(category):
    '''
    Fuction that gets the json respone to the url request
    '''
    get_category_url = category_url.format(category,api_key)
    with urllib.request.urlopen(get_category_url)as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)

        category_results = None

        if get_category_response['results']:
            category_results_list = get_category_response['results']
            category_results = process_headlines_results(category_results_list)

    return category_results

