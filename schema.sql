-- Drop tables if they exist
DROP TABLE IF EXISTS invoice;
DROP TABLE IF EXISTS intervention;
DROP TABLE IF EXISTS market;

CREATE TABLE market (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE intervention (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    provider TEXT NOT NULL,
    is_valid BOOLEAN NOT NULL,
    market_id INTEGER,
    FOREIGN KEY (market_id) REFERENCES market(id)
);

CREATE TABLE invoice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    price REAL NOT NULL,
    intervention_id INTEGER,
    FOREIGN KEY (intervention_id) REFERENCES intervention(id)
);

