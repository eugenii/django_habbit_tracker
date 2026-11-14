from django import forms

from .models import Habit


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        exclude = 'author'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'например: каждый день...'}),
        }

    def clean_time_reuqired(self):
        time = self.cleaned_data['time_required']
        if time > 120:
            raise forms.ValidationError('Время выполнения не может быть больше 120 минут')
        if time < 1:
            raise forms.ValidationError('Не меньше минуты!')
        return time