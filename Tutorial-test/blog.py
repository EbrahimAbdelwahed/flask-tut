from tools import *
from tools import _f, _try, _except, _import, _from, _def, _with, _as, _if, _elif, _else, _is, _not, _and, _in, _return, _lambda, _None, _at, _True

console1 = [
	[_from, "flask ", _import, "("],
	["", "Blueprint, flash, g, redirect, render_template, request, url_for"],
	[")"],
	[_from, "werkzeug.exceptions ", _import, "abort"],
	[""],
	[_from, "flaskr.auth ", _import, "login_required"],
	[_from, "flaskr.db ", _import, "get_db"],
	[""],
	["bp = ", func("Blueprint"), "(", string("blog"), ", __name__)"]
]

console2 = [
	[_def, func("create_app"), "(", param("test_config "), "= ", _None, "):" ],
	["", "..."],
	["", _from, ". ", _import, "blog"],
	["", "app.", func("register_blueprint"), "(blog.bp)"],
	[""],
	[_return, "app"]
]

console3 = [
	[_at, "bp.", func("route"), "(", string("/"), ")"],
	[_def, func("index"), "():"],
	["", "db = ", func("get_db"), "()"],
	["", "posts = db.", func("execute"), "("],
	["", "", string("SELECT p.id, title, body, created, author_id, username")],
	["", "", string(" FROM post p JOIN user u ON p.author_id = u.id")],
	["", "", string(" ORDER BY created DESC")],
	["", ").", func("fetchall"), "()"],
	[""],
	[_return, func("render_template"), "(", string("blog/index.html"), param("posts "), "= posts)"]
]

console4 = [
	[_at, "bp.", func("route"), "(", string("/create"), ", ", param("methods "), "= (", string("GET"), ", ", string("POST"), "))"],
	[_at, func("login_required")],
	[_def, func("create"), "():"],
	["", _if, "request.method == ", string("POST"), ":"],
	["", "", "title = request.form[", string("title"), "]"],
	["", "", "body = request.form[", string("body"), "]"],
	["", "", "error = ", _None],
	[""],
	["", "", _if, _not, "title:"],
	["", "", "", "error = ", string("Title is required.")],
	[""],
	["", "", _if, "error", _is, _not, _None, ":"],
	["", "", "", func("flash"), "(error)"],
	["", "", _else],
	["", "", "", "db = ", func("get_db"), "()"],
	["", "", "", "db.", func("execute"), "("],
	["", "", "", "", string("INSERT INTO post (title, body, author_id")],
	["", "", "", "", string(" VALUES (?, ?, ?)"), ", (title, body, g.user[", string("id"), "])"],
	["", "", "", ")"],
	["", "", "", "db.", func("commit"), "()"],
	["", "", "", _return, func("redirect"), "(", func("url_for"), "(", string("blog.index"), "))"],
	[""],
	["", _return, func("render_template"), "(", string("blog/create.html"), ")"]
]

console5 = [
	[_def, func("get_post"), "(", param("check_author "), "= ", _True, "):"],
	["", "post = ", func("get_db"), (), func("execute"), "("],
	["", "", string("SELECT p.id, title, body, created, author_id, username")],
	["", "", string(" FROM post p JOIN user u ON p.author_id = u.id")],
	["", "", string(" WHERE p.id = ?"), ", (id,)"],
	["", ").", func("fetchone"), "()"],
	[""],
	["", _if, "post", _is, _None, ":"],
	["", "", func("abort"), "(", value("404"), _f, string_f("\"Post id\""), "{ id } ", string_f("\"doesn't exist.\""), ")"],
	[""],
	["", _if, "check_author", _and, "post[", string("author_id"), "] != g.user[", string("id"), "]:"],
	["", "", func("abort"), "(", value("403"), ")"],
	[""],
	[_return, "post"],
	[""],
	[_at, "bp.", func("route"), "(", string("/<int:id>/update"), ", ", param("methods "), "= (", string("GET"), ", ", string("POST"), "))"],
	[_at, func("login_required")],
	#[_def, func(update), "(", param("id"), "):"],
	["", "post = ", func("get_post"), "(id)"],
	[""],
	["", _if, "request.method == ", string("POST"), ":"],
	["", "", "title = request.form[", string("title"), "]"],
	["", "", "body = request.form[", string("body"), "]"],
	["", "", "error = ", _None],
	[""],
	["", "", _if, _not, "title:"],
	["", "", "", "error = ", string("Title is required.")],
	[""],
	["", "", _if, "error", _is, _not, _None, ":"],
	["", "", "", func("flash"), "(error)"],
	["", "", _else],
	["", "", "", "db = ", func("get_db"), "()"],
	["", "", "", "db.", func("execute"), "("],
	["", "", "", "", string("UPDATE post SET title = ?, body = ?")],
	["", "", "", "", string(" WHERE id = ?"), ", (title, body, id)"],
	["", "", "", ")"],
	["", "", "", "db.", func("commit"), "()"],
	["", "", "", _return, func("redirect"), "(", func("url_for"), "(", string("blog.index"), "))"],
	[""],
	["", _return, func("render_template"), "(", string("blog/update.html"), ")"]
]

console6 = [
	[_at, "bp.", func("route"), "(", string("/<int:id>/delete"), ", ", param("methods "), "= (", string("POST"), ", ))"],
	[_at, func("login_required")],
#	[_def, func(delete), "(", param("id"), "):"],
	["", func("get_post"), "(id)"],
	["", "db = ", func("get_db"), "()"],
	["", "db.", func("execute"), "(", string("DELETE FROM post WHERE id = ?"), ", (id,))"],
	["", "db.commit()"],
	["", _return, func("redirect"), "(", func("url_for"), "(", string("blog.index"), "))"]
]

content = [
	"Creazione del blueprint",
	console1,
	"Registrazione del blueprint",
	console2,
	"Mostra post",
	console3,
	"Crea post",
	console4,
	"Update post",
	console5,
	"Elimina post",
	console6,
	"File completo",
	console1 + [" "] + console3 + [" "] + console4 + [" "] + console5 + [" "] + console6
]
