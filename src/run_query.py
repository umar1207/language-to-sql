from src.sql_executor import PostgresDB


def run_query(query):
    db = PostgresDB()
    db.connect()
    results = db.execute_query(query)
    db.close()
    return results

