import ldclient
from ldclient.config import Config

from flask import g

def get_ld_client():
    #if this was an app in prod, keey would go in secret file
    #hard-coding as a shortcut for now! 
    if "ld_client" not in g:
        ldclient.set_config(Config("sdk-6d5668a8-bca4-43e8-a4ed-aae8b501be6c"))
        g.ld_client = ldclient.get()

    return g.ld_client

def close_ld_client(e=None):
    ld_client = g.pop("ld_client", None)

    if ld_client is not None:
        ld_client.close()

def init_app(app):
    """Register teardown function with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_ld_client)
    # shut down the client, since we're about to quit
