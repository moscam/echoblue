from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    template = loader.get_template('eb_v001a1/index.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


def do_login(request):

    context = RequestContext(request)

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/echoblue/dashboard/')
            else:
                # Return a 'disabled account' error message
                return HttpResponse("Disabled")

        else:
            # Return an 'invalid login' error message.
            return HttpResponse("Invalid login")

    else:
        return render_to_response('eb_v001a1/login.html', {}, context)


def do_logout(request):
    logout(request)
    return HttpResponseRedirect('/echoblue/')


@login_required()
def usr_dashboard(request):
    template = loader.get_template('eb_v001a1/dashboard.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


@login_required()
def usr_profile(request):
    template = loader.get_template('eb_v001a1/profile.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


@login_required()
def admin_create(request):
    template = loader.get_template('eb_v001a1/create.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


@login_required()
def admin_create_user(request):
    template = loader.get_template('eb_v001a1/create-user.html')
    context = RequestContext(request, {
    })

    userName = request.REQUEST.get('username', None)
    userPass = request.REQUEST.get('password', None)
    userMail = request.REQUEST.get('email', None)

'''    # TODO: check if already existed
    if userName and userPass and userMail:
        u, created = User.objects.get_or_create(userName, userMail)
        if created:
          u.set_password('new password')



          u.save
        else:
        # user was retrieved
    else:
       # request was empty

    return HttpResponse(template.render(context)) '''