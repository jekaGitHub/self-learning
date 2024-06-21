from django import forms

from checking.models import Answer


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class AnswerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
