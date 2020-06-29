from django import forms
from .models import Post, Category, Comment

# choices = [('coding', 'coding'), ('sports', 'sports'), ('games', 'games')]
choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Напишите название'}),
            # поле ввода
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),

            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Напишите что-нибудь полезное :)', 'id':'body'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'id': 'snip_id'})
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # поле ввода
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text', )
        widgets = {
            'comment_text': forms.Textarea(attrs={'class': 'from-control', 'placeholder':'Текст комментария'}),
        }
