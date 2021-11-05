alter table "public"."route"
  add constraint "route_from_fkey"
  foreign key ("from")
  references "public"."address"
  ("id") on update restrict on delete restrict;
