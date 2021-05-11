import web

urls = ('/hooks')

app = web.application()

class hooks:
    def POST(self):
        data = web.data()
        return 'OK'

if __name__ == '__main__':
    app.run()