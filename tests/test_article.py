import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    test class to the the article behaviour
    '''
    def setUp(self):
        self.new_article = Article('https://i.insider.com/6219c972101faf0019294d55?width=1200&format=jpeg',
                                   'How to get Siri to read text aloud on your iPhone, iPad, or Mac computer',
                                   'insider@insider.com (Dave Johnson)','You can invoke Siri on your iPhone, iPad, or Mac computer to read almost any text thats on the screen aloud.',
                                   '2022-02-26T06:40:13Z','https://www.businessinsider.com/how-to-get-siri-to-read-text')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

