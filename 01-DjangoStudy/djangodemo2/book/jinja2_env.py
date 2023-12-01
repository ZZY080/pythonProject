from jinja2 import  Environment
from django.template.defaultfilters import  date

def environment(**options):
    env=Environment(**options)
    env.globals.update({
        "date":date
    })
    return env
