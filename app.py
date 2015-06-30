import tornado.web
import tornado.ioloop

from temboo.Library.Tumblr.Post import RetrievePublishedPosts
from temboo.core.session import TembooSession
from tornado.escape import json_decode, json_encode


session = TembooSession("jordanemedlock", "jordanemedlockcom", "aB8hQizrTLhyOUitwNdnxvddWa3Fw6ZG")
choreo = RetrievePublishedPosts(session)

def readJSON(fileName):
    f = open(fileName)
    return json_decode(f.read())

def writeJSON(fileName, json):
    f = open(fileName, 'w')
    f.write(json_encode(json))

def getTags(update=True):
    if update:
        posts, num_posts = getPosts(0)
        high = num_posts/10+1
        print high
        for page in xrange(1,high):
            posts2, _ = getPosts(page)
            posts += posts2
        tags = dict()
        for post in posts:
            for tag in post['tags']:
                if tag in tags:
                    tags[tag] += 1
            else:
                tags[tag] = 1
        return posts, tags
    else:
        return readJSON('tags.json')

def matches(query):
    def inner(post):
        def exists(name, d):
            return name in d and d[name] is not None
        tagMatches = query in post['tags']
        titleMatches = exists('title',post) and query.lower() in post['title'].lower()
        bodyMatches = exists('body', post) and query.lower() in post['body'].lower()
        return tagMatches or titleMatches or bodyMatches
    return inner

def getPosts(page=None, update=True, tag=None, query=None, slug=None):
    if update:
        page = int(page or 0)
        choreo_inputs = choreo.new_input_set()

        choreo_inputs.set_APIKey("u06kxugAWrGDtTxfU5IikKXg8oXyfFO8JqabS5HDyq3qPYquHH")
        choreo_inputs.set_BaseHostname("cs-alloc-init.tumblr.com")
        choreo_inputs.set_Limit("10")
        choreo_inputs.set_Offset(str(page * 10))

        results = choreo.execute_with_results(choreo_inputs)

        results = json_decode(results.get_Response())

        return results['response']['posts'], results['response']['total_posts']
    else:
        posts = readJSON("posts.json")
        if tag is not None:
            posts = filter(lambda x: tag in x['tags'], posts)
        if query is not None:
            posts = filter(matches(query), posts)
        if slug is not None:
            posts = filter(lambda x: x['slug'] == slug, posts)
        return posts, len(posts)


class MainHandler(tornado.web.RequestHandler):
    def get(self,page):
        page = int(page or 0)

        posts, num_posts = getPosts(page,update=False)

        self.render("home.html",posts=posts,big=False)

class PostHandler(tornado.web.RequestHandler):
    def get(self,slug):
        slug = slug or None

        posts, num_posts = getPosts(None,update=False)

        prev_post=None
        next_post=None
        this_post=None
        for post in posts:
            if post['slug'] == slug:
                this_post = post
                continue
            if this_post is None:
                prev_post = post
            else:
                next_post = post
                break
        if this_post is not None:
            posts = [this_post]
        self.render("home.html",
                    posts=posts,
                    big=True,
                    this_post=this_post,
                    next_post=next_post,
                    prev_post=prev_post)

class UpdateHandler(tornado.web.RequestHandler):
    def get(self):
        posts, tags = getTags()
        writeJSON("posts.json", posts)
        writeJSON("tags.json", tags)
        print "all done"
        self.redirect('/')

class BioHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("bio.html")


settings = {
    "autoreload": True,
    "compiled_template_cache": False,
    "template_path": "templates",
    "static_hash_cache": False,
    "static_path": "static"
}

application = tornado.web.Application([
    (r"/([0-9]*)", MainHandler),
    (r"/update", UpdateHandler),
    (r"/bio", BioHandler),
    (r"/post/(.*)", PostHandler),
], **settings)

if __name__ == "__main__":
    application.listen(3000)
    tornado.ioloop.IOLoop.current().start()
