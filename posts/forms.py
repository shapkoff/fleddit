from django.forms import ModelForm
from .models import Post, Image


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'branch']
        labels = {
            'body': 'Text'
        }


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'multiple': ''})
        self.fields['image'].required = False


# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True


# class MultipleFileField(forms.FileField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)

#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if isinstance(data, (list, tuple)):
#             result = [single_file_clean(d, initial) for d in data]
#         else:
#             result = [single_file_clean(data, initial)]
#         return result


# class FileFieldForm(forms.Form):
#     file_field = MultipleFileField()
