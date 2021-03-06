from blog.models import Post
from django import template
from django.db.models import Count

register=template.Library()
@register.simple_tag(name='my_tags')
def total_posts(): #is a name of custom template tag
    post_list=Post.objects.filter(status__exact='published')
    return post_list.count()


@register.inclusion_tag('blog/latest_post.html')
def show_latest_post(count=3):
    post=Post.objects.filter(status__exact='published')
    latest_post=post.order_by('-publish')[:count]
    return{'latest_post':latest_post}

@register.simple_tag
def get_MostCommentedPost(cnt=3):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments') [:cnt]
