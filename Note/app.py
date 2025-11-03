import web
import os
from dotenv import load_dotenv
import json

load_dotenv()

urls = (
    '/', 'index',
    '/add', 'add',
    '/edit/(\d+)', 'edit',
    '/delete/(\d+)', 'delete',
    '/stats', 'stats_page',
    '/api/stats', 'stats_api'
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
    def GET(self):
        return render.add()
    
    def POST(self):
        i = web.input()
        n = db.insert('notes', title=i.title, body=i.body)
        raise web.seeother('/')
        
class edit:
    def GET(self, id):
        note = db.select('notes', where='id=$id', vars={'id': id})
        if note:
            return render.edit(note[0]) 
        return "Note not found", 404

    def POST(self, id):
        data = web.input()
        db.update('notes',
                  where='id=$id',
                  vars={'id': id},
                  title=data.title,
                  body=data.body)
        raise web.seeother('/')

class delete:
    def POST(self, id):
        db.delete('notes', where=f"id={id}")
        raise web.seeother('/')
    
class stats_page:
    def GET(self):
        return render.stats() 

class stats_api:
    def GET(self):
        today = db.query("SELECT COUNT(*) AS c FROM notes WHERE created::date = CURRENT_DATE")[0].c
        week = db.query("SELECT COUNT(*) AS c FROM notes WHERE created >= date_trunc('week', CURRENT_DATE)")[0].c
        month = db.query("SELECT COUNT(*) AS c FROM notes WHERE created >= date_trunc('month', CURRENT_DATE)")[0].c
        all_notes = db.query("SELECT COUNT(*) AS c FROM notes")[0].c

        web.header('Content-Type', 'application/json')
        
        return json.dumps({
            "today": today,
            "week": week,
            "month": month,
            "all": all_notes
        })
    
if __name__ == "__main__":
    app.run()
