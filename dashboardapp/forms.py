from django import forms
from  .models import Profile , Question,Answer
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['username']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)
        widgets = {
            'answer': forms.Textarea(attrs={'cols': 30, 'rows': 3}),
   }
