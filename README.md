Feature Flag
======

This project was created from a Flask/Python template app and altered by Angela Lui.

Objective
-------

Evaluating whether a user is more likely to engage with the app when site is more colorful.

*Feature flag*: Targeted users will see pink header variant vs the default blue. 

<img src="https://i.imgur.com/p21t0Y5.png"
     alt="Pink Feature Flag Shown"
     width="200"/>

About the app
----

This is a basic blogging app called Flaskr that allows users to create users, log in, and create/edit/delete posts. 

The Code
 * ld.py - Imports LaunchDarkly client and initializes an instance using my SDK key. Also makes sure the instance is closed at the end of the session.
 * blog.py - Index function shows all posts from the database. Within the function it checks to see if the user has been authenticated (logged in), and if this is true, to set user's ID as the LD user key. If the user has a key, then the ldclient will look up the user's variation for the pink_headers feature flag. The variation variable is sent to blog/index.html template. 
 * /static/style.css - created new class 'pink' for pink font
 * /templates/blog/index.html - h1 header checks the flag, if pink_headers is true, show class pink, otherwise, it's the default template. 
 

Install
-------
Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Install Flask::

    $ pip install flask

Install LaunchDarkly's SDK::

    $ pip install launchdarkly-server-sdk

Run
---
::

    $ flask run

Open http://127.0.0.1:5000 in a browser.

  
