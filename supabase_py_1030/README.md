# supabase-py issue 1030

This project is making use of [UV](https://docs.astral.sh/uv/) and the [Supabase CLI](https://supabase.com/docs/guides/local-development/cli/getting-started).

Note the Supabase CLI requires Docker in order to run

### Copy the project down

```sh
npx degit silentworks/sb-python-issues/supabase_py_1030 supabase_py_1030
cd supabase_py_1030
npm install
```

### Instructions

Start the project with `npx`:

```sh
npx supabase start
```

Now run the project using `uv`:

```sh
uv run app.py
```