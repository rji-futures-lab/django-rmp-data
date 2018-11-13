from django import forms

class FacilitySearch(forms.Form):
    facility_name = forms.CharField()
    parent_company = forms.CharField()

    def clean(self):
        cleaned_data = super(facility_search, self).clean()
        facility_name = cleaned_data.get('facility_name')
        parent_company = cleaned_data.get('email')
        if not facility_name and not parent_company:
            raise forms.ValidationError('Please submit a search term.')
