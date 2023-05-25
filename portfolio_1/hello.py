import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['content-type']='text/plain'
        self.response.out.write("heelo world")
app=webapp2.WSGIApplication([('/',MainPage)], debug=True)
