from django.shortcuts import render, redirect

# Create your views here.
def defaultHome(request):
    if request.user.is_authenticated:
        return redirect('/notes')
    else:
        return redirect('/login')
    
# Create your views here.
def logoutPage(request):
    return render(request, "registration/logout.html")