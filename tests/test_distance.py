from mlproject.distance import haversine
def test_distance():
    result=haversine(20,50,30,40)
    assert type(result)== float
