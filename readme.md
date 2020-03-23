# Python program that parse ad from site 'olx.ua' by search link
`Use for run:`

    - python v.3.8.1
    - selenium v.3.141.0
    - firefox v.74.0
    - geckodriver v0.26.0
 
 `Description:`
 
 1. Create new directory to this project and nev virtual environment on it:
 
    _python -m venv env_
  
 2. Run virtual environment:
  
    _env\Scripts\activate_
  
 3. Get project files from 'GitHub.com':
    
    _git clone https://github.com/rybaprm/OlxSelenium_ 
 
 4. Install all requirements:
 
    _pip install -r requirements.txt_
 
 5. Download Selenium WebDriver for Firefox:
 
    _https://github.com/mozilla/geckodriver/releases_
    
    in this project used geckodriver-v0.26.0-win64.zip
    
    _https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip_

 6. Unpack archive to directory with this project. The project directory should
consist of such elements:
    - 'directory of project':
        - 'env'                 - directory of virtual environment;
        - 'spider_olx.py'       - python file with class declared class 'OlxSpider' (search spider);
        - 'run_spider.py'       - python file in which call class 'OlxSpider' and some method of this class;
	- 'geckodriver.exe'	    - download and unpack WebDriver for Firefox.

6. For parse ad from site 'olx.ua' by search link run in terminal with
 activated virtual environment 'env' command:
    
    _python run_spider.py > olx_ad.txt_

7. After successful execution of the program we get file 'olx_ad.txt' with
 parsing result.
 
 
` Class description:`
 
 - Сlass 'OlxSpider()'  implements parsing ad of site 'olx.ua' and consist some
  method's:
'\_\_init__()', 'stop()', 'parse()', 'parse_pages()'.


    - method '\_\_init__()' - call's once, when create instants of class. Create hidden Firefox browser for parsing;
    - method 'stop()'  - stop work of browser;
    - method 'parse()' - parse ad elements on the page and return dictionary dictionary that consist elements: link, text, date, price of ad;
    - method 'parse_pages()' - parse all pages in pagination and print value of dictionary (consist elements of ad on the page), stop work of browser after parsing. 

