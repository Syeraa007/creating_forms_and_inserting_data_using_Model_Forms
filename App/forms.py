from django import forms
from App.models import *

class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'

class PageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'

class RecordForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'     