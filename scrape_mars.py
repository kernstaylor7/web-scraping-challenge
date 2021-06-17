import pymongo
import requests
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time



# Setting up db
mg_client = pymongo.MongoClient('mongodb://localhost:27017')
db = mg_client.mars_db
collection = db.mars 

def init_browser():
    path = {'path': 'Desktop/Homework/Week_12/chromedriver.exe'}
    browser=Browser('chrome', path, headless=False)
def scrape():
    browser = init_browser()

#News
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    news_html = browser.html
    mars_soup = BeautifulSoup(news_html, 'html.parser')
    news_title =news_element.find('div', class_="content_title").get_text()
    news_paragraph= news_element.find('div', class_='article_teaser_body').get_text()

#JPL Images
    feature_url = ('https://www.jpl.nasa.gov/images')
    browser.visit(feature_url)
    feature_html = browser.html
    feature_soup = BeautifulSoup(feature_html,"html.parser")
    img_url = feature_soup.find('div',class_='carousel_container').article.footer.a['data-fancybox-href']


#Facts
    facts_url = 'https://space-facts.com/mars/'
    facts_table = pd.read_html(facts_url)
    facts_table = table[0]

#Hemispheres
    facts_url = ("https://space-facts.com/mars/")
    browser.visit(facts_url)  
    mh_html = browser.html 
    mh_soup = BeautifulSoup(mh_html,"html.parser") 
    downloads = mh_soup.find_all("div",class_='item')
    hemisphere_img_urls = []
    for result in results:
            mars_dict = {}
            titles = result.find('h3').text
            end = result.find("a")["href"]
            img_link = "https://astrogeology.usgs.gov/" + end    
            browser.visit(img_link)
            html = browser.html
            mh_soup= BeautifulSoup(html, "html.parser")
            downloads = mh_soup.find("div", class_="downloads")
            img_url = downloads.find("a")["href"]
            mars_dict['title']= titles
            mars_dict['img_url']= img_url
            hemisphere_img_urls.append(mars_dict)








    

    browser.quit()



    mars_data ={
		'news_title' : news_title,
		'summary': news_paragraph,
		'fact_table': facts_table,
		'hemisphere_image_urls': hemisphere_img_url,
        'news_url': news_url,
        'jpl_url': feature_url,
        'fact_url': facts_url,
        'hemisphere_url': mh_url,
        }
    collection.insert(mars_data)