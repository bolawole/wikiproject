from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown

md=markdown.Markdown()

def index(request):
    if request.method=="POST":
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


    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,entry):
    
    html_body=util.get_entry(entry)
    print(f"\n\n {html_body}\n\n")
    return render(request, "encyclopedia/entries.html", {"content":md.convert(html_body)})
   
    

def matches(data):
    match=[]
    entry_list=[x.lower() for x in util.list_entries()]
    for each_list in entry_list:
        if data in each_list:
            match.append(each_list)
    return match
    