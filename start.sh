#!/bin/bash
python -m textblob.download_corpora
gunicorn sentiment_api:app --bind 0.0.0.0:$PORT