from django.db import models
import random
# Create your models here.

def random_num():
	return random.randint(100000,999999)
class newsModel(models.Model):
	id = models.BigIntegerField(db_column='Aricle-ID',primary_key=True,default=random_num)
	title = models.CharField(db_column='Title',max_length=200)
	body = models.TextField(db_column='Detail')
	article_url = models.URLField(db_column='Link')
	image = models.URLField(null=True,blank=True)
	date = models.CharField(null=False,db_column='Date',max_length=50,default='None')

	def __str__(self):
		print(self.title)

