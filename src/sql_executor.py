import psycopg2
from dotenv import load_dotenv
import os


class PostgresDB:
    def __init__(self):
        # load .env variables
        load_dotenv()

        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")

        self.conn = None
        self.cursor = None

    def connect(self):
        """Initialize DB connection."""
        if self.conn is None:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()

    def execute_query(self, query):
        if self.conn is None:
            return "Error: Call connect() first."

        try:
            self.cursor.execute(query)
            self.conn.commit()

            try:
                return self.cursor.fetchall()
            except psycopg2.ProgrammingError:
                return "Query executed successfully"

        except Exception as e:
            return f"Error: {e}"

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
