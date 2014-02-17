from django.utils.translation import ugettext_lazy as _
from django import forms

from django.forms.widgets import CheckboxSelectMultiple

from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context

INTERESTED = (
  ('FM', _('Fund Manager')),
  ('SFF', _('School Fund Finder')),
)

WOULD_LIKE = (
  ('demo', _('Online Demo')),
  ('onsite/training', _('On-site or Online Training')),
  ('other', _('Other Enquiry')),
)

class ContactForm(forms.Form):

    name = forms.CharField(
      label=_("Name"), max_length=255, required=True,
    )
    email = forms.EmailField(
      label=_("Email Address"), required=True,
    )
    organisation = forms.CharField(
      label=_("Organisation"), max_length=300, required=False,
    )
    postcode = forms.CharField(
      label=_("Postcode"), max_length=10, required=False,
    )
    telephone = forms.CharField(
      label=_("Telephone"), max_length=25, required=True,
    )
    interested = forms.MultipleChoiceField(
      widget=CheckboxSelectMultiple,
      label=_("I'm interested in"), choices=INTERESTED, required=False,
    )
    wouldlike = forms.MultipleChoiceField(
      widget=CheckboxSelectMultiple,
      label=_("I would like"), choices=WOULD_LIKE, required=False,
    )
    message = forms.CharField(
      widget=forms.Textarea,
      label=_("Message"), max_length=300, required=False,
    )

    EMAIL_RECIPIENTS = (
      'info@mypebble.co.uk',
    )
    def save(self):
      """Send out the email.
      """
      name = self.cleaned_data['name']
      email = self.cleaned_data['email']
      organisation = self.cleaned_data['organisation']
      postcode = self.cleaned_data['postcode']
      telephone = self.cleaned_data['telephone']

      interested = self.cleaned_data['interested']
      wouldlike = self.cleaned_data['wouldlike']
      message = self.cleaned_data['message']

      send_mail(
        'Website Contact Form',
       get_template('core/enquiry').render(
          Context({
            'name': name,
            'email': email,
            'organisation': organisation,
            'postcode': postcode,
            'telephone': telephone,

            'interested': interested,
            'wouldlike': wouldlike,
            'message': message,
            })
        ),
        'mypebble',
        self.EMAIL_RECIPIENTS,
        fail_silently = True
      )


    def form_title(self):
      """Title of form
      """
      return _( 'Contact Us')

    def form_text(self):
      """Prints out the custom text to be displayed on the form.
      """
      return [_( 'As well as software, we also provide real people '
                'on hand to offer all the advice and support you '
                'need. No automated telephone lines - just a '
                'dedicated team of people who know the products inside out.'),
                _('Please complete the form below. We\'ll be in touch shortly.')
                ]
