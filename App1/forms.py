from django import forms
from App1.models import Todo
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime



class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'add_file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 4}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'add_file': forms.FileInput(attrs={'class': 'form-control'}),
            # 'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['due_date'].widget.attrs['min'] = datetime.date.today().isoformat()

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date.date() < datetime.date.today():
            raise ValidationError("Due date cannot be in the past.")
        return due_date

class TodoEditForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'is_completed', 'add_file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 4}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'add_file': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['due_date'].widget.attrs['min'] = datetime.date.today().isoformat()

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date.date() < datetime.date.today():
            raise ValidationError("Due date cannot be in the past.")
        return due_date

class TodoCompleteForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['is_completed', 'add_file']
        widgets = {
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'add_file': forms.FileInput(attrs={'class': 'form-control'}),
        }



class TodoAssignForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'assigned_to', 'add_file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 4}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
            'add_file': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['assigned_to'].queryset = User.objects.exclude(id=self.user.id)
        self.fields['due_date'].widget.attrs['min'] = datetime.date.today().isoformat()

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date.date() < datetime.date.today():
            raise ValidationError("Due date cannot be in the past.")
        return due_date

        


    



class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control'}))


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['first_name','last_name','username','email']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

    # def clean_password2(self):
    #     password = self.cleaned_data.get('password')
    #     password2 = self.cleaned_data.get('password2')
    #     if password and password2 and password != password2:
    #         raise ValidationError("Passwords don't match")
    #     return password2
