from django.shortcuts import render

def home(request):
    a = u"我在学Django，用它来建站。"
    #Alist = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'string': a}) #{'Uselist':Alist}

