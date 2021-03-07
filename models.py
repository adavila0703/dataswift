import sqlite3
import os

'''
    dataswift-ORM
'''

# def database(db):

class Table():
    def create_table(schema) -> None:
        schema_len = len(schema) - 1
        concat_schema = ''

        for num, field in enumerate(schema):
            if num == schema_len:
                str_replace = field.replace(",", " ")
                concat_schema += ''.join(str_replace)
            else:
                concat_schema += ''.join(field)

        Query.exe_query(f'CREATE TABLE {Model.table_name}({concat_schema});')
        return None

    def table_schema_check(table_name):
        tables = Query.exe_query(f"SELECT name FROM sqlite_master WHERE type='table'")
        fields = Query.exe_query(f"PRAGMA table_info({table_name})")
        print(Model.fields, fields.fetchall())
        for table in tables:
            if (table_name in table) == True and Model.fields == fields:
                raise ValueError(f'{table_name} already exists')



class Query():
    connection = None
    cursor = None
    data = None
    def exe_query(query) -> None:
        Query.connection = sqlite3.connect(Model.database)
        Query.cursor = Query.connection.cursor()
        try:
            Query.data = Query.cursor.execute(query)
            Query.connection.commit()
        except sqlite3.OperationalError:
            pass
        return Query.data




class Model():
    database = ''
    table_name = ''
    fields_query = []
    fields = []
    row_count = 0

    def table(database, table_name, *args, **kargs):
        Model.database = database
        Model.table_name = table_name
        Table.table_schema_check(table_name)
        Table.create_table(Model.fields_query)

    def test():
        pass

    
    def CharField(field_name, max_length):
        Model.fields.append((Model.row_count, field_name, F'VARCHAR({max_length})', 0, None, 0))
        Model.fields_query.append(field_name + ' ' + f'VARCHAR({max_length}), ')
        Model.row_count += 1

    def IntField(field_name, primary_key=False):
        if primary_key == True:
            Model.fields_query.append(field_name + ' ' + f'INTEGER PRIMARY KEY, ')
        else:
            Model.fields_query.append(field_name + ' ' + f'INTEGER, ')

    def BoolField(field_name):
        Model.fields_query.append(field_name + ' ' + f'BOOL, ')

    def DateField(field_name):
        Model.fields_query.append(field_name + ' ' + f'DATE, ')

    def DateTimeField(field_name):
        Model.fields_query.append(field_name + ' ' + f'DATETIME, ')


    


