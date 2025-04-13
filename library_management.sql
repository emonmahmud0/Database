-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2025 at 11:59 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `book_list`
--

CREATE TABLE `book_list` (
  `book_id` varchar(10) NOT NULL,
  `book_name` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL,
  `edition` varchar(10) NOT NULL,
  `price` int(6) NOT NULL,
  `qty` int(4) NOT NULL,
  `category_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book_list`
--

INSERT INTO `book_list` (`book_id`, `book_name`, `author`, `edition`, `price`, `qty`, `category_id`) VALUES
('B101', 'The Lord of the Rings', 'J.R.R. Tolkien', 'Extended E', 30, 5, 1),
('B102', 'Harry Poter', 'J k Rowlings', '2nd', 200, 3, 7),
('H303', 'Sapiens', 'Yuval Noah Harari', 'First Edit', 28, 2, 3),
('ISBN001', 'The Lord of the Rings', 'J.R.R. Tolkien', 'Extended', 30, 5, 1),
('ISBN002', 'Foundation', 'Isaac Asimov', 'First', 25, 3, 2),
('ISBN003', 'Gone Girl', 'Gillian Flynn', 'Hardcover', 28, 2, 3),
('ISBN004', 'The Girl on the Train', 'Paula Hawkins', 'Paperback', 15, 4, 4),
('ISBN005', 'Pride and Prejudice', 'Jane Austen', 'Collector\'', 20, 6, 5),
('ISBN006', 'A Brief History of Time', 'Stephen Hawking', 'Anniversar', 22, 2, 6),
('ISBN007', 'Steve Jobs', 'Walter Isaacson', 'First', 35, 3, 7),
('ISBN008', 'Mastering the Art of French Cooking', 'Julia Child', 'Revised', 26, 5, 8),
('ISBN009', 'Into the Wild', 'Jon Krakauer', 'First', 18, 2, 9),
('ISBN010', 'The Raven', 'Edgar Allan Poe', 'Illustrate', 12, 4, 10),
('S202', 'A Brief History of Time', 'Stephen Hawking', '10th Anniv', 25, 3, 2);

-- --------------------------------------------------------

--
-- Table structure for table `borrow_record`
--

CREATE TABLE `borrow_record` (
  `borrow_id` int(11) NOT NULL,
  `book_id` varchar(10) NOT NULL,
  `student_id` int(11) NOT NULL,
  `issue_date` date NOT NULL,
  `return_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `borrow_record`
--

INSERT INTO `borrow_record` (`borrow_id`, `book_id`, `student_id`, `issue_date`, `return_date`) VALUES
(1, 'B101', 1, '2024-01-10', '2024-01-24'),
(2, 'S202', 2, '2024-01-15', '2024-01-29'),
(3, 'ISBN001', 1, '2024-01-15', '2024-01-29'),
(4, 'ISBN002', 2, '2024-01-20', '2024-02-03'),
(5, 'ISBN003', 3, '2024-01-25', '2024-02-08'),
(6, 'ISBN004', 4, '2024-01-30', '2024-02-13'),
(7, 'ISBN005', 5, '2024-02-01', '2024-02-15'),
(8, 'ISBN006', 6, '2024-02-05', '2024-02-19'),
(9, 'ISBN007', 7, '2024-02-10', '2024-02-24'),
(10, 'ISBN008', 8, '2024-02-15', '2024-03-01'),
(11, 'ISBN009', 9, '2024-02-20', '2024-03-06');

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`category_id`, `category_name`) VALUES
(1, 'Fiction'),
(2, 'Science'),
(3, 'History'),
(4, 'Fiction'),
(5, 'Science Fiction'),
(6, 'Mystery'),
(7, 'Thriller'),
(8, 'Romance'),
(9, 'History'),
(10, 'Biography'),
(11, 'Cookbook'),
(12, 'Travel'),
(13, 'Poetry');

-- --------------------------------------------------------

--
-- Table structure for table `fines`
--

CREATE TABLE `fines` (
  `fine_id` int(11) NOT NULL,
  `student_id` int(11) DEFAULT NULL,
  `book_id` varchar(10) DEFAULT NULL,
  `fine_amount` decimal(10,2) NOT NULL,
  `fine_date` date NOT NULL,
  `payment_status` varchar(20) DEFAULT 'Unpaid'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fines`
--

INSERT INTO `fines` (`fine_id`, `student_id`, `book_id`, `fine_amount`, `fine_date`, `payment_status`) VALUES
(1, 1, 'B101', 5.00, '2024-01-25', 'Unpaid'),
(2, 2, 'S202', 2.00, '2024-01-30', 'Paid'),
(3, 1, 'ISBN001', 5.00, '2024-01-29', 'Unpaid'),
(4, 2, 'ISBN002', 2.50, '2024-02-05', 'Paid'),
(5, 3, 'ISBN003', 10.00, '2024-02-10', 'Unpaid'),
(6, 4, 'ISBN004', 1.00, '2024-02-15', 'Paid'),
(7, 5, 'ISBN005', 7.50, '2024-02-20', 'Unpaid'),
(8, 6, 'ISBN006', 3.00, '2024-02-25', 'Paid'),
(9, 7, 'ISBN007', 6.00, '2024-03-01', 'Unpaid'),
(10, 8, 'ISBN008', 4.00, '2024-03-05', 'Paid'),
(11, 9, 'ISBN009', 8.00, '2024-03-10', 'Unpaid'),
(12, 10, 'ISBN010', 2.00, '2024-03-15', 'Paid');

-- --------------------------------------------------------

--
-- Stand-in structure for view `overduebooks`
-- (See below for the actual view)
--
CREATE TABLE `overduebooks` (
`book_name` varchar(50)
,`student_name` varchar(50)
,`return_date` date
);

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `student_id` int(11) NOT NULL,
  `student_name` varchar(50) NOT NULL,
  `department` varchar(50) DEFAULT NULL,
  `enrollment_year` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`student_id`, `student_name`, `department`, `enrollment_year`) VALUES
(1, 'Alice Smith', 'Computer Science', 2022),
(2, 'Bob Johnson', 'Electrical Engineering', 2021),
(3, 'Charlie Williams', 'Mathematics', 2023),
(4, 'Alice Wonderland', 'Computer Science', 2021),
(5, 'Bob The Builder', 'Engineering', 2022),
(6, 'Charlie Chaplin', 'Arts', 2023),
(7, 'David Copperfield', 'Magic', 2020),
(8, 'Emily Dickinson', 'Literature', 2021),
(9, 'Frankenstein', 'Science', 2022),
(10, 'Greta Garbo', 'Drama', 2023),
(11, 'Harry Houdini', 'Escape', 2020),
(12, 'Jane Austen', 'Literature', 2021),
(13, ' жил', 'Physics', 2022);

-- --------------------------------------------------------

--
-- Structure for view `overduebooks`
--
DROP TABLE IF EXISTS `overduebooks`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `overduebooks`  AS SELECT `b`.`book_name` AS `book_name`, `s`.`student_name` AS `student_name`, `br`.`return_date` AS `return_date` FROM ((`book_list` `b` join `borrow_record` `br` on(`b`.`book_id` = `br`.`book_id`)) join `students` `s` on(`br`.`student_id` = `s`.`student_id`)) WHERE `br`.`return_date` < curdate() ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book_list`
--
ALTER TABLE `book_list`
  ADD PRIMARY KEY (`book_id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `borrow_record`
--
ALTER TABLE `borrow_record`
  ADD PRIMARY KEY (`borrow_id`),
  ADD KEY `book_id` (`book_id`),
  ADD KEY `student_id` (`student_id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `fines`
--
ALTER TABLE `fines`
  ADD PRIMARY KEY (`fine_id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `book_id` (`book_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`student_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `borrow_record`
--
ALTER TABLE `borrow_record`
  MODIFY `borrow_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `fines`
--
ALTER TABLE `fines`
  MODIFY `fine_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `book_list`
--
ALTER TABLE `book_list`
  ADD CONSTRAINT `book_list_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`);

--
-- Constraints for table `borrow_record`
--
ALTER TABLE `borrow_record`
  ADD CONSTRAINT `borrow_record_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book_list` (`book_id`),
  ADD CONSTRAINT `borrow_record_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`);

--
-- Constraints for table `fines`
--
ALTER TABLE `fines`
  ADD CONSTRAINT `fines_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`),
  ADD CONSTRAINT `fines_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book_list` (`book_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
