import web

urls = (

    '/','Index',
    '/parametros', 'Parametros'
)
app = web.application(urls,globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()

class Parametros:
    def GET(self):
        titulo = "Título desde Python"
        descripcion = "DNeque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
        return render.parametros(titulo=titulo, descripcion=descripcion)
    
if __name__ == "__main__":
    app.run()