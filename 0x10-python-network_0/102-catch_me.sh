#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me to cause the server to respond with "You got me!"
curl -s -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
