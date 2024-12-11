from tools import *
from tools import _f, _try, _except, _import, _from, _def, _with, _as, _if, _elif, _else, _is, _not, _in, _return, _lambda, _None, _at

console1 = [
	[_from, "flask ", _import, "("],
	["", "Blueprint, flash, g, redirect, render_template, request, session, url_for"],
	[")"],
	[_from, "werkzeug.security", _import, "check_password_hash, generate_password_hash"],
	[_from, "flaskr.db", _import, "get_db"],
	[_import, "functools"],
	[""],
	["bp = ", func("Blueprint"), "(", string("auth"), ", __name__, url_prefix = ", string("/auth"), ")"]
]

console2 = [
	[_def, func("create_app"), "(", param("test_config "), "= ", _None, "):" ],
	["", "..."],
	["", _from, ". ", _import, "auth"],
	["", "app.", func("register_blueprint"), "(auth.bp)"],
	[""],
	[_return, "app"]
]

console3 = [
	[_at, "bp.", func("route"), "(", string("/register"), ", ", param("methods "), "= (", string("GET"), ", ", string("POST"), "))"],
	[_def, func("register"), "():"],
	["", _if, "request.method == ", string("POST"), ":"],
	["", "", "username = request.form[", string("username"), "]"],
	["", "", "password = request.form[", string("password"), "]"],
	["", "", "db = ", func("get_db"), "()"],
	["", "", "error = ", _None],
	[""],
	["", "", _if, _not, "username:"],
	["", "", "", "error = ", string("Username is required!")],
	["", "", _elif, _not, "password:"],
	["", "", "", "error = ", string("Password is required!")],
	[""],
	["", "", _if, "error ", _is, _None, ":"],
	["", "", "", _try],
	["", "", "", "", "db.", func("execute"), "("],
	["", "", "", "", "", string("INSERT INTO user (username, password) VALUES (?, ?)"), ","],
	["", "", "", "", "", "(username, ", func("generate_password_hash"), "(password))"],
	["", "", "", "", ")"],
	["", "", "", "", "db.", func("commit"), "()"],
	["", "", "", _except, "db.", macro("InterityError"), ":"],
	["", "", "", "", "error = ", _f, string_f("\"User "), "{ username } ", string_f("is already registered!\"")],
	["", "", "", _else],
	["", "", "", "", _return, func("redirect"), "(", func("url_for"), "(", string("auth.login"), "))"],
	[""],
	["", "", func("flash"), "(error)"],
	[""],
	["", _return, func("render_template"), "(", string("auth/register.html"), ")"]
]

console4 = [
	[_at, "bp.", func("route"), "(", string("/login"), ", ", param("methods "), "= (", string("GET"), ", ", string("POST"), "))"],
	[_def, func("login"), "():"],
	["", _if, "request.method == ", string("POST"), ":"],
	["", "", "username = request.form[", string("username"), "]"],
	["", "", "password = request.form[", string("password"), "]"],
	["", "", "db = ", func("get_db"), "()"],
	["", "", "error = ", _None],
	["", "", "user = db.", func("execute"), "("],
	["", "", "", string("SELECT * FROM user WHERE username = ?"), "(username)"],
	["", "", ").", func("fetchone"), "()"],
	[""],
	["", "", _if, "username", _is, _None, ":"],
	["", "", "", "error = ", string("Incorrect username!")],
	["", "", _elif, _not, func("check_password_hash"), "(user[", string("password"), "], password):"],
	["", "", "", "error = ", string("Incorrect password!")],
	[""],
	["", "", _if, "error ", _is, _None, ":"],
	["", "", "", "session.", func("clear"), "()"],
	["", "", "", "session[", string("user_id"), "] = user[", string("id"), "]"],
	["", "", "", _return, func("redirect"), "(", func("url_for"), "(", string("index"), "))"],
	[""],
	["", "", func("flash"), "(error)"],
	[""],
	["", _return, func("render_template"), "(", string("auth/login.html")]
]

console5 = [
	[_at, "bp.", macro("before_app_request")],
	[_def, func("load_logged_in_user"), "():"],
	["", "user_id = session.", func("get"), "(", string("user_id"), ")"],
	[""],
	["", _if, "user_id", _is, _None, ":"],
	["", "", "g.user = ", _None],
	["", _else],
	["", "", "g.user = ", func("get_db"), "().", func("execute"), "("],
	["", "", "", string("SELECT * FROM user WHERE id = ?"), ", (user_id)"],
	["", "", ").", func("fetchone"), "()"]
]

console6 = [
	[_def, func("login_required"), "(", param("view"), "):"],
	["", _at, "functools.", func("wraps"), "(view)"],
	["", _def, func("wrapped_view"), "(**", param("kwargs"), "):"],
	["", "", _if, "g.user ", _is, _None, ":"],
	["", "", "", _return, func("redirect"), "(", func("ur_for"), "(", string("auth.login"), ")"],
	[""],
	["", "", _return, func("vier"), "(**kwargs)"],
	["", _return, "wrapped_view"]
]

console7 = [
	[_at, "bp.", func("route"), "(", string("/logout"), ")"],
	[_def, func("logout"), "():"],
	["", "session.", func("clear"), "()"],
	["", _return, func("redirect"), "(", func("url_for"), "(", string("index"), "))"]
]

content = [
	"Creazione del blueprint.",
	console1,
	"Regisrazione del blueprint.",
	console2,
	"Pagina per la registrazione.",
	console3,
	"Pagina per l'accesso.",
	console4,
	"Caricare dati dell'utente.",
	console5,
	"Controllare se l'accesso è stato effettuato.",
	console6,
	"Logout",
	console7,
	"File completo",
	console1 + [" "] + console3 + [" "] + console4 + [" "] + console5 + [" "] + console6 + [" "] + console7
]