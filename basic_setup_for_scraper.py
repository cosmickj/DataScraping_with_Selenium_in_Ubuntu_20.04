# <-------------------------module settings------------------------->
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

from fake_useragent import UserAgent
from configparser import ConfigParser

from bs4 import BeautifulSoup
import requests

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# <-------------------------connect database------------------------->
config = ConfigParser()
config.read('config.ini')

HOSTNAME = config['section-name']['HOSTNAME']
PORT     = int(config['section-name']['PORT'])
USERNAME = config['section-name']['USERNAME']
PASSWORD = config['section-name']['PASSWORD']
DATABASE = config['section-name']['DATABASE']
CHARSET1 = config['section-name']['CHARSET1']
CHARSET2 = config['section-name']['CHARSET2']

def checkSidoUpdated():
    dbcon = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET1)
    cursor = dbcon.cursor()
    sql = f"SELECT * FROM {table}"
    cursor.execute(sql)
    result = cursor.fetchone()
    ...

def upload(table):
    con_str = f"mysql+mysqldb://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset={CHARSET1}"
    engine = create_engine(con_str, encoding =CHARSET2)
    conn = engine.connect()
    table.to_sql(name='table-name', con=conn, if_exists='append',index=False)
    ...

# <-------------------------selenium settings------------------------->
ua = UserAgent()
userAgent = ua.random
headers = {'User-Agent':userAgent}

display = Display(visible=0, size=(1024, 768))
display.start()

DRIVER_LOCATION = "/usr/bin/chromedriver"  # whereis chromedriver
BINARY_LOCATION = "/usr/bin/google-chrome" # whereis google-chrome

options = Options()
options.add_argument(f'user-agent={userAgent}')
options.binary_location = BINARY_LOCATION
driver = webdriver.Chrome(executable_path=DRIVER_LOCATION, options=options)

# <-------------------------getsoup functions------------------------->
def bsRequests(url):
    html = requests.get(url, headers=headers)
    bs = BeautifulSoup(html.text,'html.parser')
    return bs

def bsSelenium(url):
    driver.get(url)
    time.sleep(0.5)
    html = driver.page_source
    bs = BeautifulSoup(html,'html.parser')
    return bs

# <-------------------------E N D------------------------->
driver.quit()
display.stop()