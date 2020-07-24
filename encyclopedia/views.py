from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.urls import reverse
from . import util
import markdown
import random
from .forms import Newentry

md=markdown.Markdown()

def index(request):
    if request.method=="POST":
        data=request.POST.get('search_value').lower()
        entry_list=[x.lower() for x in util.list_entries()]
        if data in entry_list:
            html_body=util.get_entry(request.POST.get('search_value'))
            return HttpResponseRedirect(reverse("entry",kwargs={'entry': data}))
        elif matches(data):
            return render(request, "encyclopedia/search_list.html", {"search_list": matches(data)})
        else:
            return HttpResponse("Nothing")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,entry):
    html_body=util.get_entry(entry)
    if html_body=='error':
            return render(request, "encyclopedia/error.html")
    return render(request, "encyclopedia/entries.html", {"content":md.convert(html_body), "content_title":entry})
   
    

def matches(data):
    match=[]
    entry_list=[x.lower() for x in util.list_entries()]
    for each_list in entry_list:
        if data in each_list:
            match.append(each_list)
    return match

def edit(request,entry):
    html_body=util.get_entry(entry)
    if request.method=="POST":
        data=request.POST.get('wikipedia_edit')
        util.save_entry(entry,data)
        html_body=util.get_entry(entry)
        return render(request, "encyclopedia/entries.html", {"content":md.convert(html_body), "content_title":entry})

    return render(request, "encyclopedia/edit.html",{"content": html_body})

def randomentry(request):
    return HttpResponseRedirect(reverse("entry",kwargs={'entry': random.choice(util.list_entries())}))


def newentry(request):
    forms=Newentry()
    if request.method=="POST":
        form = Newentry(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            content=form.cleaned_data['content']
            util.save_entry(title,content)
            return HttpResponseRedirect(reverse("entry",kwargs={'entry':title }))
    
    return render(request,"encyclopedia/new page.html",{"form":forms})



