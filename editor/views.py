from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def editor_index(request):
    """"
    A view to display editor homepage
    """
    userinfo = request.user.username
    context = {
        'userinfo': userinfo
    }
    return render(request, 'editor/editor_index.html', context)


