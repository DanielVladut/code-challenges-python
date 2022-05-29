# given a number of tiles, on each tile there is a number that indicates over how many tiles to jump
# compute if it is possible to go beyond the last tile starting from the first tile.

def jump(tiles):
    if (len(tiles) == 0):
        return False
    i = 0
    while(i < len(tiles)):
        tile_value = tiles[i]
        if tile_value == 0:
            return False
        i = i + tile_value

    return True

def test_jump():
    assert jump([5,0,0,0]) == True
    assert jump([1,1,1,1]) == True
    assert jump([1,1,2,0]) == True
    assert jump([1,1,1,0]) == False
    assert jump([2,1,0,3]) == False
    assert jump([1,0,2])   == False

