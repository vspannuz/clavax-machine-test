from django import forms
from task.models import student


from django.core import validators


import datetime



"""from phonenumber_field.formfields import PhoneNumberField"""



class studentForm(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'

    def clean(self):
        cleaned_data = super(studentForm,self).clean()
        dob = self.cleaned_data.get('dob')

        if (datetime.date.today().year-dob.year)<10 :
            raise forms.ValidationError("age must be greater than 10")

        if (datetime.date.today().year-dob.year)==10 :
            if datetime.date.today().month<dob.month:
                raise forms.ValidationError("age must be greater than 10")

        if (datetime.date.today().year-dob.year)==10 :
            if datetime.date.today().month==dob.month:
                if datetime.date.today().day<dob.day:
                    raise forms.ValidationError("age must be greater than 10")
