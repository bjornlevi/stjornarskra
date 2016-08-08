from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _

class Sentance(models.Model):
	"""
	Sentance is a single sentance of an article
	"""
	text = models.CharField(max_length = 1024)
	ORIGIN_CHOICES = (
	    (1, _("Stjórnarskrá")),
    	(2, _("Frumvarp"))
	)
	origin = models.IntegerField(choices=ORIGIN_CHOICES, default=1, max_length=1)   

class SentanceForm(forms.ModelForm):
	class Meta:
		model = Sentance
		fields = ['text', 'origin']

class Article(models.Model):
	"""
	Article has many sentances
	"""
	nr = models.CharField(max_length = 3)
	sentances = models.ManyToManyField(Sentance, blank=True)

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['nr', 'sentances']

class Comparison(models.Model):
	"""
	Comparison contains two sentances and their ratio number
	"""
    stjornarskra = models.ForeignKey(Sentance, related_name="stjornarskra_set")
    frumvarp = models.ForeignKey(Sentance, related_name="frumvarp_set")
    ratio = models.CharField(max_length = 2)

class ComparisonForm(forms.ModelForm):
	class Meta:
		model = Comparison
		fields = ['stjornarskra', 'frumvarp', 'ratio']

class Match(models.Model):
	"""
	Saved match between two sentances
	"""
	match = models.OneToOneField(Comparison)

class MatchForm(forms.ModelForm):
	class Meta:
		model = Match
		fields = ['match']