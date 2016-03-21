from optparse import make_option

from django.core.management.base import BaseCommand
from django.core.management.base import NoArgsCommand
from django.core.exceptions import ObjectDoesNotExist

from apps.task_1.models import Document


class Command(BaseCommand):
    help = 'Gets all users with education'

    option_list = NoArgsCommand.option_list + (
        make_option(
            '--education', '-e', action='store', default=None,
            dest='education', help='Education type.'
        ),
    )

    def handle(self, *args, **options):
        education = options.get('education')
        if education:
            try:
                doc = Document.objects.get(education=education)
            except ObjectDoesNotExist:
                return 'Education type not found in DB'
            print 'Education:%s' % education
            print 'Users:'
            for user in doc.people_id.all():
                print user.name

        else:
            print 'Please use -e tag with education type to see users'
