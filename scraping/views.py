from .models import  Article
from django.views.generic import CreateView,TemplateView,DeleteView,UpdateView
from .scraping import get_article

class Index_Article(TemplateView):
    template_name = 'index.html'

    def __init__(self):
        super().__init__()
        self.param={
            'model':Article.objects.all()
        }

    def get(self, request, *args, **kwargs):
        return super().get(request,self.param)


class Create_Article(CreateView):
    model = Article
    template_name = 'create.html'


    def get(self, request, *args, **kwargs):

        return super().get(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request,*args,**kwargs)


class Update_Article(UpdateView):
    model = Article
    template_name = 'update.html'

    def get(self, request, *args, **kwargs):
        return super().get(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class Delete_Article(DeleteView):
    model = Article
    template_name = 'delete.html'
    success_url = '/delete'



