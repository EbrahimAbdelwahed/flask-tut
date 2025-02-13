from flask import Flask, render_template, session, redirect, url_for
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import introduction, database, auth, pages, blog, homepage

app = Flask(__name__)
app.secret_key = "plmoknij"

def pygmentize(code, lexer=PythonLexer(), formatter=HtmlFormatter()):
    return highlight(code, lexer, formatter)

app.jinja_env.filters['pygmentize'] = pygmentize

tutorial_sections = [
	{ 'id': 'Introduction', 'title': 'Introduzione', 'content': introduction.content },
	{ 'id': 'Variables', 'title': 'Creazione Homepage', 'content': homepage.content },
	{ 'id': 'Variables', 'title': 'flaskr/db.py', 'content': database.content },
	{ 'id': 'Conditionals_Loops', 'title': 'flaskr/auth.py', 'content': auth.content },
	{ 'id': 'Functions', 'title': 'flaskr/templates/*.html', 'content': pages.content },
	{ 'id': 'OOP', 'title': 'flaskr/blog.py', 'content': blog.content }
]

@app.route('/')
def index():
   return redirect(url_for('section', section_id='Introduction'))

@app.route('/section/<section_id>')
def section(section_id):
	session['current_section'] = section_id
	section = next((sec for sec in tutorial_sections if sec['id'] == section_id), None)

	return render_template('tutorial.html', section=section, sections=tutorial_sections) if section else ("Page not found", 404)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)
