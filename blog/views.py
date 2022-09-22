from django.shortcuts import render
from django.http import HttpResponse

posts =[
	{
		"Author": "Aditya Kharadkar",
		"Title": "Python",
		"Date": "August 27, 2022",
		"Content": "This is an article or post about Python."
	},
	{
		"Author": "Prasad Kulkarni",
		"Title": "Account",
		"Date": "August 28, 2022",
		"Content": "This is an article or post about Accounts."
	},
]

# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})