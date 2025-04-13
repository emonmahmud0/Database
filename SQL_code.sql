-- Create database (if it doesn't exist)
CREATE DATABASE IF NOT EXISTS library_management;
USE library_management;

-- Create Categories table
CREATE TABLE IF NOT EXISTS Categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

-- Create Students table
CREATE TABLE IF NOT EXISTS Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    enrollment_year INT
) ENGINE=InnoDB;

-- Create book_list table
CREATE TABLE IF NOT EXISTS book_list (
    book_id VARCHAR(10) PRIMARY KEY NOT NULL,
    book_name VARCHAR(50) NOT NULL,
    author VARCHAR(50) NOT NULL,
    edition VARCHAR(10) NOT NULL,
    price INT(6) NOT NULL,
    qty INT(4) NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
) ENGINE=InnoDB;

-- Create borrow_record table
CREATE TABLE IF NOT EXISTS borrow_record (
    borrow_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id VARCHAR(10) NOT NULL,
    student_id INT NOT NULL,
    issue_date DATE NOT NULL,
    return_date DATE NOT NULL,
    FOREIGN KEY (book_id) REFERENCES book_list(book_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
) ENGINE=InnoDB;

-- Create Fines table
CREATE TABLE IF NOT EXISTS Fines (
    fine_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    book_id VARCHAR(10),
    fine_amount DECIMAL(10, 2) NOT NULL,
    fine_date DATE NOT NULL,
    payment_status VARCHAR(20) DEFAULT 'Unpaid',
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (book_id) REFERENCES book_list(book_id)
) ENGINE=InnoDB;


-- Sample Data Insertion (Optional)
INSERT INTO Categories (category_name) VALUES
('Fiction'),
('Science'),
('History');

INSERT INTO Students (student_name, department, enrollment_year) VALUES
('Alice Smith', 'Computer Science', 2022),
('Bob Johnson', 'Electrical Engineering', 2021),
('Charlie Williams', 'Mathematics', 2023);

INSERT INTO book_list (book_id, book_name, author, edition, price, qty, category_id) VALUES
('B101', 'The Lord of the Rings', 'J.R.R. Tolkien', 'Extended Edition', 30, 5, 1),
('S202', 'A Brief History of Time', 'Stephen Hawking', '10th Anniversary', 25, 3, 2),
('H303', 'Sapiens', 'Yuval Noah Harari', 'First Edition', 28, 2, 3);

INSERT INTO borrow_record (book_id, student_id, issue_date, return_date) VALUES
('B101', 1, '2024-01-10', '2024-01-24'),
('S202', 2, '2024-01-15', '2024-01-29');

INSERT INTO Fines (student_id, book_id, fine_amount, fine_date, payment_status) VALUES
(1, 'B101', 5.00, '2024-01-25', 'Unpaid'),
(2, 'S202', 2.00, '2024-01-30', 'Paid');

-- Queries Demonstrating Requested Features

-- 1. JOIN Operation: Get book details and borrower names
SELECT
    b.book_name,
    s.student_name
FROM
    book_list b
JOIN
    borrow_record br ON b.book_id = br.book_id
JOIN
    Students s ON br.student_id = s.student_id;

-- 2. VIEW Operation: Create a view for overdue books
CREATE OR REPLACE VIEW OverdueBooks AS
SELECT
    b.book_name,
    s.student_name,
    br.return_date
FROM
    book_list b
JOIN
    borrow_record br ON b.book_id = br.book_id
JOIN
    Students s ON br.student_id = s.student_id
WHERE
    br.return_date < CURDATE();

-- Select from the view
SELECT * FROM OverdueBooks;

-- 3. Nested Query: Get books borrowed by students from the 'Computer Science' department
SELECT
    b.book_name
FROM
    book_list b
WHERE
    b.book_id IN (
        SELECT
            br.book_id
        FROM
            borrow_record br
        WHERE
            br.student_id IN (
                SELECT
                    s.student_id
                FROM
                    Students s
                WHERE
                    s.department = 'Computer Science'
                )
            );

-- 4. Query to get students with fines:
SELECT
    s.student_name,
    f.fine_amount,
    f.payment_status
FROM
    Students s
JOIN
    Fines f ON s.student_id = f.student_id;

-- 5. Query to get books in a specific category:
SELECT
    b.book_name,
    c.category_name
FROM
    book_list b
JOIN
    Categories c ON b.category_id = c.category_id
WHERE
    c.category_name = 'Fiction';