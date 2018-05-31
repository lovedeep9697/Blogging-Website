from django import forms
from blog_app.models import Post,Comment


class PostForm(forms.ModelForm):

	class Meta():
		model = Post
		fields = ('author','Title','Text')

		widgets={

			'Title':forms.TextInput(attrs={'class':'textinputclass'}),
			'Text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})


		}


class CommentForm(forms.ModelForm):

	class Meta():
		model = Comment
		fields = ('author','Text')

		widgets={

			'author':forms.TextInput(attrs={'class':'textinputclass'}),
			'Text':forms.Textarea(attrs={'class':'editable medium-editor-textarea '})


		}