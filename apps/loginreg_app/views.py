from django.shortcuts import render, redirect
from . import views
from .models import Users, Messages, Comments, UserManager
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def process(request):
    if request.POST['reg'] == 'new_user':
        result = Users.objects.basic_validator(request.POST)
        # print("LOOOOOOK",type(errors))
        # print('HERE ARE THE ERRORS',errors)
        # print("LOOK AT ALL OF THESE ERRORS",errors)
        if type(result) == dict:
            for key, value in result.items():
                messages.error(request, value)
            return redirect('/')
        else:
            # print(result.id)
            request.session['user_id'] = result.id
            request.session['user_name'] = str(result.first_name+' '+result.last_name)
            # print(request.session['user_name'])
            return redirect('/welcome')

    if request.POST['reg'] == 'login':
        result = Users.objects.basic_validator(request.POST)
        if type(result) == str:
            messages.error(request,result)
            return redirect('/')
        else:
            request.session['user_id'] = result.id 
            request.session['user_name'] = result.first_name
            print(request.session['user_id'])
            return redirect('/welcome')

def welcome(request):
    this_user = Users.objects.get(id=request.session['user_id'])
    # this_user.msg.message
    # all_users = Users.msg.all()
    # print(all_users)
    allmessages = Messages.objects.all()
    # print(Messages.objects.get(id=29).comment.all)
    context = {
        "allmessages": allmessages,
        # "unbid": Messages.objects.filter()
    }
    return render(request,'welcome.html',context)

def sendit(request):
    # print(request.POST)
    user_ = Users.objects.get(id=request.session['user_id'])
    Messages.objects.create(
        user = user_,
        message = request.POST['content']
    )
    return redirect('/welcome')

def comment(request):
    user = Users.objects.get(id=request.session['user_id'])
    message = Messages.objects.get(id=request.POST['message_id'])
    Comments.objects.create(
        user = user,
        comment = request.POST['comment'],
        message = message
    )
    return redirect('/welcome')
    

def reset(request):
    request.session.clear()
    return redirect('/')