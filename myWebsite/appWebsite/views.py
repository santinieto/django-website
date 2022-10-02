from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from appWebsite.forms import FormularioArticulo
from appWebsite.models import Article, Category
from appWebsite import forms

# Respuestas Http básicas
def httpTitle(text):
    return '<h1>{}</h1>'.format(text)

def httpSubTitle(text):
    return '<h3>{}</h3>'.format(text)

def httpParagraph(text):
    return '<p>{}</p>'.format(text)

# Vistas HTTP básicas
def httpIndex(request):
    return HttpResponse(
        httpTitle('Titulo de prueba: Hola Mundo!') + 
        httpSubTitle('Subtitulo de prueba!') +        
        httpParagraph('párrafo de prueba')
        )

# Vistas con Bootstrap 5
def index(request):

    skills = [
        'Python','C++','Matlab','Data Science'
    ]

    return render(request, 'index.html', {
        'title'     : 'Pagina de inicio',
        'name'      : 'Santiago Enrique Nieto',
        'skills'    : skills,
    })

def holaMundo(request):
    return render(request, 'hola_mundo.html')
    
def paginaGenerica(request):
    return render(request, 'pagina_generica.html')

def calculadoraYears(request):

    inicio  = 2022
    fin     = 2100
    years   = range(inicio, fin+1)

    return render(request, 'calculadora_years.html', {
        'years' : years,
    })

def contacto(request):
    return render(request, 'contacto.html')

# Metodo para crear un articulo
def httpCrearArticulo(request, title = 'Articulo generico', content = 'Contenido generico', public = True): # Esta vista se va a encargar de crear un articulo dentro de nuestra web

    if request.method == 'GET':

        try:
            public = True if request.GET['public'] else False
        except:
            public = False

        article = Article(
            title = request.GET['title'],
            content = request.GET['content'],
            public = public,
        )

        article.save()

        output = """
        <h1>Articulo creado!!!</h1>
        <h3>Titulo: {}</h3>
        <h3>Contenido: {}</h3>
        <h3>Public: {}</h3>
        """.format(title, content, public)

        return render(request, 'articulo_exitoso.html')
    
    if request.method == 'POST':

        article = Article(
            title = request.POST['title'],
            content = request.POST['content'],
            public = True,
        )

        article.save()

        output = """
        <h1>Articulo creado!!!</h1>
        <h3>Titulo: {}</h3>
        <h3>Contenido: {}</h3>
        <h3>Public: {}</h3>
        """.format(title, content, public)

        return render(request, 'articulo_exitoso.html')

    return render(request, 'articulo_fallido.html')

def crearArticulo(request):
    return render(request, 'crear_articulo.html')
    
def crearArticuloClase(request):

    formulario = FormularioArticulo()

    return render(request, 'crear_articulo_clase.html', {
        'form' : formulario,
    })

# Mostrar un articulo en pantalla
def getArticulo(request):

    try:
        articulo = Article.objects.get(pk = 70)

        output = """
        <h1>Articulo obtenido!!!</h1>
        <h3>Titulo: {}</h3>
        <h3>Contenido: {}</h3>
        <h3>Public: {}</h3>
        """.format(articulo.title, articulo.content, articulo.public)
    except:
        output = """
        <h1>Articulo no encontrado!!!</h1>
        """

    return HttpResponse(output)

# Metodo para editar articulo
def editArticulo(request):

    try:
        articulo = Article.objects.get(pk = 7)

        articulo.title = 'Nombre editado'
        articulo.content = 'Contedio editado'
        articulo.public = False

        articulo.save()

        output = """
        <h1>Articulo editado!!!</h1>
        <h3>Titulo: {}</h3>
        <h3>Contenido: {}</h3>
        <h3>Public: {}</h3>
        """.format(articulo.title, articulo.content, articulo.public)
    except:
        output = """
        <h1>Articulo no encontrado!!!</h1>
        """

    return HttpResponse(output)

# Mostrar todos los articulos
def mostrarArticulos(request):

    articulos = Article.objects.all()
    #articulos = Article.objects.order_by('title')
    #articulos = Article.objects.order_by('-title')

    #articulos = Article.objects.exclude(public = False)

    # Ejecutar SQL en Python
    articulos = Article.objects.raw("""
    SELECT * FROM appWebsite_article WHERE public = 1
    """)

    return render(request, 'mostrar_articulos.html', {
        'title' : 'Lista de articulos',
        'articulos' : articulos,
    })

# Metodo para borrar articulos
def borrarArticulo(request, id):
    articulo = Article.objects.get(pk = id)
    articulo.delete()

    return redirect('mostrar_articulos')