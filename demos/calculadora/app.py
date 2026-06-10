import web

urls = (

    '/','Index',
        '/calculadora', 'Calculadora'
)
app = web.application(urls,globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()

class Calculadora:
    def GET(self):
        return render.calculadora()
    
    def POST(self):
        formulario = web.input()
        numero_1= float(formulario['numero_1'])
        numero_2= float(formulario['numero_2'])
        resultado = numero_1 + numero_2

        print(f"Tipo de dato de numero_1: {type(numero_1)}")
        print(f"Tipo de dato de numero_2: {type(numero_2)}")

        return f"La suma de {numero_1} + {numero_2} = {resultado}"
if __name__ == "__main__":
    app.run()