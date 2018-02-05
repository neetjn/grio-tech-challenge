import os
from peewee import *
from playhouse.migrate import *

from grio.db import *


migrator = PostgresqlMigrator(client)

# migration from 2-4-18
# - change field name from 'user_id' to 'id'

if os.environ.get('MIGRATION_1'):
    migrate(
        migrator.rename_column('person', 'user_id', 'id')
    )

# migration from 2-4-18
# - add 'deleted' and 'is_deleted' fields to person

if os.environ.get('MIGRATION_2'):
    is_deleted_field = BooleanField(default=False)
    deleted_field = DateTimeField(default=None, null=True)
    migrate(
        migrator.add_column('person', 'is_deleted', is_deleted_field),
        migrator.add_column('person', 'deleted', deleted_field)
    )
