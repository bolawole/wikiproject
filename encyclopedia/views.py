from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown
import random

md=markdown.Markdown()

def index(request):
    if request.method=="POST":
        
        try:
            data=request.POST.get('search_value').lower()
            entry_list=[x.lower() for x in util.list_entries()]
            if data in entry_list:
                html_body=util.get_entry(request.POST.get('search_value'))
                return render(request, "encyclopedia/entries.html", {"content":md.convert(html_body)})
            elif matches(data):
                print(f"\n\n{matches(data)}\n\n")
                return render(request, "encyclopedia/search_list.html", {"search_list": matches(data)})
            else:
                return HttpResponse("Nothing")
        except AttributeError:
            entry_list=random.choice(util.list_entries())
            html_body=util.get_entry(entry_list)
            return render(request, "encyclopedia/entries.html", {"content":md.convert(html_body)})

   
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,entry):
    html_body=util.get_entry(entry)
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

# def randomentry(request):
#     listentry=util.list_entries()
#     random_entry= random.choice(listentry)
#     html_body=util.get_entry(random_entry)
#     return entry(request,random_entry)
    


