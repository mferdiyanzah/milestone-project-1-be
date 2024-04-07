CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(100)
);

CREATE TABLE publishers (
    publisher_id INT PRIMARY KEY,
    publisher_name VARCHAR(100)
);

CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(255),
    author_id INT,
    publisher_id INT,
    genre VARCHAR(50),
    publication_date DATE,
    price DECIMAL(10, 2),
    FOREIGN KEY (author_id) REFERENCES authors(author_id),
    FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
);

CREATE TABLE sales (
    transaction_id INT PRIMARY KEY,
    book_id INT,
    sale_date DATE,
    quantity INT,
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);