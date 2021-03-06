# This file is part of GxSubOS.
# Copyright (C) 2014 Christopher Kyle Horton <christhehorton@gmail.com>

# GxSubOS is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# GxSubOS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GxSubOS. If not, see <http://www.gnu.org/licenses/>.

from pygame.locals import *

def GetCharFromKey(keydown):
  '''Returns the proper Unicode value we want to work with from a given
  pygame.KEYDOWN event.'''
  if keydown.key == K_RETURN:
    # Correctly add newlines to strings instead of carriage returns
    return '\n'
  return keydown.unicode
