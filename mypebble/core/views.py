from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from mypebble.core.forms import ContactForm

FORMS = {
  'general': ContactForm,
}


def _get_form(form_type):
  """Gets the form based on the enquiry type.
  """
  return FORMS[form_type]

@csrf_exempt
def contact(request, form_type='general'):
    form_class = _get_form(form_type)

    if request.method == 'POST': # If the form has been submitted...
        form = form_class(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()

            return render(request, 'core/form_sent.html',
              {'form': form}
            )
    else:
        form = form_class() # An unbound form

    return render(request, 'core/contact.html', {
        'form': form
    })
