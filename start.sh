
celery -A worker.celery worker --loglevel=info &

#!/bin/bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:$PORT