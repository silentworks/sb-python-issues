create or replace function send_heartbeat()
returns text
language sql
as $$
  select
  realtime.send(
    jsonb_build_object('hello', 'world'), -- JSONB Payload
    'heartbeat', -- Event name
    'test-channel', -- Topic
    false -- Public / Private flag
  );
$$;

-- Cron Job name cannot be edited
select cron.schedule('send-heartbeat', '*/1 * * * *', 'SELECT send_heartbeat()');
