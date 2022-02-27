from ..requests import get_headlines,get_category,get_source,get_source_articles
from . import main
from flask import render_template,request,redirect,url_for

@main.route('/')
def index():
    '''
    View root page function that returns the index page
    '''
    headlines = get_headlines()
    # categories = get_category("sources")
    # sources = get_source()
    return render_template('index.html',headlines= headlines)

@main.route('/categories/<category>')
def category(category):
    '''
    method to render category page
    '''
    category = get_category(category)
    sources = get_source()
    return render_template('category.html', category = category,sources=sources)

@main.route('/article/<id>')
def article(id):
    article = get_source_articles(id)
    sources = get_source()
    category = get_category('health')
    return render_template('article.html',article = article,sources = sources, category = category)
@main.route('/search/<topic_name>')
def search(topic_name):
    ''' 
    Function to display search results
    '''
