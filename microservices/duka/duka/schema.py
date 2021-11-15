"""Collection of graphql schema."""
CREATE_SEATS = """
mutation CreateSeats($objects: [seat_insert_input!]!) {
  insert_seat(objects: $objects) {
    affected_rows
  }
}
"""
