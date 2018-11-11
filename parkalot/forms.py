from django import forms

class startParkForm(forms.Form):
    customerId = forms.IntegerField(required=True)
    coordinates = forms.CharField(max_length=30)