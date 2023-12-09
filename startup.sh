#!/bin/bash

. .env

# $BIN --host "0.0.0.0" --port 9000 app:app --reload
$BIN --workers $WORKER --host "0.0.0.0" --port $PORT app:app \
--access-log --log-level $LOGLEVEL \
--env-file .env
