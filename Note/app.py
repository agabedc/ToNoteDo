import web


urls = (
    '/(.*)', 'index'
)

db = web.database(
    dbn='postgres',
    host='127.0.0.1',
    port=5432,
    user='username',
    pw='password',
    db='dbname',
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
    def GET(self, name):
        i = web.input(name=None)
        return render.index(i.name)

if __name__ == "__main__":
    app.run()