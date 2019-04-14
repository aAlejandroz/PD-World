from pd_main import *
from grid_cells import *
from policies import *

# ------------------- CELL FUNCTIONS ------------------- #

pickup_cells = []   # list of pickup cells
dropoff_cells = []  # list of drop off cells

# decrement blocks on cell #
def decrementNumBlocksInCell(pos):
  cell = getCellFromPosition(pos, pickup_cells)
  cell.num_of_blocks -= 1


# increment blocks on cell #
def incrementNumBlocksInCell(pos):
  cell = getCellFromPosition(pos, dropoff_cells)
  cell.num_of_blocks += 1

# Initialize environment to original #
def initalizeCells(pickup_states, dropoff_states):
  pickup_cells.clear()
  dropoff_cells.clear()

  for pos in pickup_states:
    pickup_cells.append(Cells(pos, 5))

  for pos in dropoff_states:
    dropoff_cells.append(Cells(pos, 0))

# returns the cell object in the given position #
def getCellFromPosition(pos, cell_list):
  for cell in cell_list:
    if cell.position == pos:
      return cell