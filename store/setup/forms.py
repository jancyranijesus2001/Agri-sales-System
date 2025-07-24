from django import forms
from store.models.waste import Waste

class WasteForm(forms.ModelForm):
    class Meta:
        model = Waste
        fields = ['name', 'mobile', 'waste_category', 'total_kg', 'image']
