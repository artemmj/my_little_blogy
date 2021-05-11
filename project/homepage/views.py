from django.shortcuts import render

from articles.models import Article


def index(request):
    articles = Article.objects.all()
    for article in articles:
        article.text = f'{article.text[:256]}...'

    return render(
        request,
        'homepage/index.html',
        context={'articles': articles},
    )


def about(request):
    return render(request, 'homepage/about.html')
