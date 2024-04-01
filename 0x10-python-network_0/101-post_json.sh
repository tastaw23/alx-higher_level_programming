#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file as the request body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
