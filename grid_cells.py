from pd_main import *

class Cells:

  def __init__(self, position, blocks):
    self.position = position # (x, y)
    self.num_of_blocks = blocks
    self.isActive = True

  def is_empty(self):
    return self.num_of_blocks == 0

  def is_full(self):
    return self.num_of_blocks == 5

  # def is_active(self):
  #   return self.active == True

  # def deactivateCell(self):
  #   self.isActive = False