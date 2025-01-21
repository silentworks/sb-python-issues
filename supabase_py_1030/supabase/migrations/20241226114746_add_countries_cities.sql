create table countries (id serial primary key, name text);

create table cities (
    id serial primary key,
    country_id int8 not null references countries,
    name text
);

-- enable RLS (countries table)
alter table public.countries enable row level security;

-- Policies (countries table)
create policy "anyone can view all countries" on public.countries
as permissive for select 
to public
using (true);

create policy "allow insert for authenticated user" on public.countries
for insert
to authenticated
with check (true);

create policy "allow delete for authenticated user" on public.countries 
as permissive for delete
to authenticated
using (true);
