from django.utils.translation import ugettext_lazy as _
from django import forms

from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

INTERESTED = (
  ('FM', _('Fund Manager')),
  ('SFF', _('School Fund Finder')),
)

WOULD_LIKE = (
  ('demo', _('Online Demo')),
  ('onsite/training', _('On-site or Online Training')),
  ('other', _('Other Enquiry')),
)

TRAINING_PERIOD_END = (
  ('Tue09', _('Tuesday 9th April at 9.30am')),
  ('Wed10', _('Wednesday 10th April at 9.30am')),
  ('Tue16', _('Tuesday 16th April at 9.30am')),
  ('Wed17', _('Wednesday 17th April at 9.30am')),
  ('Tue23', _('Tuesday 23rd April at 9.30am')),
  ('Wed24', _('Wednesday 24th April at 9.30am')),
  ('other', _('I cant do any of the above, please send me the End of Year information')),
)

TRAINING_GROUP = (
  ('Wed01', _('Wednesday 1st May at 9.30am')),
  ('Wed22', _('Wednesday 22nd May at 9.30am')),
  ('Wed05', _('Wednesday 5th June at 9.30am')),
  ('other', _('I cant do any of the above, please send me the Group information')),
)

TRAINING_NOT_PAID = (
  ('Wed01', _('Wednesday 8th May at 9.30am')),
  ('Wed22', _('Wednesday 29th May at 9.30am')),
  ('Wed05', _('Wednesday 12th June at 9.30am')),
  ('other', _('I cant do any of the above, please send me the Whos Not Paid information')),
)


class ContactForm(forms.Form):

    name = forms.CharField(
      label=_("Name"), max_length=255, required = True,
    )
    email = forms.EmailField(
      label=_("Email Address"), required = True,
    )
    organisation = forms.CharField(
      label=_("Organisation"), max_length=300, required = False,
    )
    postcode = forms.CharField(
      label=_("Postcode"), max_length=10, required = False, 
    )
    telephone = forms.CharField(
      label=_("Telephone"), max_length=15, required = False,
    )
    interested = forms.MultipleChoiceField(
      widget=CheckboxSelectMultiple,
      label=_("I'm interested in"), choices=INTERESTED, required = False,
    )
    wouldlike = forms.MultipleChoiceField(
      widget=CheckboxSelectMultiple,
      label=_("I would like"), choices=WOULD_LIKE, required = False,
    )
    message = forms.CharField(
      widget=forms.Textarea,
      label=_("Message"), max_length=300, required = False,
    )
    
    def save(self):
      """Send out the email.
      """

class ContactTraining_PeriodEnd(forms.Form):
    name = forms.CharField(
      label=_("Name"), max_length=255, required = True,
    )
    email = forms.EmailField(
      label=_("Email address"), required = True,
    )
    organisation = forms.CharField(
      label=_("Organisation"), max_length=300, required = False,
    )    
    telephone = forms.CharField(
      label=_("Telephone"), max_length=15, required=False,
    )
    training = forms.MultipleChoiceField(
      label=_("Training Date"), choices=TRAINING_PERIOD_END, required=False,
      widget=CheckboxSelectMultiple,
    )

class ContactTraining_Group(forms.Form):
    name = forms.CharField(
      label=_("Name"), max_length=255, required = True,
    )
    email = forms.EmailField(
      label=_("Email address"), required = True,
    )
    organisation = forms.CharField(
      label=_("Organisation"), max_length=300, required = False,
    )    
    telephone = forms.CharField(
      label=_("Telephone"), max_length=15, required=False,
    )
    training = forms.MultipleChoiceField(
      label=_("Training Date"), choices=TRAINING_GROUP, required=False,
      widget=CheckboxSelectMultiple,
    )
    
class ContactTraining_Not_Paid(forms.Form):
    name = forms.CharField(
      label=_("Name"), max_length=255, required = True,
    )
    email = forms.EmailField(
      label=_("Email address"), required = True,
    )
    organisation = forms.CharField(
      label=_("Organisation"), max_length=300, required = False,
    )    
    telephone = forms.CharField(
      label=_("Telephone"), max_length=15, required=False,
    )
    training = forms.MultipleChoiceField(
      label=_("Training Date"), choices=TRAINING_NOT_PAID, required=False,
      widget=CheckboxSelectMultiple,
    )
