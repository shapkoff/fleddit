from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post
from comments.models import Comment
from django.http import JsonResponse

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
