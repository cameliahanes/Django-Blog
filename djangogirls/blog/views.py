from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    # return HttpResponse('<h1>Page was found</h1>')
    return render(request, 'blog/post_list.html', {})