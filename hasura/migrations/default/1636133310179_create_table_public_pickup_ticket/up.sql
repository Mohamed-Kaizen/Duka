CREATE TABLE "public"."pickup_ticket" ("id" uuid NOT NULL DEFAULT gen_random_uuid(), "pickup" uuid NOT NULL, "ticket" uuid NOT NULL, "pickup_location" text NOT NULL, "created_at" timestamptz NOT NULL DEFAULT now(), "updated_at" timestamptz NOT NULL DEFAULT now(), PRIMARY KEY ("id") , FOREIGN KEY ("pickup") REFERENCES "public"."pickup"("id") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("ticket") REFERENCES "public"."ticket"("id") ON UPDATE restrict ON DELETE restrict);
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
CREATE TRIGGER "set_public_pickup_ticket_updated_at"
BEFORE UPDATE ON "public"."pickup_ticket"
FOR EACH ROW
EXECUTE PROCEDURE "public"."set_current_timestamp_updated_at"();
COMMENT ON TRIGGER "set_public_pickup_ticket_updated_at" ON "public"."pickup_ticket" 
IS 'trigger to set value of column "updated_at" to current timestamp on row update';
CREATE EXTENSION IF NOT EXISTS pgcrypto;
