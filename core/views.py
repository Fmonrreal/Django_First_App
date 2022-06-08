from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a><li>
    <li><a href="/about-me/">Acerca de</a><li>
    <li><a href="/portafolio/">Portafolio</a><li>
    <li><a href="/conctact/">Conctacto</a><li>
<ul>
"""

# Create your views here.
def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def conctact(request):
    return render(request,"core/conctact.html")
# def conctact(request):
#     return HttpResponse( html_base + """
#         <h2>Contacto</h2>
#         <p>Aqui os dejo mi email para preguntarme dudas: <a href="mailto:lfmonrreal91@gmail.com">lfmonrreal91@gmail.com</a></p>
#     """)

