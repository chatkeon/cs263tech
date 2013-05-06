import cgi
import datetime
import urllib
import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api import backends

class Greeting(db.Model):
    """Models an individual Guestbook entry with author, content, and date."""
    author = db.StringProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

def guestbook_key(guestbook_name=None):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name.
    Arguments: guestbook_name
    Returns: db.Key"""
    return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')

class MainPage(webapp2.RequestHandler):

    def get(self):
        """Get method for class MainPage."""
        guestbook_name=self.request.get('guestbook_name')
        greetings_query = Greeting.all().ancestor(
            guestbook_key(guestbook_name)).order('-date')
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        urlp = self.request.uri + 'profile'
        profile = 'Profile'

        urla = self.request.uri + 'admin'
        admin = 'Admin'

        template_values = {
            'greetings': greetings,
            'url': url,
            'url_linktext': url_linktext,
            'urlp': urlp,
            'Profile': profile,
            'urla': urla,
            'Admin': admin,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

class Guestbook(webapp2.RequestHandler):

    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name')
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user().nickname()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/?' + urllib.urlencode(query_params))

class Profile(webapp2.RequestHandler):

    def get(self):
        if users.get_current_user():
            self.response.write("Hello, " + users.get_current_user().nickname())
        else:
            self.response.write("Who are you?")

class Administrate(webapp2.RequestHandler):

    def get(self):
        if users.is_current_user_admin():
            self.response.write("Hello, administrator")
        else:
            self.response.write("Sorry, access restricted")

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/sign', Guestbook),
                               ('/profile', Profile),
                               ('/admin', Administrate)],
                              debug=True)