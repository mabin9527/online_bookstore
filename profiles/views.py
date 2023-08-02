from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    """
    Display user profile
    """
    profile = get_object_or_404(
        UserProfile,user=request.user
    )
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'order': order,
    }
    return render(request, template, context)
