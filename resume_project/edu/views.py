from django.shortcuts import render

# Create your views here.

def skill_page(request):
    context={
        "skill":"active"
    }
    return render(request , 'sk/skill.html', context )
