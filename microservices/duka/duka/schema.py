"""Collection of graphql schema."""
CREATE_SEATS = """
mutation CreateSeats($objects: [seat_insert_input!]!) {
  insert_seat(objects: $objects) {
    affected_rows
  }
}
"""


CREATE_TRIP_HISTORY = """
mutation CreateTripHistory($bus: uuid!, $driver: uuid!, $trip: uuid!) {
  insert_trip_history_one(object: {bus: $bus, driver: $driver, trip: $trip}) {
    id
  }
}
"""


GET_BUS = """
query GetBus($id: uuid!) {
  bus_by_pk(id: $id) {
    id
    driver
    seats {
      id
    }
  }
}
"""


CREATE_TRIP_BUS_SEATS = """
mutation CreateTripBusSeat($objects: [trip_bus_seat_insert_input!]!) {
  insert_trip_bus_seat(objects: $objects) {
    affected_rows
  }
}
"""
