CREATE TABLE "public"."payment_history" ("id" uuid NOT NULL DEFAULT gen_random_uuid(), "total_price" numeric NOT NULL, "system_price" numeric NOT NULL, "ticket" uuid NOT NULL, "method" text NOT NULL, "created_at" timestamptz NOT NULL DEFAULT now(), "updated_at" timestamptz NOT NULL DEFAULT now(), PRIMARY KEY ("id") , FOREIGN KEY ("ticket") REFERENCES "public"."ticket"("id") ON UPDATE restrict ON DELETE restrict, FOREIGN KEY ("method") REFERENCES "public"."payment_method"("value") ON UPDATE restrict ON DELETE restrict);
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
CREATE TRIGGER "set_public_payment_history_updated_at"
BEFORE UPDATE ON "public"."payment_history"
FOR EACH ROW
EXECUTE PROCEDURE "public"."set_current_timestamp_updated_at"();
COMMENT ON TRIGGER "set_public_payment_history_updated_at" ON "public"."payment_history" 
IS 'trigger to set value of column "updated_at" to current timestamp on row update';
CREATE EXTENSION IF NOT EXISTS pgcrypto;
