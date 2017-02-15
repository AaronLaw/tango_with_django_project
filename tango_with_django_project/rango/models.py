from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Categories'

	# Override the save() of Category moder, for slugify the name
	# In order to reverse url in view
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
		

class Page(models.Model):
	Category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.title
