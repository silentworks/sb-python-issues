INSERT INTO "auth"."users" ("instance_id", "id", "aud", "role", "email", "encrypted_password", "email_confirmed_at", "invited_at", "confirmation_token", "confirmation_sent_at", "recovery_token", "recovery_sent_at", "email_change_token_new", "email_change", "email_change_sent_at", "last_sign_in_at", "raw_app_meta_data", "raw_user_meta_data", "is_super_admin", "created_at", "updated_at", "phone", "phone_confirmed_at", "phone_change", "phone_change_token", "phone_change_sent_at", "email_change_token_current", "email_change_confirm_status", "banned_until", "reauthentication_token", "reauthentication_sent_at", "is_sso_user") VALUES
('00000000-0000-0000-0000-000000000000', 'd0fc7e46-a8a5-4fd4-8ba7-af485013e6fa', 'authenticated', 'authenticated', 'up+rosamond_damore@example.com', crypt('password123', gen_salt('bf')), '2023-02-18 23:31:13.017218+00', NULL, '', '2023-02-18 23:31:12.757017+00', '', NULL, '', '', NULL, '2023-02-18 23:31:13.01781+00', '{"provider": "email", "providers": ["email"]}', '{}', NULL, '2023-02-18 23:31:12.752281+00', '2023-02-18 23:31:13.019418+00', NULL, NULL, '', '', NULL, '', 0, NULL, '', NULL, 'f');

with country as (
  insert into countries (name)
  values ('Germany') returning id
)
insert into cities (name, country_id) values
('Munich', (select id from country)),
('Berlin', (select id from country)),
('Frankfurt', (select id from country)),
('Cologne', (select id from country));

with country as (
  insert into countries (name)
  values ('Indonesia') returning id
)
insert into cities (name, country_id) values
('Jakarta', (select id from country)),
('Surabaya', (select id from country)),
('Bandung', (select id from country)),
('Bekasi', (select id from country));

with country as (
  insert into countries (name)
  values ('France') returning id
)
insert into cities (name, country_id) values
('Paris', (select id from country)),
('Nice', (select id from country));

with country as (
  insert into countries (name)
  values ('United Kingdom') returning id
)
insert into cities (name, country_id) values
('London', (select id from country)),
('Manchester', (select id from country)),
('Liverpool', (select id from country)),
('Bristol', (select id from country));
