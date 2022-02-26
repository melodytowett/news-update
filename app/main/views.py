from app.models import Source
from ..requests import get_headlines,get_category,get_source
from . import main
from flask import render_template,request,redirect,url_for

@main.route('/')
def index():
    '''
    View root page function that returns the index page
    '''
    headlines = get_headlines()
    # categories = get_category()
    sources = get_source()
    title = 'Home- Welcome to News update'
    return render_template('index.html',headlines= headlines,title=title,sources=sources)

@main.route('/categories/<category>')
def category():
    '''
    method to render category page
    '''
    category = get_category()
    sources = get_source()
    return render_template('index.html', category = category,sources=sources)