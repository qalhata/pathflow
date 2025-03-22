create table potholes (
  id uuid primary key default gen_random_uuid(),
  x integer not null,
  y integer not null,
  volume float not null,
  severity text,
  image_url text,
  created_at timestamp default now()
);

create table ugvs (
  id uuid primary key default gen_random_uuid(),
  x integer not null,
  y integer not null,
  status text default 'idle',
  last_updated timestamp default now()
);
