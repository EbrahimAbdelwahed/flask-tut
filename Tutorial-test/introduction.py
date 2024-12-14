from tools import *
from tools import _import, _from, _def, _if, _else, _is, _try, _except, _pass, _return, _None, _True, _at, _pip, _install

'''
text1 = """Cos'è flask? una suite per il web developing che si può integrare in python.
                Per procedere con l'installazione utilizzeremo pip(package manager) che si occuperà occuperà di identificare e scaricare flask e le relative dipendenze."""

text2 = """Completata  l’installazione, procediamo alla creazione del nostro progetto. 
Utilizzeremo il metodo mkdir (make directory), che creerà una cartella che conterrà tutti i file necessari alla nostra applicazione web."""

text3 = """Creato il nostro progetto dovremo procedere all’importazione di flask dalla libreria installata precedentemente. Quindi scriveremo: """

text4 = """Ora è possibile inizializzare la variabile app che sarà appunto la nostra applicazione web:"""

text5 = """Come possiamo notare abbiamo passato alla variabile app una dunder variable, le dunder variable sono speciali tipi di variabile in py che permettono alla variabile di assumere valori differenti dipendentemente da alcune condizioni. """

text6 = """In questo caso la dunder variable _name_ indica il modulo al quale Flask deve attingere per file statici, template ed altro."""

text7 = """Definiamo ora una funzione homepage che restituisca la stringa “Ciao”:"""

text8 = """Quella che abbiamo appena scritto è una cosidetta funzione View: questo tipo di funzioni ci permettono di gestire le diverse aree del nostro sito web; avremo quindi tante funzioni View quanti Url nel nostro sito."""

text9 = """OSSERVA"""

text10 = """Il nome delle funzioni, per quanto arbitrario, dovrà essere scelto con criterio, in quanto sarà poi parte dell’indirizzo necessario per raggiungerlo."""

space = " "

text11 = """Per gestire le diverse funzioni View, Flask ci permette di utilizzare il decoratore @app ed il metodo  route, al quale passeremo il percorso che vogliamo utilizzare."""
 
text12 = """In questo caso visiteremo l’  homepage, il cui percorso è “/”:"""

text13 = """Per acquisire praticità con questo meccanismo, creeremo un'altra funzione view . In questo caso la chiameremo “credits” mappata per collegare all’url “/credits”:"""

text14 = """Ora possiamo avviare il nostro server di sviluppo (la copia di sviluppo del nostro sito). Per accedere al server dovremo avvalerci del terminale(premere il tasto Win + R e scrivere cmd):"""

text15 = """L’avvio del server risulterà contestualmente ad un errore: la libreria di Flask non trova la nostra applicazione. Per ovviare a tale problema, dobbiamo indicare a Flask di utilizzare la variabile d’ambiente FLASK_APP, ovvero una variabile definita a livello del sistema operativo che ci permette di andare a memorizzare alcune impostazioni in questo caso relative al funzionamento della nostra applicazione Flask."""

text16 = """Per accedere alla copia del nostro sito web è unicamente necessario riportare nel browser l’indirizzo IP, sopra evidenziato in rosso(127.0.0.1:5000)."""

text17 = """Da ora """

'''

