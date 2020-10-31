from django.shortcuts import render

# Create your views here.
def articles_landing_page(request):
    return render(request, 'articles/articles_landing_page.html')

def article_page2(request):
        return render(request, 'articles/article_page2.html')
