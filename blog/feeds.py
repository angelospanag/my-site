from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy

from .models import Post


class LatestPostsFeed(Feed):
    title = 'Blog / Angelos Panagiotopoulos'
    link = reverse_lazy('blog:index')
    description = 'Recent posts of my blog'

    @staticmethod
    def items():
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
