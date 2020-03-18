from spider_olx import OlxSpider # import class OlxSpider from file spider_olx

# Declared variable - search link of the site olx.ua
START_URL = '''https://www.olx.ua/nedvizhimost/zaporozhe/?search%5B
filter_float_price%3Afrom%5D=23000&search%5B
filter_float_price%3Ato%5D=33000&search%5Bdistrict_id%5D
=51&currency=USD'''

# Make instance of class 'OlxSpider' with named argument 'start_url' and use
# method of class 'parse_pages()'
OlxSpider(start_url=START_URL).parse_pages()