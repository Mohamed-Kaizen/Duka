CREATE TABLE "public"."trip_bus" ("id" uuid NOT NULL DEFAULT gen_random_uuid(), "trip" uuid NOT NULL, "bus" uuid NOT NULL, "status" text NOT NULL, "created_at" timestamptz NOT NULL DEFAULT now(), "updated_at" timestamptz NOT NULL DEFAULT now(), PRIMARY KEY ("id") , FOREIGN KEY ("trip") REFERENCES "public"."trip"("id") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("bus") REFERENCES "public"."bus"("id") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("status") REFERENCES "public"."trip_bus_status"("value") ON UPDATE restrict ON DELETE restrict);
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
CREATE TRIGGER "set_public_trip_bus_updated_at"
BEFORE UPDATE ON "public"."trip_bus"
FOR EACH ROW
EXECUTE PROCEDURE "public"."set_current_timestamp_updated_at"();
COMMENT ON TRIGGER "set_public_trip_bus_updated_at" ON "public"."trip_bus" 
IS 'trigger to set value of column "updated_at" to current timestamp on row update';
CREATE EXTENSION IF NOT EXISTS pgcrypto;
