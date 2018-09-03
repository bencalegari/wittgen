DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS sentence;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE book (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  author_id INTEGER,
  FOREIGN KEY (author_id) REFERENCES user(id)
);

CREATE TABLE sentence (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  body TEXT,
  book_id INTEGER NOT NULL,
  parent_id INTEGER,
  FOREIGN KEY (book_id) REFERENCES book(id),
  FOREIGN KEY (parent_id) REFERENCES sentence(id)
);

INSERT INTO user (name)
VALUES ("Wittgenstein");

INSERT INTO book (title, author_id)
VALUES ("Tractatus Logico-Philosophicus", 1);

INSERT INTO sentence (body, book_id)
VALUES ("The world is everything that is the case.", 1);

INSERT INTO sentence (body, book_id, parent_id)
VALUES ("The world is the totality of facts, not of things.", 1, 1);
