from django import forms
from .models import ProbChoice, ProbRadioSelect


class NameForm(forms.Form):
    check_box_input = forms.BooleanField(
        label='Да или Нет', required=False)
    char_field = forms.CharField(
        label='Your name', max_length=100, initial='Input you name is here')
    choice_field = forms.ChoiceField(choices=ProbChoice.THE_CHOICE)
    like = forms.ChoiceField(label='Сделайте выбор',
                             choices=ProbRadioSelect.THE_CHOICE, widget=forms.RadioSelect)
