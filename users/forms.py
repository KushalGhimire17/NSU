from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    
    class Meta:
        model = Member
        fields = ['username', 'mobile_number', 'province', 'district', 'campus', 'current_role', 'municipality', 'ward' ]
        # fields = '__all__'

