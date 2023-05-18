from django.urls import reverse_lazy
from .forms import todoform
from django.shortcuts import redirect, render
from . models import task
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView

class taskListview(ListView):
    model=task
    template_name='home.html'
    context_object_name='task1'

class  taskdetailview(DetailView):
    model=task
    template_name='detail.html'
    context_object_name='task2'


class taskupdateview(UpdateView):
    model=task
    template_name='update.html'
    context_object_name='task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
    

class taskdeleteview(DeleteView):
    model=task
    template_name='delete.html'
    success_url=reverse_lazy('cbvhome')
    


# Create your views here.
def add(request):
    task1=task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        tasks=task(name=name,priority=priority,date=date)
        tasks.save()
    return render(request,'home.html',dict(task1=task1))

# def detail(request):
#     taskss=task.objects.all()
#     return render(request,'detail.html',{'tasks':taskss})


def delete(request,taskid):
    if request.method=='POST':
        tasks=task.objects.get(id=taskid)
        tasks.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    tasks=task.objects.get(id=id)
    formsss=todoform(request.POST or None,instance=tasks)
    if formsss .is_valid():
        formsss.save()
        return redirect('/')

    return render (request,'edit.html',{'form':formsss,'tasks':tasks})