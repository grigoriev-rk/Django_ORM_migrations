from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    ordering = '-published_at'
    articles = Article.objects.order_by(ordering)
    template = 'articles/news.html'
    context = {'object_list': articles}
    return render(request, template, context)
