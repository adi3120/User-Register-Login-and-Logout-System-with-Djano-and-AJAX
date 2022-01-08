from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):

	fm=UserCreationForm()

	allusers=User.objects.values();
	allusers=list(allusers)

	logfm=AuthenticationForm()

	context={
		'form':fm,
		'loginform':logfm,
		'allusers':allusers,
	}

	return render(request,'ajaxloginapp/home.html',context)

def user_register(request):
	fm=UserCreationForm()
	context={}
	if request.method=="POST":
		fm=UserCreationForm(request.POST)
		if fm.is_valid():
			print("form is valid")
			fm.save()
			messages.success(request,"User Registered Successfully")
		else:
			print("form is not valid")
			messages.error(request,"registration failed")
	else:
		fm=UserCreationForm()
			
	allusers=User.objects.values()
	allusers=list(allusers)

	context={
		'allusers':allusers,
	}
	return JsonResponse(context)
	


def user_login(request):
	context={}
	if request.method=="POST":
		logfm=AuthenticationForm(request=request,data=request.POST)
		print()
		if logfm.is_valid():
			uname=logfm.cleaned_data['username'] #name="Username"
			upass=logfm.cleaned_data['password'] #name="Password"
			user=authenticate(username=uname,password=upass)
			print("\n\n\n login form is valid \n\n\n")
			if user is not None:
				login(request,user)
				messages.success(request,"Logged in successfully")#goes to the next page down...here 
				name=request.user.username
				print(f"\n\n\n user name ={name}\n\n\n")
				context={
					'userdetails':name,
				}
		else:
			print("\n\n\n login form is not valid \n\n\n")
	print(f"\n\n\n context={context} \n\n\n")
	return JsonResponse(context)

def user_logout(request):
	logout(request)
	return redirect('/reglogajax/')
@csrf_exempt
def user_delete(request):
	if request.method=='POST':
		id=request.POST.get('uid')
		pi=User.objects.get(pk=id)
		print(f"\n\n\n delete this user {pi}  \n\n\n")
		pi.delete()
		return JsonResponse({'status':1})
	else:
		return JsonResponse({'status':0})

