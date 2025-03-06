from jinja2 import Environment, select_autoescape, FileSystemLoader
from help.support.abspaths import jinja_templs

env = Environment(
    autoescape=select_autoescape('html'),
    loader=FileSystemLoader(jinja_templs)
)
template = env.get_template('html_reminder.html')
template.render(

)