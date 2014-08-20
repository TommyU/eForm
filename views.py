# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponseRedirect
from forms import  *
from models import request_form

from django.views.generic import TemplateView

# Create your views here.

def leave_request(req):
    if req.method=='POST':
        form = request_formForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/lrl/')
    else:
        return render_to_response('leave_request_form.html',
                                  {'form':request_formForm()},
                                  context_instance=RequestContext(req))

def leave_request_list(req):
    if req.method=='POST':
        return HttpResponseRedirect('/lr/')
    else:
        return render_to_response('leave_request_tree.html',{'forms':request_form.objects.all()},context_instance=RequestContext(req))

#分页
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def listing(request):
    request_list = request_form.objects.all()
    paginator = Paginator(request_list, 10) # Show 10 requests per page

    page = request.GET.get('page')
    try:
        requests = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，则传递第一页数据过去
        requests = paginator.page(1)
    except EmptyPage:
        # 如果页码超出了最大页码，则传递最后一页
        requests = paginator.page(paginator.num_pages)

    return render_to_response('leave_request_tree2.html', {"object_list": requests,'page_obj':requests})

#================================以上是函数视图，以下是基于类的视图==================================================

class leaveRequestView(TemplateView):
    template_name = 'leave_request_tree.html' # or define get_template_names()

    def get_context_data(self, **kwargs):
        context = super(leaveRequestView, self).\
            get_context_data(**kwargs)
        context.update({'forms':request_form.objects.all()})

        return context
#列表视图
from django.views.generic.list import ListView
class leaveRequestView2(ListView):
    template_name ='leave_request_tree2.html'#template中需要用object_list引用模型集
    model = request_form
    paginate_by =20

#表单视图（view)
from django.views.generic.detail import DetailView
class leaveRequestDetailView(DetailView):
    template_name ='leave_request_form2.html'#template中需要用object引用模型
    model = request_form
#表单视图(create1)
from django.views.generic.edit import FormView
class leaveRequestEditView(FormView):
    template_name ='leave_request_form2.html'#template中需要用form引用模型
    form_class = request_formForm
    success_url = '/lrequest2'
    def form_valid(self,form):
        form.save()
        return super(leaveRequestEditView,self).form_valid(form)

#表单视图(create1)
from django.views.generic.edit import CreateView
class leaveRequestCreateView(CreateView):
    template_name ='leave_request_form2.html'#template中需要用form引用模型
    model  = request_form
    success_url = '/lrequest2'

#表单视图(update)
from django.views.generic.edit import UpdateView
class leaveRequestUpdateView(UpdateView):
    template_name ='leave_request_form2.html'#template中需要用form引用模型
    model  = request_form
    success_url = '/lrequest2'

from django.views.generic.edit import DeleteView
class leaveRequestDeleteView(DeleteView):
    template_name ='leave_request_form2.html'#template中需要用object引用模型
    model  = request_form
    success_url = '/lrequest2'



#class leaveRequestDetailView2(DetailView):#按照SlugField进行搜索，需要有SlugField类型的字段
#    template_name ='leave_request_form2.html'#template中需要用object引用模型
#    model = request_form
#    slug_field = 'request_no'
#===============================上面在玩，下面玩真的===================================
from django.db.models import Q
class requestList(ListView):
    model = request_form
    template_name = 'request_form_list.html'
    paginate_by =10

    def get_queryset(self):
        search_val = self.request.GET.get('val', False) if self.request.GET else False
        if search_val:
            return request_form.objects.filter(
                Q(request_no__icontains = search_val)|
                Q(name__name__icontains=search_val)
            )
        else:
            return request_form.objects.all()

    def get_context_data(self, **kwargs):
        context = super(requestList, self).get_context_data(**kwargs)
        context.update(sval=self.request.GET.get('val', False)
        if self.request.GET
        else False
        )
        return context


class requestDetail(DeleteView):
    model = request_form
    template_name = 'request_form_detail.html'

    def get_context_data(self, **kwargs):
        return super(requestDetail,self).get_context_data()

class requestCreate(CreateView):
    model = request_form
    form_class = request_formForm
    template_name = 'request_form_create.html'
    success_url = '/requests'
    initial = {'date_from':datetime.date.today() + datetime.timedelta(3)}

class requestDelete(DeleteView):
    model = request_form
    template_name = 'request_form_delete.html'
    success_url = '/requests'
    context_object_name = 'dddE'

class requestUpdate(UpdateView):
    model = request_form
    form_class = request_formForm
    template_name = 'request_form_create.html'
    success_url = '/requests'