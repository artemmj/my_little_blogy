from django.shortcuts import render, get_object_or_404

from .models import Article


def get_all(request):
    context = {'articles': Article.objects.all()[:5]}
    return render(request, 'articles/articles.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 'articles/detailed_article.html', context)
