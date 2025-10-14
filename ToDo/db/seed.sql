INSERT INTO todos (title, details, status, due_date) VALUES
('Set up project', 'Create venv and install deps', 'open', NOW() + INTERVAL '1 day'),
('Write API', 'Implement /api/todos endpoints', 'open', NOW() + INTERVAL '2 days'),
('Test endpoints', 'Use curl or Thunder Client', 'open', NULL);