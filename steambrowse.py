#!/usr/bin/env python3

import os
import subprocess
import sys
from twisted.internet import reactor
from twisted.web import resource, server, static

# DEFAULTS
SERVER_PORT = 8080
STEAM_LOGIN = 'anonymous'

steamcmd = None

# Combined static and dynamic server based on https://mtrpcic.net/blog/twisted-static-content-with-dynamic-pages/
class SteamWorkshop(resource.Resource):
    isLeaf = False

    def getChild(self, name, request):
        print(name)
        print(request.args)
        if name == b'browse':
            return self
        return resource.Resource.getChild(self, name, request)

    def render_GET(self, request):
        global steamcmd

        appid_b = request.args[b'appid'][0]
        appid = appid_b.decode('utf-8')
        itemid_b = request.args[b'itemid'][0]
        itemid = itemid_b.decode('utf-8')

        if steamcmd is not None and steamcmd.poll() is None:
            return b'<html><body>steamcmd is busy...<br /><input type="button" value="Refresh" onclick="window.location.reload()" /></body></html>'
        elif os.path.isdir(os.path.join(os.getcwd(), 'steamapps', 'content', 'app_'+appid, 'item_'+itemid)):
            return b'<html><head><meta http-equiv="refresh" content="0; url=/content/app_' + appid_b + b'/item_' + itemid_b + b'/"></head><body>Exists</body></html>'
        else:
            steamcmd = subprocess.Popen(['steamcmd.exe', '+login', STEAM_LOGIN, '+download_item', appid, itemid, '+quit'])
            return b'<html><body>Downloading resource...<br /><input type="button" value="Refresh" onclick="window.location.reload()" /></body></html>'

if __name__ == "__main__":
    if len(sys.argv) == 3:
        STEAM_LOGIN = sys.argv[1]
        SERVER_PORT = int(sys.argv[2])
    print("Login: " + STEAM_LOGIN)
    print("Port: " + str(SERVER_PORT))

    print("Starting Twisted...")
    root = SteamWorkshop()
    root.putChild(b'content', static.File('./steamapps/content'))
    site = server.Site(root)
    reactor.listenTCP(SERVER_PORT, site)
    reactor.run()
