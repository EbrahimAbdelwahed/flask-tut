from tools import *
from tools import _import, _from, _def, _if, _else, _is, _try, _except, _pass, _return, _None, _True, _at, _pip, _install

text1 = "Apri il prompt dei comandi {per spostarsi tra le cartelle usare il comando: cd nome_della_cartella}, naviga nella cartella del tuo progetto e attiva l'ambiente virtuale se ne hai uno."
text2 = """Vai al browser e naviga a http://127.0.0.1:5000/. Dovresti vedere il messaggio "Hello World!"."""
text3 = "Puoi espandere questa homepage usando i template di Flask (render_template) per separare l'HTML dal codice Python, puoi anche aggiungere del CSS per lo stile."
text4 = "Crea una cartella chiamata templates nella tua cartella del progetto."
text5 = "Crea un file index.html dentro la cartella templates:"
text6 = "Modifica app.py per usare questo template:"
text7 = "Ora quando avvii l'applicazione, vedrai la pagina HTML renderizzata. Questo è solo l'inizio per creare una homepage con Flask, ma ti dà una base su cui costruire ulteriormente."
space = "\n "




console1 = [
    ["<!doctype html>"],
    ["""<html lang="it">"""],
    ["<head>"],
    ["", "<title>Homepage</title>"],
    ["</head>"],
    ["<body>"],
    ["", "<h1>Benvenuto alla Mia Homepage!</h1>"],
    ["", "<p>Questa è una pagina di esempio.</p>"],
    ["</body>"],
    ["</html>"]
]

console2 = [
    [_from, "flask ", _import, "Flask"],
	["", "app = ", func("Flask"), "(__name__, "],
	["", _at, "app.", func("route"), "(", string("/"), ")"],
	["", _def, func("hello"), "():"],
	["", "", _return, "render_template(", string("'index.html'"), ")"],
	[""],
	["", _if , ("__name__ =="), ("""'__main__':""")],
    ["", "app.", func("run "), "debug=" , _True ]
]

content = [
    text1,
    [["$ python app.py"]],
    text2,
    [""],
    text3,
    text4,
    [["$ mkdir templates"]],
    text5,
    console1,
    text6,
    console2,
    text7


    
    






]