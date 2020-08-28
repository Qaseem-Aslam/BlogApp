from django.shortcuts import render
#from account.models import Account
from blog.models import BlogPost
from operator import attrgetter
from blog.views import get_blog_queryset
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def home_screen_view(request):
	context = {}
	# context['some_string'] = 'this string came from python file!OoooOoooOooooooo'
	# context['integer'] = 12345
	# context = {
	# 	'some_string': 'this string came from python file!OoooOoooOooooooo',
	# 	'integer': 12345
	# }
	# list_values = []
	# list_values.append('123')
	# list_values.append('456')
	# list_values.append('789')

	# context['list_values'] = list_values

	# question = Question.objects.all()
	# context['questions'] = question
	BLOG_POSTS_PER_PAGE=1
	query=""
	if request.GET:
		query = request.GET.get('q','')
		context['query'] = str(query)

	blog_posts = sorted(get_blog_queryset(query),key=attrgetter('date_updated'),reverse=True)

	#pagination
	page = request.GET.get('page',1)
	blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
	try:
		blog_posts = blog_posts_paginator.page(page)
	except PageNotAnInteger:
		blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)
	context['blog_posts'] = blog_posts

	return render(request,"home.html",context)