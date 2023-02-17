from django.shortcuts import render

def home_page(request):
    name = 'Hossain'
    title = 'Home'
    # u_name = request.POST
    context ={
        'name': name,
        'title':title,
    }
    return render(request, 'home/home.html', context)