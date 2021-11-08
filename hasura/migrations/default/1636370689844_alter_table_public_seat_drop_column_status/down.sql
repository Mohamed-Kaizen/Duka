alter table "public"."seat" alter column "status" drop not null;
alter table "public"."seat" add column "status" text;
