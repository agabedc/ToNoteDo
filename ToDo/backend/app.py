import web

urls = (
    '/', 'Index', '/add', 'add'
)


# Render HTML templates from the 'templates' folder
render = web.template.render('templates/')

# In-memory store for tasks
tasks = []

# The main class for the homepage
class Index:
    def GET(self):
        return render.index(tasks=tasks)  # render index.html with tasks
    
class add:
    def POST(self):
        i = web.input(task="")
        #add item to the list
        if i.task:
            tasks.append(i.task)
        raise web.seeother('/')
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()