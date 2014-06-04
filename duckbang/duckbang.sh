#!/bin/bash

query_string="!"

for arg in "$@"
do
    query_string="$query_string$arg " 
done

query_string=`python -c "from urllib import urlencode; print urlencode({'q':'$query_string'});"`

echo "Loading $query_string"

lynx "https://duckduckgo.com/lite/?$query_string"
