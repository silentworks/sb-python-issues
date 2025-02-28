# supabase-py phone password signup

This project is making use of [UV](https://docs.astral.sh/uv/) and the [Supabase CLI](https://supabase.com/docs/guides/local-development/cli/getting-started).

Note the Supabase CLI requires Docker in order to run

### Copy the project down

```sh
npx degit silentworks/sb-python-issues/supabase_phone_password_signup supabase_phone_password_signup
cd supabase_phone_password_signup
npm install
```

### Instructions

Start the project with `npx`:

```sh
npx supabase start
```

Now run the project using `uv`:

```sh
uv run uvicorn app.main:app --reload
```

Then visit http://127.0.0.1:8000/docs and test it out.
