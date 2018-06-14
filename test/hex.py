from game.hexmap import TerrainType, Hex, HexMap, Direction


def test_terrain_set():
    h = Hex(5, 5, TerrainType.t_cty)
    assert h.terrain == TerrainType.t_cty

def test_major_terrain():
    assert TerrainType.major_type_for(TerrainType.t_hll) == TerrainType.t_mtn

def test_minor_terrain():
    assert TerrainType.is_minor_type(TerrainType.t_hll)

def test_direction_equal():
    hm = HexMap(5)
    assert hm.get_neighbor(Hex(3, 3), Direction.NORTH) == Hex(3, 2)

def test_hex_objects_equal():
    a = Hex(3, 3)
    b = Hex(4, 5)
    c = Hex(3, 3)
    assert a is c
    assert a is not b

def test_hex_range():
    hm = HexMap(5)
    print(list(hm.get_hexes_in_range(Hex(0, 0), 1)))
    assert set(hm.get_hexes_in_range(Hex(2, 2), 1)) == {Hex(2, 2),
                                                   Hex(3, 2),
                                                   Hex(3, 1),
                                                   Hex(2, 1),
                                                   Hex(1, 2),
                                                   Hex(1, 3),
                                                   Hex(2, 3)}