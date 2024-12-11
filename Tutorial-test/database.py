from tools import *
from tools import _import, _from, _def, _with, _as, _if, _is, _not, _in, _return, _lambda, _None, _at

console1 = [
	[keyword("DROP TABLE IF EXISTS "), "user;"],
	[keyword("DROP TABLE IF EXISTS "), "post;"],
	[""],
	[keyword("CREATE TABLE "), "user ("],
	["", "id ", keyword("INTEGER "), value("PRIMARY KEY "), macro("AUTOINCREMENT"), ","],
	["", "username ", keyword("TEXT "), macro("UNIQUE NOT NULL"), ","],
	["", "password ", keyword("TEXT "), macro("NOT NULL")],
	[");"],
	[""],
	[keyword("CREATE TABLE "), "post ("],
	["", "id ", keyword("INTEGER "), value("PRIMARY KEY "), macro("AUTOINCREMENT"), ","],
	["", "author_id ", keyword("INTEGER "), macro("NOT NULL"), ","],
	["", "created ", keyword("TIMESTAMP "), macro("NOT NULL "), keyword("DEFAULT "), macro("CURRENT_TIMESTAMP"), ","],
	["", "title ", keyword("TEXT "), macro("NOT NULL"), ","],
	["", "body ", keyword("TEXT "), macro("NOT NULL"), ","],
	["", value("FOREIGN KEY "), "(author_id) ", value("REFERENCES "), "user (id)"],
	[");"]
]
console2 = [
	[_from, "flask ", _import, "current_app, g"],
	[_import, "sqlite3"],
	[""],
	[_from, "datetime ", _import, "datetime"],
	[_import, "click"]
]

console3 = [
	[_def, func("get_db"), "():"],
	["", _if, string("db "), _not, _in, "g:"],
	["", "", "g.db = sqlite3.", func("connect"), "("],
	["", "", "", "current_app.config[", string("DATABASE"), "],"],
	["", "", "", param("detect_types "), "= sqlite3.", macro("PARSE_DECLTYPES")],
	["", "", ")"],
	[""],
	["", _return, "g.db"]
]

console4 = [
	[_def, func("close_db"), "(", param("e "), "= ", _None, "):"],
	["", "db = g.", func("pop"), "(", string("db"), ", ", _None, ")"],
	[""],
	["", _if, "db ", _is, _not, _None, ":"],
	["", "", "db.", func("close"), "()"]
]

console5 = [
	[_def, func("init_db"), "():"],
	["", "db = ", func("get_db"), "()"],
	[""],
	[_with, "current_app.", func("open_resource"), "(", string("schema.sql"), ") ", _as, "f:"],
	["", "db.", func("executescript"), "(f.", func("read"), "().", func("decode"), "(", string("utf8"), "))"],
	[""],
	[_at, "click.", func("command"), "(", string("init-db"), ")"],
	[_def, func("init_db_command"), "():"],
	["", func("init_db"), "()"],
	["", "click.", func("echo"), "(", string("Database initialized!"), ")"],
	[""],
	["sqlite3.", func("register_converter"), "("],
	["", string("timestamp"), ", ", _lambda, param("v"), ": datetime.", func("fromisoformat"), "(v.", func("decode"), "())"],
	[")"]
]

console6 = [
	[_def, func("init_app"), "(", param("app"), "):"],
	["", "app.", func("teardown_appcontext"), "(", func("close_db"), ")"],
	["", "app.cli.", func("add_command"), "(", func("init_db_command"), ")"]
]

console7 = [
	[_def, func("create_app"), "(", param("test_config "), "= ", _None, "):" ],
	["", "..."],
	["", _from, ". ", _import, "db"],
	["", "db.", func("init_app"), "(app)"],
	[""],
	[_return, "app"]
]

console8 = [
	["$ flask --app flaskr init-db"],
	["Initialized the database."]
]

content = [
	"Il nostro database",
	console1,
	"Importiamo i moduli necessari.",
	console2,
	"Funzione per chiamare database.",
	console3,
	"Funzione per chiudere database.",
	console4,
	"Funzione per inizializzare database.",
	console5,
	"Registrare funzioni.",
	console6,
	console7,
	"Inizializza il database.",
	console8,
	"File completo",
	console2 + [" "] + console3 + [" "] + console4 + [" "] + console5 + [" "] + console6
]