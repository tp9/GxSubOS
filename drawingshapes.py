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

import pygame
import math

def DrawRoundRect(surface, color, rect, corner_radius, width=0):
  """Draws a rectangle with rounded corners on the given surface.
  If width=0, draw filled; otherwise, draw just the border."""
  cr = corner_radius
  tl_rect = pygame.Rect(0, 0, cr, cr)
  tr_rect = pygame.Rect(rect.width - cr, 0, cr, cr)
  bl_rect = pygame.Rect(0, rect.height - cr, cr, cr)
  br_rect = pygame.Rect(rect.width - cr, rect.height - cr, cr, cr)
  top_rect = pygame.Rect(cr / 2, 0, rect.width - cr, cr)
  middle_rect = pygame.Rect(0, cr / 2, rect.width, rect.height - cr)
  bottom_rect = pygame.Rect(cr / 2, rect.height - cr, rect.width - cr, cr)
  pygame.draw.rect(surface, color, top_rect, width)
  pygame.draw.rect(surface, color, middle_rect, width)
  pygame.draw.rect(surface, color, bottom_rect, width)
  if width is 0:
    arc_width = cr / 2
  else:
    arc_width = width / 2
  pygame.draw.arc(surface, color, tl_rect, math.pi / 2, math.pi, arc_width)
  pygame.draw.arc(surface, color, tr_rect, 0, math.pi / 2, arc_width)
  pygame.draw.arc(surface, color, bl_rect, math.pi, 1.5 * math.pi, arc_width)
  pygame.draw.arc(surface, color, br_rect, 1.5 * math.pi, 2 * math.pi, arc_width)

def DrawHSeparator(surface, width, height):
  """Draws a horizontal separator with the given width at the given height."""
  sep_color_top = pygame.Color(0, 0, 0, 20)
  sep_color_bottom = pygame.Color(255, 255, 255, 20)
  start_top, end_top = [0, height], [width, height]
  start_bottom, end_bottom = [0, height + 1], [width, height + 1]
  pygame.draw.line(surface, sep_color_top, start_top, end_top, 1)
  pygame.draw.line(surface, sep_color_bottom, start_bottom, end_bottom, 1)

def DrawVSeparator(surface, width, height):
  """Draws a vertical separator with the given height at the given width."""
  sep_color_left = pygame.Color(0, 0, 0, 20)
  sep_color_right = pygame.Color(255, 255, 255, 20)
  start_left, end_left = [width, 0], [width, height]
  start_right, end_right = [width + 1, 0], [width + 1, height]
  pygame.draw.line(surface, sep_color_left, start_left, end_left, 1)
  pygame.draw.line(surface, sep_color_right, start_right, end_right, 1)
