import psycopg2
from config import config

def get_connection():
    conn = psycopg2.connect(
        host=config["host"],
        database=config["database"],
        user=config["user"],
        password=config["password"]
    )
    return conn