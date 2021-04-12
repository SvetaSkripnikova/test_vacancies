from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

from accounts.forms import LoginForm, RegisterForm, MyLoginForm, UserRegistrationForm


# def user_login(request):
#     if request.method == 'POST':
#         form = MyLoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('/')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = MyLoginForm()
#     return render(request, 'accounts/login.html', {'form': form})



class MyRegisterFormView(FormView):
    # Указажем какую форму мы будем использовать для регистрации наших пользователей, в нашем случае
    # это UserCreationForm - стандартный класс Django унаследованный
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/accounts/login"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "accounts/register.html"

    def form_valid(self, form):
        form.save()
        # Функция super( тип [ , объект или тип ] )
        # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

#регистрация
class MySignupView(CreateView):
   model = User

   #form_class = UserCreationForm
   form_class = RegisterForm
   success_url = reverse_lazy('login')
   template_name = 'accounts/register.html'

   def form_valid(self, form):
       form_valid = super().form_valid(form)
       username = form.cleaned_data["username"]
       first_name = form.cleaned_data["first_name"]
       last_name = form.cleaned_data["last_name"]
       password = form.cleaned_data["password"]
       auth_user = authenticate(username=username, first_name=first_name, last_name=last_name, password=password)
       login(self.request, auth_user)
       return form_valid


#вход
# class MyLoginView(LoginView):
#     form_class = LoginForm
#     success_url = '/'
#     redirect_authenticated_user = True
#     template_name = 'accounts/login.html'
#
#     def get_success_url(self):
#         return self.success_url('login')

 # class LogoutView(LogoutView):
 #     template_name = 'registration/logged_out.html'
    #next_page = reverse_lazy('logged_out')


# class LogoutView(View):
#     @staticmethod
#     def get(request):
#         logout(request)
#         return reverse_lazy("logout")

class LogoutSuccessView(View):
    @staticmethod
    def get(request):
        return render(request, 'accounts/logout_success.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})
