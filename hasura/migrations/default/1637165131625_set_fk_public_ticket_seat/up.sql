alter table "public"."ticket"
  add constraint "ticket_seat_fkey"
  foreign key ("seat")
  references "public"."trip_bus_seat"
  ("id") on update restrict on delete restrict;
