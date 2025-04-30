# supabase admin delete user

This project is making use of [UV](https://docs.astral.sh/uv/) and the [Supabase CLI](https://supabase.com/docs/guides/local-development/cli/getting-started).

Note the Supabase CLI requires Docker in order to run

### Copy the project down

```sh
npx degit silentworks/sb-python-issues/supabase_admin_delete_user supabase_admin_delete_user
cd supabase_admin_delete_user
npm install
```

### Instructions

#### Local Supabase with the CLI

Start the project with `npx`:

```sh
npx supabase start
```

#### Hosted Supabase

If you prefer to use hosted Supabase copy the content of `supabase/seed.sql` into the [SQL editor](https://supabase.com/dashboard/project/_/sql/new) in the Supabase Dashboard and run it.

Update the `.env` file with the credentials from the Dashboard.

#### Running the project locally

Now run the project using `uv`:

```sh
uv run app.py
```