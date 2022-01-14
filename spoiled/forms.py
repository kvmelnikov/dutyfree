from spoiled.models import Spoiled, Nomenclature
from django import forms
from spoiled.humanize import  naturalsize
from django.core.files.uploadedfile import InMemoryUploadedFile

class SpoiledForm(forms.ModelForm):

    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    picture = forms.FileField(required=False, label='File to Upload <= ' + max_upload_limit_text)
    upload_field_name = 'picture'

    class Meta:
        model = Spoiled
        fields = ['nomenclature', 'description_comment', 'shop', 'quantity', 'sub_description', 'picture', 'future_spoiled', 'discount_percent']

    def __init__(self, *args, **kwargs):
        super(SpoiledForm, self).__init__(*args, **kwargs)

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'{fieldname} обязательный к заполнению'.format(
                fieldname=field.label)}

    # Validate the size of the picture
    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None:
            return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < " + self.max_upload_limit_text + " bytes")

    # Convert uploaded File object to a picture
    def save(self, commit=True):
        instance = super(SpoiledForm, self).save(commit=False)
        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.picture  # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            instance.name_photo = f
            instance.content_type = f.content_type
            instance.picture = bytearr  # Overwrite with the actual image data
        if commit:
            instance.save()

        return instance
