import os
from typing import List, Any

def fetch_records(query: str) -> List[Any]:
    """Fetch records from Postgres using the query."""
    import psycopg2
    from psycopg2.extras import RealDictCursor

    dsn = os.environ.get("DATABASE_URL")
    if not dsn:
        raise ValueError("DATABASE_URL environment variable not set")

    with psycopg2.connect(dsn) as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()
