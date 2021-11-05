alter table "public"."users"
  add constraint "users_role_fkey"
  foreign key ("role")
  references "public"."users_role"
  ("value") on update restrict on delete restrict;
