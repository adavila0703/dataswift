from models import Model

# Model.table(
#     'db.sqlite3',
#     'new_table',
#     Model.IntField('num', primary_key=True),
#     Model.CharField('test', max_length=50),
#     Model.BoolField('boolean'),
#     Model.DateField('date'),
#     Model.DateTimeField('datetime')
#     )

Model.table(
    'db.sqlite3',
    'new',
    Model.CharField(field_name='hi', max_length=10),
    Model.CharField(field_name='wow', max_length=10)
    )


    