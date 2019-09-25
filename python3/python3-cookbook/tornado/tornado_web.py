import hashlib

import tornado.ioloop
from flask.json.tag import TaggedJSONSerializer
from itsdangerous import URLSafeTimedSerializer
from tornado.web import RequestHandler, url, Application
from tornado import web
import json

def get_current_user_idex(secret_cookie, secret_key):
    if not secret_cookie:
        return

    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    try:
        session = s.loads(secret_cookie)
        return session['user']
    except Exception as err:
        raise err


class MainHandler(RequestHandler):
    name = dict()

    def get(self):
        self.write("Hello tornado\n")
        self.write("Hello tornado\n")
        self.name = self.get_arguments("name")
        print(self.name)
        self.write(str(self.name))


class StoryHandler(RequestHandler):
    def initialize(self, db, id):
        self.db = db
        self.id = id

    # 在每个请求最开始的时候调用
    def prepare(self):
        print("storyhandler prepare")

    def get(self, story_id):
        self.write("this is story %s" % str(self.db)+str(self.id))

    # 用于清理，在请求结束后调用
    def on_finish(self):
        print("on finish")


class MyFormHandler(RequestHandler):
    def post(self):
        self.set_header("Content-Type", "application/json")

        body = json.loads(self.request.body)
        if not body:
            model = body.get("key", "no key")

            print(model)

        self.write("You wrote " + self.get_body_argument("key"))


class BaseHandler(RequestHandler):
    def get_current_user(self):
        """Get current username from idex session"""
        secret_cookie = self.get_cookie('session', {})
        secret_key = "A0s3r98j/3ys R~XHH!3mN4LWX/,?RT"
        session = get_current_user_idex(secret_cookie, secret_key=secret_key)
        if not session:
            raise web.HTTPError(status_code=403, log_message='Not Authentication')
        username = session.get('name')
        # user = self.user_from_username(username)
        # self.set_login_cookie(user)
        return username

class UserHandler(BaseHandler):

    def get(self):
        session = self.get_current_user()
        self.write(session)






default_request = [
    url(r'/', MainHandler),
    # url(r'/story/([0-9]+)', StoryHandler, dict(db="db", id=2)),
    url(r'/myform/', MyFormHandler),
    # url(r'/user/', UserHandler)
]


def make_app():
    return tornado.web.Application(default_request)

if __name__ == '__main__':
    app=make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()