text1 = "Flask è un framework leggero per applicazioni web. Per procedere alla sua installazione sarà necessario creare la cartella che ospiterà il progetto."
text2 = "Tutti prompt che sono preceduti dal simbolo $ sono comandi che vanno eseguiti nel prompt dei comandi. \n Ora dobbiamo spostarci nella cartella del progetto. "
text3 = "Per installare ed utilizzare Flask, è buon uso creare un ambiente virtuale."
text4 = "Per attivare l'ambiente virtuale: " # spostandoci nella cartella .venv {per spostarsi tra le cartelle usare il comando: cd nome_della_cartella}."
text5 = "Dovresti vedere il nome dell'ambiente virtuale nel prompt dei comandi, indicando che è attivo."
text6 = "Installa Flask: \n Con l'ambiente virtuale attivo, esegui:"
text7 = "Questo comando scaricherà e installerà Flask e le sue dipendenze."
text8 = "Creare una Prima Applicazione Flask: Crea un file chiamato app.py (o come preferisci chiamarlo) nella tua cartella del tuo progetto."
text9 = "Dal prompt dei comandi (con l'ambiente virtuale attivo), esegui:"
text10 = """Dovresti vedere un messaggio che indica che il server Flask è in esecuzione. Apri il tuo browser e vai a http://127.0.0.1:5000/ per vedere il messaggio "Hello, World!"."""
text11 = """Ricorda di disattivare l'ambiente virtuale quando hai finito di lavorare con esso digitando "deactivate" nel prompt dei comandi."""
text12 = "Per evitare di dover utilizzare un ambiente virtuale è necessario aggiungere il percorso del pacchetto flask alla variabile d'ambiente PATH."
text13 = "Per cercare dove si trova l'eseguibile di flask:"
text14 = "Copiare il percorso della cartella in cui è contenuto l'eseguibile di flask:"
text15= "ATTENZIONE: Non copiare il percorso della cartella contenente flask del tuo ambiente virtuale:"
text16 = """Ora modificheremo la variabile d'ambiente PATH: \n 1. Nelle Impostazioni -> Sistema -> Informazioni \n 2. Nelle Impostazioni correlate -> Impostazioni di sistema avanzate \n"""
text17 = "3. In Avanzate -> Variabili d'ambiente \n"
text18 = " 4. Selezionare la variabile Path e modificarla \n "
text19 = "5. Selezionare nuovo ed incollare il percorso precedentemente copiato."
text20 = " \n \n Per verificare che flask sia accessibile globalmente sul pc:"
'''
console1 = [
	[_from, "flask ", _import, "Flask"],
	[_import, "os"],
]

console2 = [
	[_def, func("create_app"), "(", param("test_config"), "= ", _None, "):" ],
	["", "app = ", func("Flask"), "(__name__, ", param("instance_relative_config "), " = ", _True, ")"],
	["", "app.config.", func("from_mapping"), "("],
	["", "", param("SECRET_KEY "), "= ", string("dev"), ","],
	["", "", param("DATABASE "), "= os.path.", func("join"), "(app.instance_path, ", string("flaskr.sqlite"), "),"],
	["", ")"],
	[""],
	["", _if, "test_config ", _is, _None, ":"],
	["", "", "app.config.", func("from_pyfile"), "(", string("config.py"), ", ", param("silent "), "= ", _True, ")"],
	["", _else],
	["", "", "app.config.", func("from_mapping"), "(test_config)"],
	[""],
	["", _try],
	["", "", "os.", func("makedirs"), "(app.instance_path)"],
	["", _except, macro("OSError"), ":"],
	["", "", _pass],
	[""],
	["", _at, "app.", func("route"), "(", string("/"), ")"],
	["", _def, func("hello"), "():"],
	["", "", _return, string("<h1>Hello, World!</h1>")],
	[""],
	["", _return, "app	"]
]
console3 = [
    [_from, "flask ", _import, "Flask"],
]
console4 = [
[_def, func("create_app"),":" ],
	["", "app = ", func("Flask"), "(__name__) "]
    
]

console5 = [
    [_def, "homepage(): "],
    [_return, "Ciao"]
]

console6 = [
	["", _at, "app.", func("route"), "(", string("/credits"), ")"],
	["", _def, func("contatti"), "():"],
	["", "", _return, string("<h3>Questo sito è stato sviluppato da un alunno del 5i</h3>")],
	[""],
	["", _return, "app	"]

]

console7 = [
	["", _at, "app.", func("route"), "(", string("/"), ")"],
	["", _def, func("homepage"), "():"],
	["", "", _return, string("<h1>Hello, World!</h1>")],
	[""],
	["", _return, "app	"]

]'''

console1 = [
	[_from, "flask ", _import, "Flask"],
	[ "app = ", func("Flask"), "(__name__, "],
	[ _at, "app.", func("route"), "(", string("/"), ")"],
	[ _def, func("hello"), "():"],
	["", "", _return, string("<h1>Hello, World!</h1>")],
	[""],
	[ _if , ("__name__ =="), ("""'__main__':""")],
    	["", "app.", func("run "), "debug=" , _True ]
]
	

   
   


content = [

	text1,
	[["$ mkdir nome_del_tuo_progetto"]],
	text2,
	[["$ cd nome_del_tuo_progetto"]],
	text3,
	[["$ python3 -m venv .venv"]],
	text4,
	[["$ nome_del_tuo_progetto\Scripts\\activate"]],
	text5,
	text6,
	[["$ pip install Flask"]],
	text7,
	text8,
	console1,
	text9,
	[["$ python app.py"]],
	text10,
	text11,
	text12,
	text13,
	[["$ dir /s flask*"]],
	text14,
	{ "src": "2.PNG" },
	text15,
	{ "src": "3.PNG" },
	text16,
	text17,
	{ "src": "4.PNG" },
	text18,
	{ "src": "5.PNG" },
	text19,
	{ "src": "6.PNG" },
	text20,
	{ "src": "7.PNG" }

]

'''
    text1,
    [["$ pip install flask"]],
    text2,
    [["$ mkdir hello_flask"]],
    text3 + " ",
    console3,   
    text4,
    console4,
    text5,
    text6,
    text7,
    console5,
	text8,
	text9,
	text10,
	space,
	text11,
	text12,
	console7,
	text13,
	console6,
	text14,
	[["$ flask run"]],
	text15,
	[["$ set FLASK_APP=application.py"]],
	text16,
		"Cominciamo importando Flask e os, che ci aiuterà a creare la cartella che conterrà il nostro database.",
	console1,
   "Adesso creiamo la nostra Flask app definendo la funzione create_app().",
   console2,
   "File completo.",
	console1 + [" "] + console2,
   "Possiamo eseguare il programma.",
   [
		["$ flask --app flaskr run --debug"]
	],

   "Risultato.",
   { "src": "Img1.png" },
        console3 '''
