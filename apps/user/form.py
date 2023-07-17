from django import forms

from apps.user.models import User

#Buscar herencia de modelForm
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
                  "first_name", 
                  "email",
                  "birthdate",
                  "address",]


#buscar herencia form
class UserForm2(forms.forms):
    first_name=forms.CharField()
    email=forms.EmailField()
    birthdate=forms.DateField()
    address=forms.CharField()
