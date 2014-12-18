import backports
import backports.ssl_match_hostname

def find_tornado():
    import sys
    import os.path
    import rospkg
    rpkg = rospkg.RosPack()
    sys.path = [
        os.path.split(__file__)[0],
        os.path.join(rpkg.get_path('rosbridge_tools'), 'src/rosbridge_tools'),
        ] + sys.path
    print sys.path
    import tornado
    import tornado.platform
    import tornado.ioloop
    import tornado.web
    import tornado.websocket
    sys.path = sys.path[2:]
    assert(tornado.version == '4.0.2')
    return tornado

