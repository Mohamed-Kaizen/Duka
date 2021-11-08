alter table "public"."bus" drop constraint "bus_trip_fkey",
  add constraint "bus_trip_fkey"
  foreign key ("trip")
  references "public"."trip"
  ("id") on update restrict on delete restrict;
