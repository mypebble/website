import logging
import smtplib

from django.core.mail import send_mail
from django.core.exceptions import DoesNotExist
from django.dispatch import receiver
from django.template import Context, loader

from forms_builder.forms.signals import form_valid


log = logging.getLogger(__name__)


EMAIL_SENDERS = {
    'enquiries': u'www+enquiries@mypebble.co.uk'
}


def get_checked(entry):
    """Get the checked fields from the form(s).
    """
    interested_field = entry.form.fields.filter(slug='im_interseted_in')
    if interested_field.exists():
        interested_field = interested_field.get()
        interested = entry.fields.get(field_id=interested_field.pk).value
        yield interested

    training_field = entry.form.fields.filter(slug='training')
    if training_field.exists():
        yield 'Training'

    documentation_field = entry.form.fields.filter(slug='i_would_like')
    if documentation_field.exists():
        documentation_field = documentation_field.get()
        documentation = entry.fields.get(field_id=documentation_field.pk).value
        yield documentation


@receiver(form_valid)
def send_email(sender=None, form=None, entry=None, **kwargs):
    if entry is None:
        return

    subject = u'New Enquiry'
    from_ = EMAIL_SENDERS['enquiries']
    to = (u'info@mypebble.co.uk', )

    message_template = loader.get_template('core/enquiry')

    name_field = entry.form.fields.get(slug='name')
    name = entry.fields.get(field_id=name_field.pk).value

    email_field = entry.form.fields.get(slug='email_address')
    email_address = entry.fields.get(field_id=email_field.pk).value

    org_field = entry.form.fields.filter(slug='school_or_organisation')
    if not org_field.exists():
        org_field = entry.form.fields.get(slug='school')
    else:
        org_field = org_field.get()
    org = entry.fields.get(field_id=org_field.pk).value

    try:
        postcode_field = entry.form.fields.get(label='Postcode')
    except DoesNotExist:
        postcode = ''
    else:
        postcode = entry.fields.get(field_id=postcode_field.pk).value

    try:
        telephone_field = entry.form.fields.get(label='Telephone')
    except DoesNotExist:
        telephone = ''
    else:
        telephone = entry.fields.get(field_id=telephone_field.pk).value

    extra_field = entry.form.fields.filter(slug='add_a_message')
    if extra_field.exists():
        extra_field = extra_field.get()
        extra = entry.fields.get(field_id=extra_field.pk).value
    else:
        extra = None

    available = entry.form.fields.filter(slug='next_available_date')
    if available.exists():
        available = available.get()
    else:
        available = None

    context = Context({
        'name': name,
        'email_address': email_address,
        'organisation': org,
        'postcode': postcode,
        'telephone': telephone,
        'checked': [c for c in get_checked(entry)],
        'extra': extra,
        'available': available,
    })

    message = message_template.render(context)

    try:
        send_mail(subject, message, from_, to)
    except smtplib.SMTPException:
        log.error(
            u'Email could not send.\nContext={context}'.format(context=context)
        )
        raise
