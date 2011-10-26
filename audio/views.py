from models import audio
from django.shortcuts import render_to_response

# define a function view
def listfile(request):
    # select * from audio
    files = audio.objects.all()

    # rendering html
    return render_to_response('index.html', {'data': files})