from django.db import models
from django.db.models import Count
from django.core.paginator import Paginator
from django.utils import timezone

def annotate_posts_with_comments(query_set):
    return query_set.annotate(
        comment_count=Count('comments')
    ).order_by('-pub_date')

def get_paginated_page(request, query_set, per_page=10):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)

def filter_published_posts(query_set, user=None):
    query_set = query_set.filter(
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
    if not user or not user.is_authenticated:
        return query_set.filter(is_published=True)
    return query_set.filter(
        models.Q(is_published=True) | models.Q(author=user))
