# -*- coding: utf-8 -*-

"""
Py Asana Digest is created by Frank Wickström at the Embedded systems lab at Åbo Akademi University
Originally created as a Python port of the Ruby script found at: https://github.com/miyagawa/asana_digest

Copyright (C) 2012  Frank Wickström

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from libs.task import Task
from conf import CONFIG

t = Task(CONFIG).run()
