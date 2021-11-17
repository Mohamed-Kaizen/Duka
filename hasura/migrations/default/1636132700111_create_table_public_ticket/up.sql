CREATE TABLE "public"."ticket" ("id" uuid NOT NULL DEFAULT gen_random_uuid(), "code" text NOT NULL, "total_passenger" integer NOT NULL, "status" text NOT NULL, "seat" uuid NOT NULL, "trip" uuid NOT NULL, "bus" uuid NOT NULL, "customer" uuid, "operator" uuid, "ticketer" uuid, "created_at" timestamptz NOT NULL DEFAULT now(), "updated_at" timestamptz NOT NULL DEFAULT now(), PRIMARY KEY ("id") , FOREIGN KEY ("status") REFERENCES "public"."ticket_status"("value") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("trip") REFERENCES "public"."trip"("id") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("bus") REFERENCES "public"."bus"("id") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("customer") REFERENCES "public"."users"("id") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("operator") REFERENCES "public"."users"("id") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("ticketer") REFERENCES "public"."users"("id") ON UPDATE restrict ON DELETE restrict, UNIQUE ("code"));
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
CREATE TRIGGER "set_public_ticket_updated_at"
BEFORE UPDATE ON "public"."ticket"
FOR EACH ROW
EXECUTE PROCEDURE "public"."set_current_timestamp_updated_at"();
COMMENT ON TRIGGER "set_public_ticket_updated_at" ON "public"."ticket" 
IS 'trigger to set value of column "updated_at" to current timestamp on row update';
CREATE EXTENSION IF NOT EXISTS pgcrypto;
