#!/bin/bash
# takes in a URL, sends a POST request passed URL, and displays body response
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
