Curtis Complaint Counter
========================

This is a slack integration to track Curtis La Graff's complaints.

Development Quickstart
----------------------

#. Create a virtual environment

#. Run ``setup.py develop``

   ::

     python setup.py develop

Deployment
----------

After installing via ``setup.py`` run the following:

::

  $ deploy

This will update the Lambda endpoint that the API Gateway routes Slack-integration's requests to.
