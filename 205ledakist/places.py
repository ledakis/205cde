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
import os
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class placesmain(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('places.html')
        self.response.write(template.render())

class places(webapp2.RequestHandler):
    def get(self):
        # template = JINJA_ENVIRONMENT.get_template('history.html')
        # self.response.write(template.render())
        self.response.write('eleos')

app = webapp2.WSGIApplication([
    (r'/places/?', placesmain),
    (r'/place/(.*)', places)

], debug=True)
