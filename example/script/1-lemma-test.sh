#!/bin/bash

curl -XPOST -H "content-type:application/json" \
-d '{"content":["a", "b", "b"]}' \
http://127.0.0.1:9100/api/ml/lemma
