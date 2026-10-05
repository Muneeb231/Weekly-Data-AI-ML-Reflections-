# Week 3 - Data: Views

**Context**

This week I learned about SQL **views**, which are virtual tables that don't store data themselves, but instead represent the result of a stored query. Every time you query a view, the underlying query runs fresh against the real tables.

**Key Takeaway**

A view is created with `CREATE VIEW` and can then be queried just like a regular table:

```sql
CREATE VIEW book_authors AS
SELECT books.title, authors.name AS author_name
FROM books
JOIN authors ON books.author_id = authors.id;

SELECT * FROM book_authors;
```

Instead of writing that `JOIN` every time I want titles paired with author names, I can just query `book_authors` directly just like I would query a table.

**Why This Matters**

Views are useful for a few reasons:
- **Simplification**: hide a complex join or aggregation behind a simple, reusable name.
- **Security**: expose only specific columns or rows to certain users, without giving them access to the full underlying table (e.g. a view that excludes a salary of an employee).
- **Consistency**: if multiple people/queries need the same derived data, a view keeps that logic in one place instead of duplicated across scripts.
