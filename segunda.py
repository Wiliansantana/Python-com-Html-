animais={
    "Cachorros":["Dalmatas", "Vira lara", "Pintcher"]
}
animais1={
    "Gatos":["Persa", "Siâmes", "Ragdoll"]
    }

pagina=open("index02.html", "w")
pagina.write("""

<html lang="pt-BR">
<head>
    <title> Dicionario de Animais</title>
</head>

<body>

""")

for c,v in animais.items():
    pagina.write("<h1>%s</h1>" % c)
    for e in v:
        pagina.write("<p>%s</p>" % e)

for c,v in animais1.items():
    pagina.write("<h1>%s</h1>" % c)
    for e in v:
        pagina.write("<p>%s</p>" % e)

    pagina.write("""

    </body>
    </html>
   
    """)
    pagina.close()