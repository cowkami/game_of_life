import sequtils
import nimpy

proc next_generation(cells: seq[seq[int]]): seq[seq[int]] {.exportpy.} =
  let width = cells[0].len
  let height = cells.len
  result = newSeqWith(height, newSeq[int](width))

  for i in 0..<height:
    for j in 0..<width:
      #nw: north west, ne: north east, c: center ...
      let up = (height - 1 + i) mod height
      let down = (i + 1) mod height
      let right = (j + 1) mod width
      let left = (width - 1 + j) mod width
      
      let nw = cells[up][left]
      let n  = cells[up][j]
      let ne = cells[up][right]
      let w  = cells[i][left]
      let c  = cells[i][j]
      let e  = cells[i][right]
      let sw = cells[down][left]
      let s  = cells[down][j]
      let se = cells[down][right]
      
      let neighbor_cell_sum = nw + n + ne + w + e + sw + s + se
      
      if c == 0 and neighbor_cell_sum == 3:
        result[i][j] = 1
      elif c == 1 and neighbor_cell_sum in [2, 3]:
        result[i][j] = 1
      else:
        result[i][j] = 0
