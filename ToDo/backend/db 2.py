import os
import web
from dotenv import load_dotenv

load_dotenv(override=False)

def get_db():
    return web.database(
        dbn='postgres',
        db=os.getenv('PGDATABASE', 'slowapi'),
        user=os.getenv('PGUSER', 'postgres'),
        pw=os.getenv('PGPASSWORD', ''),
        host=os.getenv('PGHOST', 'localhost'),
        port=int(os.getenv('PGPORT', '5432')),
    )
