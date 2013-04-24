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

TRAINING_PERIOD_END = (
  ('Tue 09 April', _('Tuesday 9th April at 9.30am COMPLETE')),
  ('Wed 10 April', _('Wednesday 10th April at 9.30am COMPLETE')),
  ('Tue 16 April', _('Tuesday 16th April at 9.30am COMPLETE')),
  ('Wed 17 April', _('Wednesday 17th April at 9.30am COMPLETE')),
  ('Tue 23 April', _('Tuesday 23rd April at 9.30am')),
  ('Wed 24 April', _('Wednesday 24th April at 9.30am')),
  ('Keep Updated',
    _('I can\'t do any of the above, please send me the End of Year '
      'information')),
)

TRAINING_GROUP = (
  ('Wed 01 May', _('Wednesday 1st May at 9.30am')),
  ('Wed 22 May', _('Wednesday 22nd May at 9.30am')),
  ('Wed 05 June', _('Wednesday 5th June at 9.30am')),
  ('Keep Updated',
    _('I can\'t do any of the above, please send me the Group information')),
)

TRAINING_NOT_PAID = (
  ('Wed 01 May', _('Wednesday 8th May at 9.30am')),
  ('Wed 22 May', _('Wednesday 29th May at 9.30am')),
  ('Wed 05 June', _('Wednesday 12th June at 9.30am')),
  ('Keep Updated',
    _('I can\'t do any of the above, please send me the Who\'s Not Paid'
      ' information')),
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
      label=_("Telephone"), max_length=15, required=False,
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

class ContactTraining_PeriodEnd(forms.Form):
    name = forms.CharField(
      label=_("Name"), max_length=255, required=True,
    )
    email = forms.EmailField(
      label=_("Email Address"), required=True,
    )
    organisation = forms.CharField(
      label=_("Organisation"), max_length=300, required=False,
    )
    telephone = forms.CharField(
      label=_("Telephone"), max_length=15, required=False,
    )
    training = forms.MultipleChoiceField(
      label=_("Training Date"), choices=TRAINING_PERIOD_END, required=False,
      widget=CheckboxSelectMultiple,
    )

    EMAIL_RECIPIENTS = (
      'training@talktopebble.co.uk',
    )
    def save(self):
      """Send out the email.
      """
      name = self.cleaned_data['name']
      email = self.cleaned_data['email']
      organisation = self.cleaned_data['organisation']
      telephone = self.cleaned_data['telephone']

      training = self.cleaned_data['training']

      session = "Period End"

      send_mail(
        'Training - Webinar',
        get_template('core/training').render(
          Context({

            'name': name,
            'email': email,
            'organisation': organisation,
            'telephone': telephone,
            'training': training,
            'session' : session,
          })
        ),
        'mypebble',
        self.EMAIL_RECIPIENTS,
        fail_silently = True
      )

    def form_title(self):
      """Title of form
      """
      return _( 'Training Webinar - End of Year Overview')

    def form_text(self):
      """Prints out the custom text to be displayed on the form.
      """
      return [_(
                'This FREE online training session gives you an overview of your End of Year procedures.'
                ' The session will take about 10 minutes - the perfect way to help you make the most of your '
                'Fund Manager software.'),
                _('Please complete the form below and select which date(s) you are available to join a free '
                'online training session. Places are limited to 8 schools for each online session so you may '
                'wish to choose more than one date. We\'ll be in touch shortly.'
                )]

    def form_text_details(self):
      """Prints out the custom text to be displayed on the form.
      """
      return _(
                'We will send you an invitation to join our FREE WebEx training, so please watch out for it. '
                'The email will be sent from Cisco Systems. If you do not receive this invitation please let us '
                'know before the training is due to start. You will need to follow the instructions and log in '
                'to the session from the email approximately 10 to 15 minutes before the stated time of the Webinar. '
                'Just before the training is due to start please dial the conference telephone number supplied in the '
                'email or use your audio on your PC or laptop to join the WebEx training. We will start promptly at '
                'the stated time. '
                'More free online training sessions will be scheduled later in the year.')


class ContactTraining_Group(forms.Form):
    name = forms.CharField(
      label=_("Name"), max_length=255, required=True,
    )
    email = forms.EmailField(
      label=_("Email Address"), required=True,
    )
    organisation = forms.CharField(
      label=_("Organisation"), max_length=300, required=False,
    )
    telephone = forms.CharField(
      label=_("Telephone"), max_length=15, required=False,
    )
    training = forms.MultipleChoiceField(
      label=_("Training Date"), choices=TRAINING_GROUP, required=False,
      widget=CheckboxSelectMultiple,
    )
    EMAIL_RECIPIENTS = (
      'training@talktopebble.co.uk',
    )
    def save(self):
      """Send out the email.
      """
      name = self.cleaned_data['name']
      email = self.cleaned_data['email']
      organisation = self.cleaned_data['organisation']
      telephone = self.cleaned_data['telephone']

      training = self.cleaned_data['training']

      session = "Groups"


      send_mail(
      'Training - Webinar',
      get_template('core/training').render(
      Context({
      'name': name,
      'email': email,
      'organisation': organisation,
      'telephone': telephone,

      'training': training,
      'session' : session,
      })
      ),
      'mypebble',
      self.EMAIL_RECIPIENTS,
      fail_silently = True
    )

    def form_title(self):
      """Title of form
      """
      return _( 'Training Webinar - Groups Overview')

    def form_text(self):
      """Prints out the custom text to be displayed on the form.
      """
      return [_(
          'This FREE online training session gives you an overview of the Groups function.'
          'The session will take about 10 minutes the perfect way to help you make the '
          'most of your Fund Manager software.'
        ),
        _(
          'Please complete the form below and select which date(s) you are available '
          'to join a free online training session. Places are limited to 8 schools '
          'for each online session so you may wish to choose more than one date. '
          'We\'ll be in touch shortly.'
        )
      ]

    def form_text_details(self):
      """Prints out the custom text to be displayed on the form.
      """
      return _(
        'We will send you an invitation to join our FREE WebEx training, so please '
        'watch out for it. The email will be sent from Cisco Systems. If you do '
        'not receive this invitation please let us know before the training is due '
        'to start. You will need to follow the instructions and log in to the session '
        'from the email approximately 10 to 15 minutes before the stated time of '
        'the Webinar. Just before the training is due to start please dial the '
        'conference telephone number supplied in the email or use your audio on your '
        'PC or laptop to join the WebEx training. We will start promptly at the stated '
        'time.'
        'More free online training sessions will be scheduled later in the year.'
      )

class ContactTraining_Not_Paid(forms.Form):
    name = forms.CharField(
      label=_("Name"), max_length=255, required=True,
    )
    email = forms.EmailField(
      label=_("Email Address"), required=True,
    )
    organisation = forms.CharField(
      label=_("Organisation"), max_length=300, required=False,
    )
    telephone = forms.CharField(
      label=_("Telephone"), max_length=15, required=False,
    )
    training = forms.MultipleChoiceField(
      label=_("Training Date"), choices=TRAINING_NOT_PAID, required=False,
      widget=CheckboxSelectMultiple,
    )
    EMAIL_RECIPIENTS = (
      'training@talktopebble.co.uk',
    )
    def save(self):
      """Send out the email.
      """
      name = self.cleaned_data['name']
      email = self.cleaned_data['email']
      organisation = self.cleaned_data['organisation']
      telephone = self.cleaned_data['telephone']

      training = self.cleaned_data['training']
      session = "Who\'s not Paid"

      send_mail(
      'Training - Webinar',
      get_template('core/training').render(
      Context({
      'name': name,
      'email': email,
      'organisation': organisation,
      'telephone': telephone,

      'training': training,
      'session' : session,
      })
      ),
      'mypebble',
      self.EMAIL_RECIPIENTS,
      fail_silently = True
    )

    def form_title(self):
      """Title of form
      """
      return _( 'Training Webinar - Who\'s Not Paid Overview')

    def form_text(self):
      """Prints out the custom text to be displayed on the form.
      """
      return [_(
        'This FREE online training session gives you an overview of the '
        'Who\'s Not Paid report.  The session will take about 10 minutes'
        ' the perfect way to help you make the most of your Fund Manager software.'),
        _(
        'Please complete the form below and select which date(s) you are available '
        'to join a free online training session. Places are limited to 8 schools for '
        'each online session so you may wish to choose more than one date. '
        'We\'ll be in touch shortly.'
      )]

    def form_text_details(self):
      """Prints out the custom text to be displayed on the form.
      """
      return _(
        'We will send you an invitation to join our FREE WebEx training, so please '
        'watch out for it. The email will be sent from Cisco Systems. If you do not '
        'receive this invitation please let us know before the training is due to start. '
        'You will need to follow the instructions and log in to the session from the '
        'email approximately 10 to 15 minutes before the stated time of the Webinar. '
        'Just before the training is due to start please dial the conference telephone '
        'number supplied in the email or use your audio on your PC or laptop to join the '
        'WebEx training. We will start promptly at the stated time. '
        'More free online training sessions will be scheduled later in the year.'
      )
