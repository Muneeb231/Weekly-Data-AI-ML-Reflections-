
# Week 1 - Data: My Process for Designing a Database

**Context**

This week I worked through a problem set from Harvard's CS50 Databases course involving an airport system. This task included modeling various components like passengers, flights, airlines, and concourses. Rather than just posting the final schema, I wanted to document the process I used to get there, since that's the part that's actually reusable on future projects.

**The Process**

1. List your entities: Passengers, Flights, Airlines, Concourses.
   For every pair of entities, ask: "is there a real-world relationship here?"
   - Passenger ↔ Flight — yes, obviously.
   - Passenger ↔ Airline — not directly; only indirectly through their flight.
   - Flight ↔ Airline — yes, one airline operates a flight.

2. For each real relationship, figure out the cardinality. Is it one-to-one, one-to-many, or many-to-many?
   - Passenger ↔ Flight is many-to-many: one passenger can take many flights over time, and one flight has many passengers.
   - Flight ↔ Airline is one-to-many: one airline operates many flights, but each flight belongs to only one airline.

3. Let the cardinality decide the structure of the schema.
   - Many-to-many → needs a junction table.
   - One-to-many → the foreign key goes on the "many" side.

**Why This Matters**

Steps 1–3 are really about thinking in relationships before thinking in tables. It's tempting to jump straight to "what tables do I need," but starting from entities and using our judgement to ask whether a relationship exists avoids a lot of schema rework later.
