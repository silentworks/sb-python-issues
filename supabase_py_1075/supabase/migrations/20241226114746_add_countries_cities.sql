create table countries (id serial primary key, name text);

create table cities (
    id serial primary key,
    country_id int8 not null references countries,
    name text
);

