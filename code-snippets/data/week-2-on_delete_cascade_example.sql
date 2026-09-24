-- Parent table
CREATE TABLE authors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Child table, with a foreign key that cascades on delete
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE -- On delete cascade is always used when references foreign key
);

-- Insert an author and a couple of their books
INSERT INTO authors (id, name) VALUES (1, 'Jane Austen');
INSERT INTO books (id, title, author_id) VALUES (1, 'Pride and Prejudice', 1);
INSERT INTO books (id, title, author_id) VALUES (2, 'Emma', 1);

-- Deleting the author automatically deletes their books too
DELETE FROM authors WHERE id = 1;

