from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_names(name):
    if len(name) < 6:
        raise ValidationError(
            _("This field must be greater then 6 characters long")
        )

def validate_unique_name(value, model_class, field_name='name'):
    """
    Generalized validator to check if a value is unique for a given model and field.
    
    :param value: The value to be checked.
    :param model_class: The Django model class where the uniqueness needs to be checked.
    :param field_name: The field name on which uniqueness is checked. Defaults to 'name'.
    """
    normalized_value = value.lower()
    filter_kwargs = {f"{field_name}__iexact": normalized_value}
    if model_class.objects.filter(**filter_kwargs).exists():
        raise ValidationError(
            _('The %(field_name)s "%(value)s" is already in use.'),
            params={'field_name': field_name, 'value': value},
        )

