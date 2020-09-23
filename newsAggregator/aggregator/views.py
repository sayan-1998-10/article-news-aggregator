from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
import requests
from .models import newsModel
# Create your views here.

URL = 'https://indianexpress.com/section/india/'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

def get_news(request):
	session = requests.Session()
	# create a session object to improve performance in terms of reduced latency,
	# lesser network congestion, enabling http pipelining, redudcing CPU usage 
	# same tcp connection will be maintained for subsequent requests.
	source = session.get(URL,headers=headers).text
	soup = BeautifulSoup(source,'lxml')
	articles = soup.find_all('div',class_='articles')
	for article in articles:
		# create the model
		news_id    = article.a['href'].split('-')[-1].rstrip('/')
		news_title = article.h2.text
		news_body  = article.p.text
		news_url   = article.a['href'] 
		news_image = article.img['data-lazy-src'].split('?')[0]
		news_date  = article.find('div',class_='date').text 

		news_instance = newsModel()
		news_instance.id = news_id
		news_instance.title = news_title
		news_instance.body = news_body
		news_instance.article_url = news_url 
		news_instance.image = news_image
		news_instance.date = news_date
		try:
			news_instance.save()
		except Exception as e:
			pass
	latest_news = newsModel.objects.all()

	return render(request,'index.html',{'all_news':latest_news})