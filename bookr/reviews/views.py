from django.shortcuts import render

def index(request):
    name = "world"
    return render(request,"base.html", {"name":name})

def book_search(request):
    search_text = request.GET.get("search", request.GET.get("blue", "hello"))
    return render(request, "search_results.html", {"search_text":search_text})