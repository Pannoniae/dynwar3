from game.hex import TerrainType, Hex


def test_terrain_set():
    h = Hex(5, 5, TerrainType.t_cty)
    assert h.terrain == TerrainType.t_cty

def test_major_terrain():
    assert TerrainType.majorType(TerrainType.t_hll) == TerrainType.t_mtn