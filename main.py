#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import datetime
from google.appengine.ext import db
import webapp2
import time
import sys
import random
import twython
from twython import Twython, TwythonError
from google.appengine.ext import db

CONSUMER_KEY = ‘???’
CONSUMER_SECRET = ‘???’
ACCESS_KEY = ‘???’
ACCESS_SECRET = ‘???’

from datetime import *
today = date.today()
future = date(2018,11,5)
diff = future - today
NUMBER = diff.days

twitter = twython.Twython(
                          CONSUMER_KEY,
                          CONSUMER_SECRET,
                          ACCESS_KEY,
                          ACCESS_SECRET
                          )

photo = open("%s.jpg" %NUMBER,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status="%s days until the United States Midterm Elections on November 6th, 2018. #election2018 #campaign2018 #politics" %NUMBER, media_ids=[response['media_id']])

