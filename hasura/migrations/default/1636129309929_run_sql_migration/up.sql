CREATE TABLE users_role (
  value text PRIMARY KEY,
  comment text
);

CREATE TABLE users_gender (
  value text PRIMARY KEY,
  comment text
);


CREATE TABLE notification_type (
  value text PRIMARY KEY,
  comment text
);

CREATE TABLE seat_status (
  value text PRIMARY KEY,
  comment text
);

CREATE TABLE ticket_status (
  value text PRIMARY KEY,
  comment text
);


CREATE TABLE payment_method (
  value text PRIMARY KEY,
  comment text
);


INSERT INTO users_role (value, comment) VALUES
  ('admin', 'Privilege to have full control of the system'),
  ('bus_admin', 'Privilege to control bus, driver, ticketer and trips within the organization'),
  ('ticketer', 'Privilege to create a ticket on the behave user within the organization'),
  ('operator', 'Privilege to create a ticket on the behave user with more payment options within the organization'),
  ('user', 'The customer of the system'),
  ('manager', 'Privilege to access full information within the organization');


INSERT INTO users_gender (value, comment) VALUES
  ('F', 'Female'),
  ('M', 'Male');


INSERT INTO notification_type (value, comment) VALUES
  ('trip', 'Activity that related to Trip'),
  ('payment', 'Activity that related to Payment'),
  ('system', 'Message from the system or admin site');


INSERT INTO seat_status (value, comment) VALUES
  ('Available', 'The seat is available'),
  ('Selected', 'The seat is booked until the user pay'),
  ('Unusable', 'The seat cant be booked by anyone'),
  ('Reserved', 'The seat is booked');


INSERT INTO ticket_status (value, comment) VALUES
  ('Pendding', 'The Customer has not paid yet'),
  ('Paid', 'The Customer has paid'),
  ('UnPaid', 'The Customer didnt paid due the payment deadline'),
  ('Cancelled', 'The seat is booked');



INSERT INTO payment_method (value, comment) VALUES
  ('CBE_Branch', 'Paying by going to CBE Brance'),
  ('CBE_Birr', 'Paying using CBE Birr'),
  ('Cash', 'Paying to the ticketer'),
  ('Awash_Branch', 'Paying by going to Awash Brance'),
  ('Nib_Branch', 'Paying by going to Nib Brance'),
  ('Abyssinia_branch', 'Paying by going to Abyssinia Brance'),
  ('Telebirr', 'Paying use Telebirr');
