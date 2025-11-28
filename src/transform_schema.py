def transform(columns_info, constraints_info):
    schema = {}

    for table, column, dtype, nullable, max_len in columns_info:
        if table not in schema:
            schema[table] = {
                "columns": [],
                "constraints": {
                    "primary_key": [],
                    "foreign_keys": [],
                    "unique": []
                }
            }

        schema[table]["columns"].append({
            "column": column,
            "type": dtype,
            "nullable": nullable,
            "max_length": max_len
        })

    for table, ctype, column, foreign_table, foreign_column in constraints_info:

        if table not in schema:
            continue  # should not happen but safe

        if ctype == "PRIMARY KEY":
            schema[table]["constraints"]["primary_key"].append(column)

        elif ctype == "FOREIGN KEY":
            schema[table]["constraints"]["foreign_keys"].append({
                "column": column,
                "references": {
                    "table": foreign_table,
                    "column": foreign_column
                }
            })

        elif ctype == "UNIQUE":
            schema[table]["constraints"]["unique"].append(column)

    return schema
