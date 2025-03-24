# Supabase Python issue 1075

This project is making use of [UV](https://docs.astral.sh/uv/) and the [Supabase CLI](https://supabase.com/docs/guides/local-development/cli/getting-started).

Note the Supabase CLI requires Docker in order to run

### Copy the project

```sh
npx degit silentworks/sb-python-issues/supabase_py_1075 supabase_py_1075
cd supabase_py_1075
npm install
```

### Instructions

Start the project with `npx`:

```sh
npx supabase start
```

Rename `.env.example` to `.env` (update the values if you are using hosted Supabase instead of the local one)

Now run the project using `uv`:

```sh
uv run uvicorn main:app --workers 4
```

Now use `ab` or [oha] to run your benchmark tests.

```sh
ab -n 5000 -c 100 http://127.0.0.1:8000
```

[oha]: https://github.com/hatoo/oha
