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

        # Create example tasks
        examples = [
            {
                'title': 'Complete Django TODO application',
                'description': 'Finish building the TODO app with all CRUD operations, filtering, and statistics',
                'due_date': timezone.now() - timedelta(days=1),  # Overdue
                'is_resolved': False,
            },
            {
                'title': 'Review project documentation',
                'description': 'Read through README.md and TESTING.md files',
                'due_date': timezone.now() + timedelta(days=2),
                'is_resolved': False,
            },
            {
                'title': 'Set up development environment',
                'description': 'Install Django, create virtual environment, and configure project settings',
                'due_date': timezone.now() - timedelta(days=3),
                'is_resolved': True,  # Already done
            },
            {
                'title': 'Learn Django ORM',
                'description': 'Study Django models, queries, and database relationships',
                'due_date': timezone.now() + timedelta(days=7),
                'is_resolved': False,
            },
            {
                'title': 'Push code to GitHub',
                'description': 'Upload the project to the GitHub repository',
                'due_date': timezone.now() - timedelta(hours=5),  # Overdue
                'is_resolved': False,
            },
            {
                'title': 'Write unit tests',
                'description': 'Create test cases for models, views, and forms',
                'due_date': timezone.now() + timedelta(days=5),
                'is_resolved': False,
            },
            {
                'title': 'Design database schema',
                'description': 'Plan the database structure for the TODO application',
                'due_date': timezone.now() - timedelta(days=5),
                'is_resolved': True,  # Already done
            },
            {
                'title': 'Add Facebook blue theme',
                'description': 'Update the UI with Facebook blue color scheme',
                'due_date': timezone.now(),
                'is_resolved': True,
            },
            {
                'title': 'Implement list and grid views',
                'description': 'Add toggle between list and grid view modes',
                'due_date': timezone.now(),
                'is_resolved': True,
            },
            {
                'title': 'Add task statistics',
                'description': 'Display counts for total, resolved, pending, and overdue tasks',
                'due_date': timezone.now(),
                'is_resolved': True,
            },
            {
                'title': 'Fix authentication issues',
                'description': 'Resolve GitHub push authentication problems',
                'due_date': timezone.now() + timedelta(hours=2),
                'is_resolved': False,
            },
            {
                'title': 'Create user documentation',
                'description': 'Write comprehensive README with setup instructions',
                'due_date': timezone.now() + timedelta(days=1),
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

