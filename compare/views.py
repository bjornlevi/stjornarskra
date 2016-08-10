from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import redirect
from compare.models import *

from fuzzywuzzy import fuzz

class ArticleList(ListView):
  model = Article

  def get_context_data(self, **kwargs):
    context = super(ArticleList, self).get_context_data(**kwargs)
    return context

class ArticleDetail(DetailView):
  model = Article

  def get_context_data(self, **kwargs):
    context = super(ArticleDetail, self).get_context_data(**kwargs)
    return context

def add_match(request, stjornarskra_sentence_id, frumvarp_sentence_id):
	stjornarskra = Sentence.objects.get(id=stjornarskra_sentence_id)
	frumvarp = Sentence.objects.get(id=frumvarp_sentence_id)
	ratio = fuzz.ratio(stjornarskra.text, frumvarp.text)
	Match.objects.create(stjornarskra=stjornarskra, frumvarp=frumvarp, ratio=ratio)
	return redirect('compare:article_list')

def remove_match(request, stjornarskra_sentence_id, frumvarp_sentence_id):
	Match.objects.filter(stjornarskra=stjornarskra_sentence_id, frumvarp=frumvarp_sentence_id).delete()
	return redirect('compare:article_list')

class NotMatchList(ListView):
	model = Match
	template_name = 'compare/nomatch_list.html'

	def get_context_data(self, **kwargs):
		context = super(NotMatchList, self).get_context_data(**kwargs)
		match_stjornarskra = Match.objects.filter(stjornarskra__origin=1)
		stjornarskra_sentence = [s.stjornarskra.id for s in match_stjornarskra]

		context['nomatch_list'] = Sentence.objects.filter(origin=1).exclude(id__in=stjornarskra_sentence)
		return context

class NewList(ListView):
	model = Match
	template_name = 'compare/new_list.html'

	def get_context_data(self, **kwargs):
		context = super(NewList, self).get_context_data(**kwargs)
		match_frumvarp = Match.objects.filter(frumvarp__origin=2)
		frumvarp_sentence = [f.frumvarp.id for f in match_frumvarp]

		context['new_list'] = Sentence.objects.filter(origin=2).exclude(id__in=frumvarp_sentence)
		return context