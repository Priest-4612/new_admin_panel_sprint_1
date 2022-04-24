from dataclasses import fields

from psycopg2.extras import execute_batch


class PostgresSaver(object):
    def __init__(self, connection):
        self._connection = connection

    def save_data(self, loaded_data, dataclass_dict, save_rows_size=100):
        if not loaded_data:
            return
        table = list(loaded_data.keys())[0]
        tuple_data = [
            tuple(row.__dict__.values())
            for row in loaded_data[table]
        ]
        fields_dataclasses = [
            field.name
            for field in fields(dataclass_dict[table])
        ]
        join_fields = (', ').join(fields_dataclasses)
        using_attributes = '%s, ' * (len(fields_dataclasses) - 1) + '%s'
        query = """INSERT INTO {table} ({fields}) VALUES ({values})
                   ON CONFLICT (id) DO NOTHING;""".format(
            table=table,
            fields=join_fields,
            values=using_attributes,
        )
        execute_batch(
            self._connection.cursor(),
            query,
            tuple_data,
            page_size=save_rows_size,
        )
        self._connection.commit()
