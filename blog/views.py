from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post

posts =[
	{
		"author": "Aditya Kharadkar",
		"title": "Python",
		"date_posted": "August 27, 2022",
		"content": "This is an article or post about Python."
	},
	{
		"author": "Prasad Kulkarni",
		"title": "Account",
		"date_posted": "August 28, 2022",
		"content": "This is an article or post about Accounts."
	},
]

# Create your views here.
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})