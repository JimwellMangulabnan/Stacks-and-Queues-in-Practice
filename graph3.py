print("\n\t*********  PROGRAMMED BY  ********")
print("\t***** JIMWELL L. MANGULABNAN *****")
print("\t********** BSCOE 2-2 *************")
print()

from typing import NamedTuple

class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float