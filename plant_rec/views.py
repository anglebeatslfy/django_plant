from django.shortcuts import render
from plant.predict import predict
import os
# Create your views here.


def index(request):

    if request.method == 'POST':
        img = request.FILES.get('img')
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        url = os.path.join(BASE_DIR, 'static', 'imgs_temp', img.name)
        with open(url, 'wb') as f:
            for chunk in img.chunks():
                f.write(chunk)
        plant_dict = predict(url)
        context = {
            'status': True,
            'img': url,
            'plants': plant_dict,
            'result': list(plant_dict.keys())[0]
        }
        return render(request, 'index.html', context=context)
    else:
        context = {
            'status': False,
        }
        return render(request, 'index.html', context=context)