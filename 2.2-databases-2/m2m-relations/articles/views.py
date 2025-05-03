from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'

    ordering = request.GET.get('ordering', '-published_at')

    valid_orderings = ['-published_at', 'published_at', 'title', '-title']
    if ordering not in valid_orderings:
        ordering = '-published_at'

    articles = Article.objects.prefetch_related(
        'scopes__tag'
    ).order_by(ordering)

    context = {
        'object_list': articles,
        'ordering': ordering
    }

    return render(request, template, context)