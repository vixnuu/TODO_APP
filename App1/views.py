from django.shortcuts import render,redirect
from django.views import View
from App1.forms import TodoForm,LoginForm,TodoEditForm,RegisterForm,TodoAssignForm,TodoCompleteForm
from django.contrib.auth import login,authenticate,logout
from django.views.generic import TemplateView,DetailView,DeleteView,FormView
from App1.models import Todo
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.
class HomeView(TemplateView):
   template_name="home.html"
   def get_context_data(self, **kwargs):
      context= super().get_context_data(**kwargs)
      # Todos created for me (creator is user and assigned_to is user)
      my_todos = Todo.objects.filter(creator=self.request.user, assigned_to=self.request.user)
      # Todos I assigned to others (creator is user, assigned_to is not user)
      assigned_to_others = Todo.objects.filter(creator=self.request.user).exclude(assigned_to=self.request.user)
      # Todos assigned to me by others (assigned_to is user, creator is not user)
      assigned_to_me = Todo.objects.filter(assigned_to=self.request.user).exclude(creator=self.request.user)
      context['my_todos'] = my_todos
      context['assigned_to_others'] = assigned_to_others
      context['assigned_to_me'] = assigned_to_me
      return context
   

# class HomeView(TemplateView):
#    template_name="home.html"
#    def get_context_data(self, **kwargs):
#       context= super().get_context_data(**kwargs)
#       todos=Todo.objects.filter(user=self.request.user)
#       context['todo']=todos
#       return context

class CreateTodo(View):
   def get(self,request):
      form = TodoForm()
      return render(request, 'create_todo.html', {"form": form})

   def post(self,request):
      form = TodoForm(request.POST, request.FILES)
      if form.is_valid():
         user=request.user
         Todo.objects.create(creator=user, assigned_to=user, **form.cleaned_data)
         return redirect('home')
      else:
         return HttpResponse('done')
   

class DetailView(DetailView):
   template_name='detail.html'
   model=Todo
   pk_url_kwarg='id'
   context_object_name='todo'

class UpdateView(View):
   def get(sel,request,**kwargs):
      todo=Todo.objects.get(id=kwargs.get('id'))
      if request.user == todo.creator:
         form=TodoEditForm(instance=todo)
         return render(request,'update.html',{'form':form})

      else:
         form=TodoCompleteForm(instance=todo)
         return render(request,'update.html',{'form':form})


   def post(self,request,**kwargs):
      todo=Todo.objects.get(id=kwargs.get('id'))
      if request.user == todo.creator:
         form=TodoEditForm(request.POST, request.FILES, instance=todo)
      else:
         form=TodoCompleteForm(request.POST, request.FILES, instance=todo)
      if form.is_valid():
         form.save()
         return redirect('detail',id=todo.id)
      else:
         return HttpResponse('error')
      
class DeleteView(DeleteView):
   def get(self,request,**kwargs):
      todo=Todo.objects.get(id=kwargs.get('id'))
      todo.delete()
      return redirect('home')







class AssignCreateView(View):
   def get(self,request,**kwargs):
      form=TodoAssignForm(user=request.user)
      return render(request,'assign.html',{'form':form})
   
   def post(self,request,**kwargs):
      form=TodoAssignForm(request.POST, request.FILES, user=request.user)
      user=request.user
      print(user)
      if form.is_valid():
         todo=Todo.objects.create(creator=request.user,**form.cleaned_data)
         return redirect('home')
      else:
         return render(request,'assign.html',{'form':form})



   # def post(self,request,**kwargs):
   #    form=TodoAssignForm(request.POST)
   #    if form.is_valid():
   #       todo = Todo.objects.create(
   #          user=request.user,
   #          title=form.cleaned_data['title'],
   #          description=form.cleaned_data['description'],
   #          due_date=form.cleaned_data['due_date']
   #       )
   #       AssignedTodo.objects.create(
   #          todo=todo,
   #          assigned_to=form.cleaned_data['assigned_to']
   #       )
   #       return redirect('home')
   #    else:
   #       return render(request,'assign.html',{'form':form})
   


# class AssignHomeView(TemplateView):
#    template_name='home.html'
#    def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       todos=AssignedTodo.objects.filter()



# def get_context_data(self, **kwargs):
#        context= super().get_context_data(**kwargs)
#        todos=Todo.objects.filter(user=self.request.user)
# +      assigned_todos=AssignedTodo.objects.filter(assigned_to=self.request.user)
#        context['todo']=todos
# +      context['assigned_todos']=assigned_todos
#        return context
















class LoginView(View):
   def get(self,request):
      form=LoginForm
      return render(request,'login.html',{'form':form})

   def post(self, request):
      form = LoginForm(request.POST)
      username=request.POST.get('username')
      password=request.POST.get('password')
      user=authenticate(request,username=username,password=password)
      if user:
         login(request,user)
         return redirect('home')
      else:
         return redirect('login')

      


   #       username = form.cleaned_data['username']
   #       password = form.cleaned_data['password']
   #       user = authenticate(request, username=username, password=password)
   #       if user is not None:
   #          login(request, user)
   #          return redirect('home')
   #       else:
   #          form.add_error(None, 'Invalid username or password')
   #    return render(request, 'login.html', {'form': form})
   

class RegisterView(FormView):
   form_class=RegisterForm
   template_name='register.html'

   def post(self,request):
      form=RegisterForm(request.POST)
      if form.is_valid():
         User.objects.create_user(**form.cleaned_data)
         return redirect('login')
      
class LogoutView(View):
   def get(self,request):
      logout(request)    
      return redirect('login')