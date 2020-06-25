from django.shortcuts import render,redirect,get_object_or_404
from django.forms import ModelForm

from .models import Image

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'image']

def index(request, template_name='gallery/index.html'):
    images = Image.objects.all()
    data = {
        'object_list': images,
    }
    return render(request, template_name, data)

def image_create(request, template_name='gallery/form.html'):
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('gallery:home')
    return render(request, template_name, {'form':form})    

def image_update(request, pk, template_name='gallery/form.html'):
    image = get_object_or_404(Image, pk=pk)
    form = ImageForm(request.POST or None, instance=image)
    if form.is_valid():
        form.save()
        return redirect('gallery:home')
    return render(request, template_name, {'form':form})

def image_delete(request, pk, template_name='gallery/confirm_delete.html'):
    image = get_object_or_404(Image, pk=pk)    
    if request.method=='POST':
        image.delete()
        return redirect('gallery:home')
    return render(request, template_name, {'object':image})    