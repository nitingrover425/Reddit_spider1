# Reddit_spider1
This spider scrapes data from a particular reddit url and creates a csv file which contains title,points and timestamp of posts. 
## Starting a scrapy project with name reddit_scraper
```
scrapy start_project reddit_scrapper
```
## Coding the spider 
Inside the spiders folder , created a python file(reddit_spider.py)
Make a few changes in the setting.py file(to create a csv file) 

## Execute

```
scrapy crawl redditbot
```
This will execute the spider code and the desired csv file will be created.

