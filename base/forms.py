from django import forms
from .models import Employee, Education


class EmployeeForm(forms.ModelForm):
    SKILLS_CHOICES = [
        ("python", "Python"),
        ("javascript", "JavaScript"),
        ("go", "Go"),
        ("rust", "Rust"),
    ]

    gender = forms.ChoiceField(choices=Employee.GENDER.items())
    state = forms.ChoiceField(choices=Employee.STATE.items())
    skills = forms.MultipleChoiceField(
        choices=SKILLS_CHOICES, widget=forms.CheckboxSelectMultiple
    )
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Employee
        fields = [
            "name",
            "date_of_birth",
            "gender",
            "email",
            "state",
            "address",
            "skills",
        ]


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["edu_type", "description", "grad_year"]
