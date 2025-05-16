import { createClient, FunctionsHttpError, FunctionsRelayError, FunctionsFetchError } from '@supabase/supabase-js'

import { config } from 'dotenv'

config()

const url = process.env.SUPABASE_URL
const key = process.env.SUPABASE_KEY
const supabase = createClient(url, key)

const { data, error } = await supabase.functions.invoke('hello', {
  body: { foo: 'bar' },
})

if (error instanceof FunctionsHttpError) {
  const errorMessage = await error.context.json()
  console.log('Function returned an error', error.context.status)
} else if (error instanceof FunctionsRelayError) {
  console.log('Relay error:', error.message)
} else if (error instanceof FunctionsFetchError) {
  console.log('Fetch error:', error.message)
}
