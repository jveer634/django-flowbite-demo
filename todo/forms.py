from django import forms

from .models import Todo



class TodoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({
            "class": "bg-gray-50 border border-gray-300 text-gray-900 text-md rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5",
        })

        self.fields["content"].widget.attrs.update({
            "class": "bg-gray-50 border border-gray-300 text-gray-900 text-md rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5",
        })
        self.fields["status"].widget.attrs.update({
            "class": "bg-gray-50 border border-gray-300 text-gray-900 text-md rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 ",
        })
    
    
    
    class Meta:
        model=Todo
        fields = ["title", "content", "status"]


    