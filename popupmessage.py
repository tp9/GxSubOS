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
import glass

title_font = pygame.font.Font("fonts/Roboto/Roboto-Bold.ttf", 32)
message_font = pygame.font.Font("fonts/Roboto/Roboto-Regular.ttf", 16)
button_font = pygame.font.Font("fonts/Roboto/Roboto-Bold.ttf", 16)
padding = 32

class PopupMessage():
  """A class for diplaying popup messages to the user.
  This is meant to be comparable to using show_message() in GameMaker."""
  popup_color = glass.glass_color
  popup_color.a = glass.glass_alpha
  
  def __init__(self, title_text="Untitled", message_text="(No message.)"):
    self.title_text = title_text
    self.message_text = message_text
    self.surface = pygame.Surface((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.SRCALPHA)
    self.gradient_surface = pygame.image.load("graphics/popupmessage_bkg_gradient.png")
    self.gradient_surface = pygame.transform.smoothscale(self.gradient_surface, (pygame.display.Info().current_w, pygame.display.Info().current_h))
    self.Redraw()

  def Redraw(self, surface=None):
    """Redraws this PopupMessage's surface."""
    self.surface.fill((0, 0, 0, 0))
    title_surface = title_font.render(self.title_text, True, glass.accent_color)
    message_surface = message_font.render(self.message_text, True, glass.accent_color)
    message_pos = (self.surface.get_width() / 2 - message_surface.get_width() / 2, self.surface.get_height() / 2)
    title_pos = (message_pos[0], self.surface.get_height() / 2 - title_surface.get_height())
    window_rect = pygame.Rect(title_pos[0] - padding, title_pos[1] - padding, message_surface.get_width() + 2 * padding, title_surface.get_height() + message_surface.get_height() + 2 * padding)
    window_surface = pygame.Surface(window_rect.size, pygame.SRCALPHA)
    window_surface.fill(self.popup_color)
    if surface != None:
      self.surface.blit(glass.Blur(surface), (0, 0))
    self.surface.blit(self.gradient_surface, (0, 0))
    self.surface.blit(window_surface, window_rect)
    self.surface.blit(title_surface, title_pos)
    self.surface.blit(message_surface, message_pos)
