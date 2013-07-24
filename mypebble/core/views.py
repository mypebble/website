from django.shortcuts import redirect, render

from mypebble.core.forms import ContactForm, ContactTraining_PeriodEnd, ContactTraining_Group, ContactTraining_Not_Paid, ContactTraining_New_Features

FORMS = {
  'general': ContactForm,
  'training_period_end': ContactTraining_PeriodEnd,
  #'training_group': ContactTraining_Group,
  #'training_not_paid': ContactTraining_Not_Paid,
  #'training_new_features': ContactTraining_New_Features,
}


def _get_form(form_type):
  """Gets the form based on the enquiry type.
  """
  return FORMS[form_type]

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
