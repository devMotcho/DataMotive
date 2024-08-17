import pint
from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError


fields_not_in_pint = ['Unit', 'unit', 'uni']

def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()

    if value not in fields_not_in_pint:
        try:
            single_unit = ureg[value]
        except UndefinedUnitError as e:
            raise ValidationError(f"'{value}' is not a valid unit of measure.")
        except:
            raise ValidationError(f"'{value}' is invalid. Unkown error.")
