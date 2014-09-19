from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from wheel.models import Wheel, Sector

@login_required
def list(request):
    wheel_list = Wheel.objects.all().filter(owner=request.user).order_by('name')
    context = {'wheel_list': wheel_list}
    return render(request, 'wheel/list.html', context)
