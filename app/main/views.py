from ..requests import get_headlines
from . import main
from flask import render_template,request,redirect,url_for

@main.route('/')
def index():
    '''
    View root page function that returns the index page
    '''
    business_news = get_headlines()
    print(business_news)
    title = 'Home- WElcme to News update'
    return render_template('index.html',business = business_news,title = title)
