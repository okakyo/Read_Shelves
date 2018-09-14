from .models import  Article
from django.views.generic import CreateView,DetailView,DeleteView,UpdateView

class Article_View(DetailView):
    pass

class Create_Article(CreateView):
    pass

class Update_Article(UpdateView):
    pass

class Delete_Article(DeleteView):
    pass


