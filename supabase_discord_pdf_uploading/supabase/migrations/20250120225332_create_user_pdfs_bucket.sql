-- Set up storage for user_pdfs
insert into storage.buckets (id, name, public)
  values ('user_pdfs', 'user_pdfs', true);

-- Set up access controls for storage.
-- See https://supabase.com/docs/guides/storage#policy-examples for more details.
create policy "User images are publicly accessible." on storage.objects
for select 
using (bucket_id = 'user_pdfs');

create policy "Anyone can upload an user_pdfs." on storage.objects
for insert
with check (bucket_id = 'user_pdfs');

create policy "A user can update their own user_pdfs." on storage.objects
for update 
using (true) 
with check (bucket_id = 'user_pdfs');

create policy "A user can delete their own user_pdfs." on storage.objects
for delete
using (true)
