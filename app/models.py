class Source:
    """
    Source class to define souce objects
    """
    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url

class Article:
    """"
    Article class to define article objects
    """
    def __init__ (self,image, title,author,description,publishedAt,url):
        self.image = image
        self.title = title
        self.author = author
        self.description = description
        self.publishedAt = publishedAt
        self.url = url
