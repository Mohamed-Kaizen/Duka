alter table "public"."bus" alter column "trip" drop not null;
alter table "public"."bus" add column "trip" uuid;
