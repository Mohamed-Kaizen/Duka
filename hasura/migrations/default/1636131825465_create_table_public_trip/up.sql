CREATE TABLE "public"."trip" ("id" uuid NOT NULL DEFAULT gen_random_uuid(), "departure_location" text NOT NULL, "departure_time" timestamptz NOT NULL, "arrival_time" timestamptz NOT NULL, "payment_deadline" timestamptz NOT NULL, "organization" uuid NOT NULL, "route" uuid NOT NULL, "created_at" timestamptz NOT NULL DEFAULT now(), "updated_at" timestamptz NOT NULL DEFAULT now(), PRIMARY KEY ("id") , FOREIGN KEY ("organization") REFERENCES "public"."organization"("id") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("route") REFERENCES "public"."route"("id") ON UPDATE restrict ON DELETE restrict);
CREATE OR REPLACE FUNCTION "public"."set_current_timestamp_updated_at"()
RETURNS TRIGGER AS $$
DECLARE
  _new record;
BEGIN
  _new := NEW;
  _new."updated_at" = NOW();
  RETURN _new;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER "set_public_trip_updated_at"
BEFORE UPDATE ON "public"."trip"
FOR EACH ROW
EXECUTE PROCEDURE "public"."set_current_timestamp_updated_at"();
COMMENT ON TRIGGER "set_public_trip_updated_at" ON "public"."trip" 
IS 'trigger to set value of column "updated_at" to current timestamp on row update';
CREATE EXTENSION IF NOT EXISTS pgcrypto;
