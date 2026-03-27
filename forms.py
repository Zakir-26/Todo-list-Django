from django import forms

class item(forms.Form):
    task = forms.CharField(widget = forms.TextInput(attrs={ 
        "placeholder":"Add task",   

    }), 
        required= True,
        label = "Add Task"
        
    )