import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
		self.render('index.html')
		
class New_AdmissionHandler(tornado.web.RequestHandler):
    def get(self):
		self.render('new_admission.html')

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        n1 = self.get_argument('name')
        n2= self.get_argument('passw')
        self.render('home.html', usern=n1, passw=n2)


application = tornado.web.Application(
	handlers=[(r'/', IndexHandler), (r'/home', PoemPageHandler),(r'/new_admission', New_AdmissionHandler)],
	template_path=os.path.join(os.path.dirname(__file__), "templates"))

def main(address):
    application.listen(8080, address)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    address = "127.0.0.1"
    main(address)