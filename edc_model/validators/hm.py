from django.core.validators import RegexValidator

"""
expect 1h20m, 11h5m, etc
"""

hm_validator = RegexValidator(  # noqa
    "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
    message="Invalid format. Expected something like 1h20m, 11h5m, etc",
)
