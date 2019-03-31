proc next_generation(cells: openArray[openArray[int]], height: int, width: int): seq[int] {. exportc, dynlib .} =
  let cells_len = len(cells)
  for i in cells:
    echo i
  echo height
  echo width

  for i in 0..<height:
    for j in 0..<width:
      #nw: north west, ne: north east, c: center ...
      let up = (height - 1 + i) mod height
      let down = (i + 1) mod height
      let right = (j + 1) mod width
      let left = (width - 1 + j) mod width
      
      let nw = cells[up*height + left]
      let n  = cells[up*height + j]
      let ne = cells[up*height + right]
      let w  = cells[i*height + left]
      let c  = cells[i*height + j]
      let e  = cells[i*height + right]
      let sw = cells[down*height + left]
      let s  = cells[down*height + j]
      let se = cells[down*height + right]
      let neighbor_cell_sum = nw + n + ne + w + e + sw + s + se
      
      if c == 0 and neighbor_cell_sum == 3:
        result[i*height + j] = 1
      elif c == 1 and neighbor_cell_sum in [2, 3]:
        result[i*height + j] = 1
      else:
        result[i*height + j] = 0

#let cell = @[1, 0, 1,1, 1, 0,0, 0, 1]
#echo cell
#echo " "
#echo next_generation(cell, 3, 3)
