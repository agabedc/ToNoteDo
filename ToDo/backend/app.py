import os
import web
from db import db
import json

urls = (
    '/', 'Index',
    '/add', 'Add',
    '/toggle/(\\d+)', 'Toggle',
    '/edit/(\\d+)', 'Edit',
    '/delete/(\\d+)', 'Delete'
)

app = web.application(urls, globals())

# Render HTML templates from the 'templates' folder
render = web.template.render(
    os.path.join(os.path.dirname(__file__), 'templates'),
    cache=False
)
# The main class for the homepage
class Index:
    def GET(self):
        tasks = list(db.query("SELECT id, title, completed, created_at FROM public.tasks ORDER BY id DESC"))
        return render.index(tasks)
    
class Add:
    def POST(self):
        i = web.input(title="")
        title = i.title.strip()
        if title:
            db.insert('tasks', title=title)
        raise web.seeother('/')
        
class Toggle:
    def POST(self, id):
        db.query("""
            UPDATE public.tasks
            SET completed = NOT completed
            WHERE id = $id
        """, vars={'id': int(id)})
        raise web.seeother('/')

class Edit:
    def POST(self, id):
        data = web.input(title="")
        title = data.title.strip()
        if title:
            db.update('tasks', where='id=$id', vars={'id': int(id)}, title=title)
            if web.ctx.env.get('HTTP_X_REQUESTED_WITH'):  # If AJAX
                return json.dumps({'status': 'ok', 'id': int(id), 'title': title})
        raise web.seeother('/')

class Delete:
    def POST(self, id):
        db.delete('tasks', where='id=$id', vars={'id': int(id)})
        raise web.seeother('/')
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()