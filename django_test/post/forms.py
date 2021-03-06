from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(
        widget=forms.Textarea(

        ),
    )

    photo = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
