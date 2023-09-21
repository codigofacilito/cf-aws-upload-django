from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import default_storage


def index(request):

    image_url = None

    if request.method == 'POST' and request.FILES.get('imagen'):
        uploaded_image = request.FILES['imagen']
        
        image_path = f'{uploaded_image.name}'
        image_url = default_storage.save(image_path, uploaded_image)
        image_url = f'https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/{image_url}'

    return render(request, 'index.html', {
        'image_url': image_url
    })