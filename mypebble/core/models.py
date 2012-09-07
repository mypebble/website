import logging
import smtplib

from django.core.mail import send_mail
from django.dispatch import receiver
from django.template import Context, loader

from forms_builder.forms.signals import form_valid


log = logging.getLogger(__name__)


EMAIL_SENDERS = {
    'enquiries': u'www+enquiries@mypebble.co.uk'
}


def get_checked(entry):
    interested_field = entry.form.fields.get(slug='im_interseted_in')
    interested = entry.fields.get(field_id=interested_field.pk).value

    yield interested

    documentation_field = entry.form.fields.get(slug='i_would_like')
    documentation = entry.fields.get(field_id=documentation_field.pk).value

    yield documentation


@receiver(form_valid)
def send_email(sender=None, form=None, entry=None, **kwargs):
    if entry is None:
        return

    subject = u'New Enquiry'
    from_ = EMAIL_SENDERS['enquiries']
    to = (u'info@mypebble.co.uk', u'scw@talktopebble.co.uk')

    message_template = loader.get_template('core/enquiry')

    name_field = entry.form.fields.get(slug='name')
    name = entry.fields.get(field_id=name_field.pk).value

    email_field = entry.form.fields.get(slug='email_address')
    email_address = entry.fields.get(field_id=email_field.pk).value

    org_field = entry.form.fields.get(slug='school_or_organisation')
    org = entry.fields.get(field_id=org_field.pk).value

    postcode_field = entry.form.fields.get(label='Postcode')
    postcode = entry.fields.get(field_id=postcode_field.pk).value

    telephone_field = entry.form.fields.get(slug='telephone')
    telephone = entry.fields.get(field_id=telephone_field.pk).value

    extra_field = entry.form.fields.get(slug='add_a_message')
    extra = entry.fields.get(field_id=extra_field.pk).value

    context = Context({
        'name': name,
        'email_address': email_address,
        'organisation': org,
        'postcode': postcode,
        'telephone': telephone,
        'checked': [c for c in get_checked(entry)],
        'extra': extra,
    })

    message = message_template.render(context)

    try:
        send_mail(subject, message, from_, to)
    except smtplib.SMTPException:
        log.info(
            u'Email could not send.\nContext={context}'.format(context=context)
        )
        raise
