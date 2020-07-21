from django.shortcuts import render

# Create your views here.
from catalog.models import Article, Author, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_articles = Article.objects.all().count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_articles': num_articles,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
from django.views import generic

class ArticleListView(generic.ListView):
    model = Article
from django.views import generic

class ArticleDetailView(generic.DetailView):
    model = Article

class AuthorListView(generic.ListView):
    model = Author
class AuthorDetailView(generic.DetailView):
    model = Author