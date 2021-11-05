CREATE TABLE "public"."seat" ("id" uuid NOT NULL DEFAULT gen_random_uuid(), "name" text NOT NULL, "status" text NOT NULL, "bus" uuid NOT NULL, "created_at" timestamptz NOT NULL DEFAULT now(), "updated_at" timestamptz NOT NULL DEFAULT now(), PRIMARY KEY ("id") , FOREIGN KEY ("status") REFERENCES "public"."seat_status"("value") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("bus") REFERENCES "public"."bus"("id") ON UPDATE restrict ON DELETE restrict);
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
CREATE TRIGGER "set_public_seat_updated_at"
BEFORE UPDATE ON "public"."seat"
FOR EACH ROW
EXECUTE PROCEDURE "public"."set_current_timestamp_updated_at"();
COMMENT ON TRIGGER "set_public_seat_updated_at" ON "public"."seat" 
IS 'trigger to set value of column "updated_at" to current timestamp on row update';
CREATE EXTENSION IF NOT EXISTS pgcrypto;
