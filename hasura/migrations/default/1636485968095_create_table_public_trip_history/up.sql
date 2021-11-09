CREATE TABLE "public"."trip_history" ("id" uuid NOT NULL DEFAULT gen_random_uuid(), "trip" uuid NOT NULL, "driver" uuid NOT NULL, "bus" uuid NOT NULL, "created_at" timestamptz NOT NULL DEFAULT now(), "updated_at" timestamptz NOT NULL DEFAULT now(), PRIMARY KEY ("id") , FOREIGN KEY ("trip") REFERENCES "public"."trip"("id") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("driver") REFERENCES "public"."users"("id") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("bus") REFERENCES "public"."bus"("id") ON UPDATE restrict ON DELETE restrict);
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
CREATE TRIGGER "set_public_trip_history_updated_at"
BEFORE UPDATE ON "public"."trip_history"
FOR EACH ROW
EXECUTE PROCEDURE "public"."set_current_timestamp_updated_at"();
COMMENT ON TRIGGER "set_public_trip_history_updated_at" ON "public"."trip_history" 
IS 'trigger to set value of column "updated_at" to current timestamp on row update';
CREATE EXTENSION IF NOT EXISTS pgcrypto;
