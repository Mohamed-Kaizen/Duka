alter table "public"."seat"
  add constraint "seat_status_fkey"
  foreign key ("status")
  references "public"."seat_status"
  ("value") on update restrict on delete restrict;
