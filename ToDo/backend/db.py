import web, os
from dotenv import load_dotenv
load_dotenv()

db = web.database(
    dbn='postgres',
    host=os.getenv('DB_HOST', '127.0.0.1'),
    port=int(os.getenv('DB_PORT', 5432)),
    user=os.getenv('DB_USER'),
    pw=os.getenv('DB_PASSWORD'),
    db=os.getenv('DB_NAME'),
)
