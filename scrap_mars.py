from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape:

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'http://redplanetscience.com/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    # Retrieve the div for the latest article
    results = soup.find('div', class_='content_title')
    news_title = results.text

    # Retrieve the div for the latest paragraph of the latest article
    results = soup.find('div', class_='article_teaser_body')
    news_p = results.text

    browser.quit()

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    # Get href of featured image
    results = soup.find('a', class_='showimg')
    # print(results['href'])

    featured_image_url=url+results['href']

    browser.quit()

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)

    mars_df=tables[1]

    # Convert table to html table
    mars_table_html = mars_df.to_html()

    browser.quit()

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://marshemispheres.com/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    # Retrieve titles of all hemispheres from main page

    titles = []

    hemispheres = soup.find_all('div', class_='description')
    for hemisphere in hemispheres:
        h3 = hemisphere.find('h3')
        titles.append(h3.text)

    hemisphere_image_urls = []

    for title in titles:
        hemisphere_image_urls.append({'title': title,'img_url':''})

    # Retrieve image url for first hemisphere
    hemi_url = 'https://marshemispheres.com/cerberus.html'
    browser.visit(hemi_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    results = soup.find_all('a', target='_blank') 
    imgURL = results[3]['href']
    imgURL = url + imgURL

    hemisphere_image_urls[0]['img_url'] = imgURL

    # Retrieve image url for second hemisphere

    hemi_url = 'https://marshemispheres.com/schiaparelli.html'
    browser.visit(hemi_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    results = soup.find_all('a', target='_blank') 
    imgURL = results[3]['href']
    imgURL = url + imgURL

    hemisphere_image_urls[1]['img_url'] = imgURL

    # Retrieve image url for third hemisphere

    hemi_url = 'https://marshemispheres.com/syrtis.html'
    browser.visit(hemi_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    results = soup.find_all('a', target='_blank') 
    imgURL = results[3]['href']
    imgURL = url + imgURL

    hemisphere_image_urls[2]['img_url'] = imgURL

    # Retrieve image url for fourth hemisphere

    hemi_url = 'https://marshemispheres.com/valles.html'
    browser.visit(hemi_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    results = soup.find_all('a', target='_blank') 
    imgURL = results[3]['href']
    imgURL = url + imgURL

    hemisphere_image_urls[3]['img_url'] = imgURL

    mars_data = {
    'title' : news_title,
    'news' : news_p,
    'mars_image' : featured_image_url,
    'facts' : mars_table_html,
    'hemis' : hemisphere_image_urls
    }

    return mars_data







