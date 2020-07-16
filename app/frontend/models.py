from django.db import models
from django.urls import reverse

# Create your models here.

class BlogEdit(models.Model):
	bloguser=models.CharField(max_length=20)
	title=models.CharField(max_length=50)
	blog=models.CharField(max_length=1000)
	tags=models.CharField(max_length=10)
	date=models.DateField(auto_now_add=True)

	class Meta:
		ordering=['-date']
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail',kwargs={'pk':self.pk})