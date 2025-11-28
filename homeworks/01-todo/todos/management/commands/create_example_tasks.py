"""
Django management command to create example tasks for the TODO application.

Usage:
    python manage.py create_example_tasks
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from todos.models import Todo


class Command(BaseCommand):
    help = 'Creates example tasks for the TODO application'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear all existing tasks before creating examples',
        )

    def handle(self, *args, **options):
        if options['clear']:
            Todo.objects.all().delete()
            self.stdout.write(
                self.style.WARNING('All existing tasks have been deleted.')
            )

        # Create example tasks - Social life tasks for a 40s man with wife and son
        examples = [
            {
                'title': 'Plan family weekend trip',
                'description': 'Research and book activities for family weekend getaway with wife and son',
                'due_date': timezone.now() - timedelta(days=2),  # Overdue
                'is_resolved': False,
            },
            {
                'title': 'Attend son\'s soccer game',
                'description': 'Saturday morning game at 10 AM - bring camera and snacks',
                'due_date': timezone.now() + timedelta(days=2),
                'is_resolved': False,
            },
            {
                'title': 'Organize dinner party with friends',
                'description': 'Invite the old college friends for a dinner party at our place',
                'due_date': timezone.now() - timedelta(days=3),
                'is_resolved': True,  # Already done
            },
            {
                'title': 'Book restaurant for anniversary dinner',
                'description': 'Make reservation for our 15th wedding anniversary next month',
                'due_date': timezone.now() + timedelta(days=7),
                'is_resolved': False,
            },
            {
                'title': 'Call mom to check in',
                'description': 'Weekly phone call with mom - catch up on family news',
                'due_date': timezone.now() - timedelta(hours=5),  # Overdue
                'is_resolved': False,
            },
            {
                'title': 'Plan son\'s birthday party',
                'description': 'Organize birthday party - invite friends, order cake, plan activities',
                'due_date': timezone.now() + timedelta(days=5),
                'is_resolved': False,
            },
            {
                'title': 'Attend neighborhood BBQ',
                'description': 'Community BBQ event at the park - bring dish to share',
                'due_date': timezone.now() - timedelta(days=4),
                'is_resolved': True,  # Already done
            },
            {
                'title': 'Date night with wife',
                'description': 'Movie night or dinner - just the two of us',
                'due_date': timezone.now() + timedelta(days=1),
                'is_resolved': False,
            },
            {
                'title': 'Help son with school project',
                'description': 'Assist with science fair project due next week',
                'due_date': timezone.now() + timedelta(days=3),
                'is_resolved': False,
            },
            {
                'title': 'Organize family photos',
                'description': 'Sort through recent vacation photos and create album',
                'due_date': timezone.now() + timedelta(days=10),
                'is_resolved': False,
            },
            {
                'title': 'Attend work colleague\'s retirement party',
                'description': 'Celebrate long-time colleague\'s retirement this Friday evening',
                'due_date': timezone.now() + timedelta(days=2),
                'is_resolved': False,
            },
            {
                'title': 'Plan summer vacation',
                'description': 'Research and plan family summer vacation destinations',
                'due_date': timezone.now() + timedelta(days=14),
                'is_resolved': False,
            },
            {
                'title': 'Fix broken bike with son',
                'description': 'Teach son how to fix his bike - bonding time',
                'due_date': timezone.now() - timedelta(days=1),
                'is_resolved': True,
            },
            {
                'title': 'Meet friends for coffee',
                'description': 'Catch up with the guys at the local coffee shop',
                'due_date': timezone.now() + timedelta(days=4),
                'is_resolved': False,
            },
        ]

        created_count = 0
        for example in examples:
            todo, created = Todo.objects.get_or_create(
                title=example['title'],
                defaults={
                    'description': example['description'],
                    'due_date': example['due_date'],
                    'is_resolved': example['is_resolved'],
                }
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} example tasks!'
            )
        )
        
        # Display summary
        total = Todo.objects.count()
        resolved = Todo.objects.filter(is_resolved=True).count()
        pending = Todo.objects.filter(is_resolved=False).count()
        overdue = len([t for t in Todo.objects.filter(is_resolved=False) if t.is_overdue()])
        
        self.stdout.write('\n' + '='*50)
        self.stdout.write(self.style.SUCCESS('Task Summary:'))
        self.stdout.write(f'  Total Tasks: {total}')
        self.stdout.write(f'  Resolved: {resolved}')
        self.stdout.write(f'  Pending: {pending}')
        self.stdout.write(f'  Overdue: {overdue}')
        self.stdout.write('='*50)

