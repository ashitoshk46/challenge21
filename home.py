from base import BaseHandler


class HomeHandler(BaseHandler):
    def get(self):
        #self.write("In the home@get")
        self.render("home.html", title="Home Page")

    def post(self):
        return
