from django.forms import ModelForm, CharField, EmailField, URLField

from contacts.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = (
            'name',
            'company',
            'phone_number',
            'email_address',
            'linked_in_profile',
        )

    phone_number = CharField(required=False)
    email_address = EmailField(required=False)
    linked_in_profile = URLField(required=False)
