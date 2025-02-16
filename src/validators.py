from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_names(name):
    if len(name) < 6:
        raise ValidationError(
            _("This field must be greater then 6 characters long")
        )

