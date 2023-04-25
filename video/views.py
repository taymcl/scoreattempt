from django.shortcuts import render
from .models import Video




# Create your views here.
def videoPage(request):
    return render(request, 'video/videoPage.html', {})




def video_detail(request, video_id):
    # Retrieve video details based on video_id from your database or any other source
    video = Video.objects.get(id=video_id) # Assuming you have a Video model with id field
    context = {'video_title': video.title, 'video_src': video.url}
    return render(request, 'video_detail.html', context)
