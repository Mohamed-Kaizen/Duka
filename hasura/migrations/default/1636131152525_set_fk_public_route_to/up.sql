alter table "public"."route"
  add constraint "route_to_fkey"
  foreign key ("to")
  references "public"."address"
  ("id") on update restrict on delete restrict;
