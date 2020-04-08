import scrapy

class RedditbotSpider(scrapy.Spider):
	name = 'redditbot'
	allowed_domains = ['www.reddit.com/r/DamnUEngineering/new/']
	start_urls = ['https://www.reddit.com/r/DamnUEngineering/new/']
	
	def parse(self,response):
		#Extracting the content using css selectors
		titles = response.css('h3::text').extract()
		points = response.css('div[class*="_1rZYMD_4xY3gRcSS3p8ODO"]::text').extract()
		times = response.css('a[data-click-id*="timestamp"]::text').extract()




		#Give the extracted content row wise
		for item in zip(titles,points,times):
			#create a dict to store the scraped info
			scraped_info =
			{
				'title' : item[0],
				'points' : item[1],
				'time' : item[2]
			}

			yield scraped_info

