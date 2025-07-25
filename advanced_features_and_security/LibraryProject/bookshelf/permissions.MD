# Permissions and Groups Setup

## Custom Permissions

Defined on the `Book` model in `bookshelf/models.py`:

- can_view — View book records
- can_create — Create new books
- can_edit — Edit existing books
- can_delete — Delete books

## Groups

| Group Name | Permissions Assigned                     |
|------------|-------------------------------------------|
| Viewers    | can_view                                 |
| Editors    | can_view, can_create, can_edit           |
| Admins     | can_view, can_create, can_edit, can_delete |

## View Protection

Views in `bookshelf/views.py` are decorated with `@permission_required` to enforce access control.
