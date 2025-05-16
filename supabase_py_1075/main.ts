import { createClient } from '@supabase/supabase-js'
import { config } from 'dotenv'

config()

const url = process.env.SUPABASE_URL!
const key = process.env.SUPABASE_KEY!
const supabase = createClient(url, key)

const server = Bun.serve({
  port: 3000,
  async fetch(request) {
    const { data, error } = await supabase.from("cities")
      .select(`*`).limit(1)
    return Response.json(data);
  },
});

console.log(`Listening on ${server.url}`);
