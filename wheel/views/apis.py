from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from wheel.models import Wheel, Sector

@login_required
def show(request, wheel_id):
    try:
        wheel = Wheel.objects.get(id=wheel_id)
        if wheel.owner != request.user:
            raise Exception('Requested item is not owned by user')
    except ObjectDoesNotExist:
        return HttpResponse('{"status": "error", "code": "Requested item does not exists"}', mimetype='application/json')
    except Exception as inst:
        return HttpResponse('{"status": "error", "code": "' + str(inst) + '"}', mimetype='application/json')
    canvas.delete()
    return HttpResponse('{"status": "success"}', mimetype='application/json')
