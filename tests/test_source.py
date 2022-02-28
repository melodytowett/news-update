import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    test class behaviour for source class
    '''
    def setUp(self):
        '''
        set up method that will run before evey test
        '''
        self.new_source = Source('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))



