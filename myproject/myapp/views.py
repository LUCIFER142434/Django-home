from django.shortcuts import render

def index(elen):
    return render (elen,"index.html")

def about(elen):
    return render (elen,"about.html")

def blog(elen):
    return render (elen,"blog.html")

def clas(elen):
    return render (elen,"class.html")










def copy_fun(element):
    copy_li = [
        {"name":"Home","url":"#","active":True},
        {"name":"about","url":"about","active":False},
        {"name":"class","url":"class","active":False},
        {"name":"blog","url":"blog","active":False},
    ]
    copy_blog = [
        {"img":"static/images/b1.jpg","age":17,"name":"Fed","profi":"Boxer Joniya Daro","active":True},
        {"img":"static/images/b2.jpg","age":27,"name":"Jun","profi":"Boxer Joniya Daro","active":True},
    ]
    
    copy_return = {"copy_li":copy_li,"copy_blog":copy_blog}
    return render(element, "index.html",copy_return)
