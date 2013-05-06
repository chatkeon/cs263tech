Development Setup
=====================================

First of all, sign up for an account on Google App Engine. Then, download the GAE SDK appropriate for your system according to the instructions online.

To create a web app:

1. Create a directory to hold your files.
2. Write your source code (.py files).
3. Create a configuration file, app.yaml.
4. Create other files as necessary (index.yaml, index.html, etc.).
5. Run your app using the SDK.
6. Test and debug your app. The development server supplied with the SDK can run in the background and will reflect your changes when you refresh the browser.
7. When your app is ready, go to your GAE account and create an application. Make sure your applicationID matches your application name.
8. Deploy your app!

Other information:

* GAE includes a simple, lightweight, Python web framework called webapp2. This is bundled into the GAE SDK, so it is easy and convenient to use. For more information, see the webapp2 documentation: webapp-improved.appspot.com.
* GAE supports HTML and CSS so that you can design the view and layout of your app. Included is support for Django and Jinja2 templates.
