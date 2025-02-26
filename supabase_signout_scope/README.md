# supabase-py sign out scope

This project is making use of [UV](https://docs.astral.sh/uv/) and the [Supabase CLI](https://supabase.com/docs/guides/local-development/cli/getting-started).

Note the Supabase CLI requires Docker in order to run

### Copy the project down

```sh
npx degit silentworks/sb-python-issues/supabase_signout_scope supabase_signout_scope
cd supabase_signout_scope
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

Then visit http://127.0.0.1:8000/docs and test the signin and signout endpoints from different browsers.
