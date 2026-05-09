#!/bin/sh

echo "Starting Celery worker..."
celery -A config worker -l info