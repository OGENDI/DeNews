class Sources:
    '''
    Defines the news sources objects 
    '''
    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url

class Article:
    '''
    Instantiating news objects
    '''
    def __init__(self,id,image,title,author,description,time,url):
        self.id = id
        self.image = image
        self.title = title
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        