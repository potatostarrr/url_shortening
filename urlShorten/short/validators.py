
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
def urlValidator(url):
    urlvalidator = URLValidator()
    valid = False
    try:
        urlvalidator(url)
        valid |= True
    except:
        pass
    try:
        urlvalidator('http://'+url)
        valid |= True
    except:
        pass
    if not valid:
        raise ValidationError('Invalid URL!')
    return url
