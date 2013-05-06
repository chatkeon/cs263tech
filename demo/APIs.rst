APIs
=====================================

The following is a list of the APIs available for Google App Engine and a brief description of what they do:

1. App Identity: this API allows your app to obtain its own application ID and other information so that it can reference itself or assert its identity to other applications.
2. Backends: this API allows you to access or get information about the backend instances handling a particular request.
3. Blobstore: this API allows you to serve large data objects to users (i.e. larger than the objects allowed in Datastore).
4. Capabilities: this API allows you to detect unavailable capabilities (due to outages, scheduled downtown, etc.).
5. Channel: this API allows you to create a channel between your application and Google servers so that your application can send messages to JavaScript clients in real time without polling.
6. Datastore: this API allows you to store and retrieve information using GQL (includes a data-modeling API).
7. Google Cloud Endpoints: this API allows you to generate API backends to simplify client access to data from other applications.
8. Images: this API allows you to manipulate image data.
9. Logs: this API allows you to access application and request logs.
10. Mail: this API allows you to send e-mails on behalf of the application of the user (if signed into Google).
11. MapReduce: this API allows you to efficiently process large amounts of data using the MapReduce computing model.
12. Memcache: this API allows you to use a memory cache to speed up datastore access or to hold temporary values.
13. Namespaces: this API allows you to implement multitenancy through the use of separate namespaces.
14. OAuth: this API allows your application to use the OAuth protocol as an OAuth service provider.
15. Prospective Search: this API allows your application to simultaneously match several registered queries against a stream of input documents.
16. Remote: this API allows you to transparently access App Engine services from any Python application.
17. Search: this API allows users to perform searches across structured data within your application (e.g. plain text, html, etc.).
18. Sockets: this API allows your application to use outbound sockets.
19. Task Queues: this API allows your application to perform user-initiated requests and/or background work outside of a user request.
20. URL Fetch: this API allows your application to communicate with other hosts over the Internet through HTTP and HTTPS requests.
21. Users: this API allows you to authenticate users who have accounts with Google, your own app domain, or OpenID, as well as to identify administrators.
22. XMPP: this API allows you to send and receive instant messages from XMPP-compatible services.

For more detailed information, see the API's documentation on Google App Engine: https://developers.google.com/appengine/docs/python/apis.