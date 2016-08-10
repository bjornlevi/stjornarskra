from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _

from fuzzywuzzy import fuzz

class Sentence(models.Model):
	"""
	sentence is a single sentence of an article
	"""
	text = models.CharField(max_length = 1024)
	ORIGIN_CHOICES = (
	    (1, _("Stjórnarskrá")),
    	(2, _("Frumvarp"))
	)
	origin = models.IntegerField(choices=ORIGIN_CHOICES, default=1)   
	article_nr = models.CharField(max_length=3)

	def __lt__(self, other):
		return self.article_nr < other.article_nr

	def __str__(self):
		return self.text

	def find_matches(self):
		results = []
		for f in Sentence.objects.filter(origin=2):
			ratio = fuzz.ratio(self.text, f.text)
			if ratio == 100:
				return [(ratio, f)]
			if ratio > 0:
				results.append((ratio, f))
		return sorted(results)[::-1]

class SentenceForm(forms.ModelForm):
	class Meta:
		model = Sentence
		fields = ['text', 'origin', 'article_nr']

class Match(models.Model):
	ratio = models.IntegerField()
	stjornarskra = models.ForeignKey(Sentence, related_name='stjornarskra')
	frumvarp = models.ForeignKey(Sentence, related_name='frumvarp')

class Article(models.Model):
	nr = models.CharField(max_length=3, unique=True)
	sentences = models.ManyToManyField(Sentence)
