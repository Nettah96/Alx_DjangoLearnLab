from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Create default groups and assign permissions'

    def handle(self, *args, **kwargs):
        permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, perms in permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for codename in perms:
                perm = Permission.objects.get(codename=codename)
                group.permissions.add(perm)
            self.stdout.write(self.style.SUCCESS(f"{group_name} group updated."))
