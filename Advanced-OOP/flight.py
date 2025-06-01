"""
Flight Leg:
GLA -> LHR -> CAN

2 segments (GLA -> LHR, LHR -> CAN)
"""
from typing import List


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)
        return " -> ".join(stops)

    @property
    def departure_point(self) -> str:
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, value):
        dest = self.segments[0].destination
        self.segments[0] = Segment(value, dest)

    @property
    def destiny_point(self) -> str:
        return self.segments[-1].destination

    @destiny_point.setter
    def destiny_point(self, value):
        dep = self.segments[-1].departure
        self.segments[-1] = Segment(dep, value)


flight = Flight([Segment("GLA", "LHR"), Segment("LHR", "CAN")])
print(flight.departure_point)
print(flight)

flight.departure_point = "EDI"
print(flight.departure_point)
print(flight)

flight.destiny_point = "BOS"
print(flight.destiny_point)
print(flight)
