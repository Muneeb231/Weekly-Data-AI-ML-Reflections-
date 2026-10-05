
# Week 2 - Data: DML and Referential Integrity

**Context**

This week I learned about DML (Data Manipulation Language) keywords: `UPDATE`, `INSERT INTO`, and `DELETE FROM`. Unlike DDL (Data Definition Language), which changes the *structure* of a database (tables, columns, schemas), DML changes the *contents*. of the table

**Key Takeaway**

I learned how to maintain **referential integrity** when deleting data. One useful keyword for this is `ON DELETE CASCADE`: when a row is deleted, any rows in other tables that reference it via a foreign key are automatically deleted too. This prevents "orphaned" rows, whcih are foreign keys pointing to records that no longer exist.

**Example**

```sql
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
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
);

INSERT INTO authors (id, name) VALUES (1, 'Jane Austen');
INSERT INTO books (id, title, author_id) VALUES (1, 'Pride and Prejudice', 1);
INSERT INTO books (id, title, author_id) VALUES (2, 'Emma', 1);

-- Deleting the author automatically deletes their books too
DELETE FROM authors WHERE id = 1;
```

**Why This Matters**

`ON DELETE CASCADE` is set when you *define* the foreign key, not at delete time. Without it, that `DELETE FROM authors` statement would either fail (if the DB enforces foreign key constraints) or leave orphaned rows in `books` pointing to an author that no longer exists.
