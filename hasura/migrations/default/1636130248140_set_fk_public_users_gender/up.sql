alter table "public"."users"
  add constraint "users_gender_fkey"
  foreign key ("gender")
  references "public"."users_gender"
  ("value") on update restrict on delete restrict;
