from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post, Image
from comments.models import Comment
from django.http import JsonResponse
from .forms import PostForm, ImageForm
from django.contrib import messages

# Create your views here.
def post_view(request, branch, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        comment_text = request.POST['comment_text']
        if len(comment_text) > 0: 
            user = request.user

            comment = Comment.objects.create(text=comment_text, user=user, post=post)

            return JsonResponse({
                'success': True,
                'username': user.username,
                'text': comment.text,
            })

    comments = Comment.objects.filter(post=post)
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})

def add_new_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = Post(
                title=post_form.cleaned_data['title'],
                body=post_form.cleaned_data['body'],
                branch=post_form.cleaned_data['branch'],
                user=request.user
            )
            post.save()
        else:
            messages.warning(request, 'Can not save post')
            redirect('new')

        if image_form.is_valid():
            for img in request.FILES.getlist('image'):
                Image(image=img, post=post).save()
        else:
            messages.warning(request, 'Can not save image(s)')
            return redirect('new')
        
        messages.success(request, 'Post upload!')
        return redirect('profile')
    else:
        image_form = ImageForm()
        post_form = PostForm()
        return render(request, 'posts/new_post.html', {'image_form': image_form, 'post_form': post_form})
