from .models import  Article
from django.views.generic import ListView,CreateView,TemplateView,DeleteView,UpdateView
from .scraping import get_article
from .forms import url_forms
from django.shortcuts import render
import datetime


class Index_Article(ListView):
    template_name = 'basic/index.html'
    paginate_by = 5
    model = Article

    def get(self, request, *args, **kwargs):
        return super().get(request,*args,**kwargs)


class Create_Article(CreateView):
    model = Article
    template_name = 'basic/create.html'
    form_class = url_forms
    success_url = '/'

    def __init__(self):
        super().__init__()
        self.param={
            'title':'',
            'url':'',
            'text':''
        }

    def get(self, request, *args, **kwargs):
        return super().get(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        if self.param['title']=='':
            self.param['title']=datetime.date.today()
    
        return super(Create_Article, self).post(request,*args,**kwargs)


class Update_Article(UpdateView):
    model = Article
    template_name = 'baisc/update.html'

    def get(self, request, *args, **kwargs):
        return super().get(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class Delete_Article(DeleteView):
    model = Article
    template_name = 'basic/delete.html'
    success_url = '/'
    def __init__(self):
        super().__init__()
        self.param={
            'message':'このノートを削除しますか'
        }
    def get(self, request, *args, **kwargs):
        pass
    def post(self, request, *args, **kwargs):
        pass
