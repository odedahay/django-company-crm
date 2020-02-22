from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

def test_view_2(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
    else:
        user = 'no user'
    
    context = {
        'user': profile
    }

    return render(request, 'profiles/test.html', context)