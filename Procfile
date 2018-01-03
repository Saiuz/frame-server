web: newrelic-admin run-program gunicorn --pythonpath="$PWD/frameserver" wsgi:application
worker: python frameserver/manage.py rqworker default