import web
import os
from dotenv import load_dotenv

load_dotenv()

urls = (
    '/', 'index',
    '/add', 'add',
    '/edit', 'edit',
    '/delete/(\d+)', 'delete'
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
        
class edit:
    def PUT(self):
        data = web.input()
        id_, title_, body_ = data.id, data.title, data.body

        db.update('notes',
                  where='id=$id',
                  vars={'id': id_},
                  title=title_,
                  body=body_)

        raise web.seeother('/')
    
class delete:
    def DELETE(self, id):
        db.delete('notes', where=f"id={id}")
        raise web.seeother('/')
    
if __name__ == "__main__":
    app.run()
