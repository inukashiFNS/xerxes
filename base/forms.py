from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        #will have all attributes from the room in models.py except the unditables ones
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
       model = User
       fields = ['username', 'email'] 