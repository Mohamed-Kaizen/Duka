CREATE TABLE "public"."bus" ("id" uuid NOT NULL DEFAULT gen_random_uuid(), "licence_number" text NOT NULL, "total_seat" integer NOT NULL, "driver" uuid NOT NULL, "trip" uuid NOT NULL, "organization" uuid NOT NULL, "is_active" boolean NOT NULL DEFAULT true, "created_at" timestamptz NOT NULL DEFAULT now(), "updated_at" timestamptz NOT NULL DEFAULT now(), PRIMARY KEY ("id") , FOREIGN KEY ("driver") REFERENCES "public"."users"("id") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("trip") REFERENCES "public"."trip"("id") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("organization") REFERENCES "public"."organization"("id") ON UPDATE restrict ON DELETE restrict, UNIQUE ("licence_number"));
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
CREATE TRIGGER "set_public_bus_updated_at"
BEFORE UPDATE ON "public"."bus"
FOR EACH ROW
EXECUTE PROCEDURE "public"."set_current_timestamp_updated_at"();
COMMENT ON TRIGGER "set_public_bus_updated_at" ON "public"."bus" 
IS 'trigger to set value of column "updated_at" to current timestamp on row update';
CREATE EXTENSION IF NOT EXISTS pgcrypto;
