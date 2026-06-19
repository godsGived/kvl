from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'location', 'event_date', 'max_guests']
        widgets = {
            'event_date': forms.DateTimeInput(attrs={"class":"form-control"}),
            'title': forms.TextInput(attrs={"class":"form-control"}),
            'location': forms.TextInput(attrs={"class":"form-control"}),
            'max_guests': forms.NumberInput(attrs={"class":"form-control"})
        }