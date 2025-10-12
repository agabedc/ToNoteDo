import web
import os
from dotenv import load_dotenv

load_dotenv()

urls = (
    '/', 'index',
    '/add', 'add'
)

db = web.database(
    dbn='postgres',
    host='127.0.0.1',
    port=5432,
    user='postgres',
    pw=os.getenv('DB_PW'),
    db='postgres',
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
    def GET(self):
        notes = db.select('notes')
        return render.index(notes)

class add:
    def POST(self):
        i = web.input()
        n = db.insert('notes', title=i.title, body=i.body)
        raise web.seeother('/')
        

if __name__ == "__main__":
    app.run()