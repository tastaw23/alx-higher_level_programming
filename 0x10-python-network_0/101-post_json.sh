#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file as the request body
# Displays the body of the response
json_file="$2"
if [ -f "$json_file" ]; then
    response=$(curl -s -X POST -H "Content-Type: application/json" -d @"$json_file" "$1")
    if [[ $response == *"Valid JSON"* ]]; then
        echo "Valid JSON"
    else
        echo "Not a valid JSON"
    fi
else
    echo "File not found"
fi
