from ..requests import get_headlines
from . import main
from flask import render_template,request,redirect,url_for

@main.route('/')
def index():
    '''
    View root page function that returns the index page
    '''
    source_news = get_headlines("source")
    print(source_news)
    title = 'Home- WElcme to News update'
    return render_template('index.html',source = source_news,title = title)