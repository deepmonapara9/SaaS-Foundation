from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
<<<<<<< HEAD

@login_required
def profile_list_view(request, *args, **kwargs):
    
    context = {
        "object_list": User.objects.filter(is_active=True)
    }
    return render(request, 'profiles/list.html', context)


@login_required
def profile_detail_view(request, username=None, *args, **kwargs):
    user = request.user
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    context = {
        "object": profile_user_obj,
        "instance": profile_user_obj,
        "owner": is_me,
    }
    return render(request, 'profiles/detail.html', context)
=======
@login_required
def profile_view(request, username=None, *args, **kwargs):
    user = request.user
    print('user.has_perm("auth.view_user")', user.has_perm("auth.view_user"))
    print('user.has_perm("visits.view_pagevisit")', user.has_perm("visits.view_pagevisit"))
    # profile_user_obj = User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    return HttpResponse(f"Hello there! {username} - {profile_user_obj.id} - {user.id} - {is_me}")
>>>>>>> 3a2120fc09fda309b1e2a0621e83501bb5925e6c
