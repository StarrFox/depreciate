CREATE TABLE IF NOT EXISTS "depreciates" (
    "id"	INTEGER NOT NULL,
    "type"	INTEGER NOT NULL DEFAULT 0,
    "author"	INTEGER NOT NULL,
    "when"	TIMESTAMP NOT NULL,
    "reason"	TEXT,
    PRIMARY KEY("id","type")
);