from dataclasses import fields


class SQLiteLoader(object):
    def __init__(self, cursor, load_rows_size=100):
        self._cursor = cursor

    def load_data(self, table, dataclass_dict, load_rows_size=1):
        fields_dataclasses = [
            field.name
            for field in fields(dataclass_dict[table])
        ]
        join_fields = (', ').join(fields_dataclasses)
        query = 'SELECT {fields} FROM {table};'.format(
            fields=join_fields,
            table=table,
        )
        self._cursor.execute(query)
        while True:
            loaded_data = self._cursor.fetchmany(load_rows_size)

            if not loaded_data:
                break

            yield {
                table: [
                    dataclass_dict[table](*row)
                    for row in loaded_data
                ],
            }
