import tornado.web
import tornado.ioloop
import json


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("this is command from python backend")


class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class queryParameterRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("number")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(f"{num} is  {r}")
        else:
            self.write(f"{num} isn't a invalid parameter")


class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseId):
        self.write(
            f"welcome {studentName} ! The course you are viewing is {courseId}")


class mainListRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("list.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))

    def post(self):
        fruit = self.get_argument("fruit")
        fh = open("list.txt", "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added succesfully"}))


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/animals", listRequestHandler),
        (r"/isEven", queryParameterRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler),
        (r"/list", mainListRequestHandler)
    ])

    port = 8882

    app.listen(port)
    print(f"server is up and runnnig at port {port}")
    tornado.ioloop.IOLoop.current().start()
