from game.hexmap import TerrainType, Hex


def test_terrain_set():
    h = Hex(5, 5, TerrainType.t_cty)
    assert h.terrain == TerrainType.t_cty

def test_major_terrain():
    assert TerrainType.major_type_for(TerrainType.t_hll) == TerrainType.t_mtn

def test_minor_terrain():
    assert TerrainType.is_minor_type(TerrainType.t_hll)