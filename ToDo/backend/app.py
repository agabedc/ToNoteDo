import web

urls = (
    '/', 'Index'
)


# Render HTML templates from the 'templates' folder
render = web.template.render('templates/')

# The main class for the homepage
class Index:
    def GET(self):
        return render.index()  # render index.html

if __name__ == "__main__":
    for i in range(10):
        print(i)
    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ("127.0.0.1", 8080))