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
    app = web.application(urls, globals())
    app.run()