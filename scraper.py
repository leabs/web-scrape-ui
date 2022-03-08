import requests
from bs4 import BeautifulSoup



class Webpage:
    def __init__(self, url):
        self.url = url
        self.html = self.get_page_html()
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def get_page_html(self):
        page = requests.get(self.url)

        # print('Request status code:', page.status_code)

        if page.status_code == 200:
            return page.text
        return

    # HEAD TAG
    def get_head_tag(self):
        # decode_contents() will convert the bytes format to python strings
        return [self.soup.find('head').decode_contents()]

    # SPECIFIC CLASS
    def get_content_by_class(self, class_name):
        eles = self.soup.find_all(class_=class_name)
        return [ele.decode_contents() for ele in eles]

    # SPECIFIC ID
    def get_content_by_id(self, id_name):
        eles = [self.soup.find(id=id_name)]
        return [ele.decode_contents() for ele in eles]

    # IMAGES
    def get_all_images(self):
        eles = self.soup.find_all('img')
        return [str(ele) for ele in eles]

    # ALL CONTENTS
    def get_all_contents(self):
        return [self.soup.find('body').decode_contents()]



if __name__ == '__main__':
    sample_url = 'https://en.wikipedia.org/wiki/Mahatma_Gandhi'

    a = Webpage(sample_url)

    # print(a.get_head_tag())
    # print(type(a.get_head_tag()[0]))

    # print(a.get_all_contents())
    # print(type(a.get_all_contents()[0]))

    # print(a.get_content_by_class('reference'))
    # print(type(a.get_content_by_class('reference')[0]))

    # print(a.get_content_by_id('siteNotice'))
    # print(type(a.get_content_by_id('siteNotice')[0]))

    # print(str(a.get_all_images()[0]))
    # print(type(a.get_all_images()[0]))