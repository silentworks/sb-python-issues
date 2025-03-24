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

