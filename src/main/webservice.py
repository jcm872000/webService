import tornado.ioloop
import tornado.web
import xml.dom.minidom
from xml.dom.minidom import Document
CMD_Str_path = "../res/meta/cmd.xml"
CMD_dom = xml.dom.minidom.parse(CMD_Str_path)
command_lists = CMD_dom.getElementsByTagName("command")

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello world")

class MetaHandler(tornado.web.RequestHandler):
	def get(self):
		for command_node in command_lists:
			print command_node.childNodes[0].data
			self.write(command_node.childNodes[0].data+"<br/>")

application = tornado.web.Application([(r"/main/", MainHandler),])
application = tornado.web.Application([(r"/run/", MetaHandler),])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
