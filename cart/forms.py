from django import forms


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1, max_value=9,
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
