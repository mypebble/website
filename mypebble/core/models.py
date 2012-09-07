from django.core.mail import send_mail
from django.dispatch import receiver
from django.template import Context, loader

from forms_build.forms.signals import form_valid


EMAIL_SENDERS = {
    'enquiries': u'www+enquiries@mypebble.co.uk'
}


def get_checked(entry):
    interested = entry.fields.get(field__label="I'm interested in").value
    documentation = entry.fields.get(field__label='I would like').value
    for i in interested:
        yield i
    for d in documentation:
        yield d


@receiver(form_valid)
def send_email(sender=None, form=None, entry=None, **kwargs):
    if entry is None:
        return

    subject = u'New Enquiry'
    from_ = EMAIL_SENDERS['enquiries']
    to = (u'info@mypebble.co.uk', u'scw@talktopebble.co.uk')

    message_template = loader.get_template('core/enquiry')

    name = entry.fields.get(field__label='Name').value
    email_address = entry.fields.get(field__label='Email Address').value
    organisation = entry.fields.get(field__label='School or Organisation').value
    postcode = entry.fields.get(field__label='Postcode').value
    telephone = entry.fields.get(field__label='Telephone').value
    extra = entry.fields.get(field__label='Add a message').value

    context = Context({
        'name': name,
        'email_address': email_address,
        'organisation': organisation,
        'postcode': postcode,
        'telephone': telephone,
        'checked': [c for c in get_checked(entry)],
        'extra': extra,
    })

    message = message_template.render(context)

    send_mail(subject, message, from_, to)
