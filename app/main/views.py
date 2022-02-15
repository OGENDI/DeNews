from flask import render_template,request
from . import root
from ..requests import get_headlines, get_source,article_source, get_category

@root.route('/')
def index():
    ''' view root page function that returns index page data'''
    
    # Get headlines
    mysources = get_source()
    headlines = get_headlines()
    print(mysources)
    title ='News Updates'
    return render_template('index.html', mysources=mysources, title =title,headlines=headlines)

@root.route('/article/<int:aritcle_id>')
def article(id):
    ''' function for an article to return a page details'''
    articles = article_source(id)
    return render_template('articles.html',articles=articles, id=id)
        
@root.route('/categories/<category_name>')
def news_category(category_name):
    ''' function and route returning the news categories in cartegories page '''
    category = get_category(category_name)
    category_title = f'{category_name}'  
    return render_template('categories.html', title= category_title, category=category)