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

def validate_note(data):
    errors = {}
    if not data.get('title', '').strip():
        errors['title'] = "Title is required"
    if not data.get('body', '').strip():
        errors['body'] = "Body is required"
    return errors

class index:
    def GET(self):
        notes = db.select('notes')
        return render.index(notes)

class add:
    def GET(self):
        return render.add(errors={}, title='', body='')
    
    def POST(self):
        i = web.input(title='', body='')
        errors = validate_note(i)
        if errors:
            return render.add(errors=errors, title=i.title, body=i.body)
        n = db.insert('notes', title=i.title, body=i.body)
        raise web.seeother('/')
        
class edit:
    def GET(self, id):
        note = db.select('notes', where='id=$id', vars={'id': id})
        if note:
            return render.edit(note[0], errors={}) 
        raise web.seeother('/?message=Note%20not%20found')

    def POST(self, id):
        note_query = db.select('notes', where='id=$id', vars={'id': id})
        if not note_query:
            raise web.seeother('/?message=Note%20not%20found')
        data = web.input(title='', body='')
        errors = validate_note(data)
        if errors:
            note = note_query[0]
            note.title = data.title
            note.body = data.body
            return render.edit(note=note, errors=errors)
        db.update('notes',
                  where='id=$id',
                  vars={'id': id},
                  title=data.title,
                  body=data.body)
        raise web.seeother('/')

class delete:
    def POST(self, id):
        note = db.select('notes', where='id=$id', vars={'id': id})
        if not note:
            raise web.seeother('/?message=Note%20not%20found')
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
