
class Cells:
  
  def __init__(self, position, blocks):
    self.position = position # (x, y)
    self.num_of_blocks = blocks
    
  def is_empty(self):
    return self.num_of_blocks is 0
  

