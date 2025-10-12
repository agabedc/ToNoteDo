CREATE TABLE notes (
  id serial primary key,
  title text,
  body text,
  created timestamp default now(),
  edited timestamp default now()
);

INSERT INTO notes (title, body) VALUES ('Learn web.py', 'learn now!');