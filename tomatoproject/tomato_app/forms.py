from django import forms


class ImageUploadForm(forms.Form):
    """Form for uploading tomato leaf images"""
    image = forms.ImageField(
        label='Select a tomato leaf image',
        help_text='Upload a clear image of a tomato leaf for disease detection',
        widget=forms.ClearableFileInput(attrs={
            'id': 'id_image',
            'accept': 'image/jpeg,image/jpg,image/png',
            'class': 'form-control'
        })
    )


class MultiImageUploadForm(forms.Form):
    """Form for uploading multiple images"""
    images = forms.ImageField(
        label='Select multiple images',
        help_text='Hold Ctrl (or Cmd on Mac) to select multiple files'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].widget.attrs.update({
            'multiple': True,
            'accept': 'image/*'
        })
