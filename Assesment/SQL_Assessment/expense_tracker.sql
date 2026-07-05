/* =====================================================================
   TOPS Technologies - Assessment File
   Theme: Personal Expense Tracker DB
   Submitted by: Arbaz Nilgar
===================================================================== */

/* =====================================================================
   SECTION A: Concept Application (Theory Answers)
===================================================================== */
/*
1. Explain how relational databases help maintain accuracy in expense records.
Answer: Relational databases use Primary Keys to ensure each record is unique and Foreign Keys to link tables correctly (like linking an expense to a valid user). This prevents duplicate, missing, or inaccurate data.

2. Why are constraints important in personal finance data?
Answer: Constraints like NOT NULL, UNIQUE, or CHECK ensure that invalid data cannot be saved. For example, a CHECK constraint can prevent an expense amount from being negative.

3. How does GROUP BY help analyze spending patterns?
Answer: GROUP BY allows us to aggregate data into categories. For example, grouping expenses by 'category_id' with SUM(amount) shows exactly how much money was spent on Food vs. Rent.

4. Explain a scenario where rollback is required during expense entry.
Answer: If a transaction involves multiple steps (like deducting money from a bank account and adding it to an expense table) and the system crashes after the first step, a ROLLBACK is required to undo the incomplete transaction and prevent money loss.

5. How do views help users track monthly expenses efficiently?
Answer: Views act as virtual tables. We can save a complex query (with JOINs and monthly filters) as a View, allowing users to quickly see their monthly report without writing the long query again.

6. Why use triggers for automatic category or balance updates?
Answer: Triggers automate actions in the database. If a user adds a new expense, a trigger can automatically deduct that amount from their total balance table without needing extra backend code.
*/

/* =====================================================================
   SECTION B: SQL Hands-On
===================================================================== */

-- Step 0: Creating the Given Database Schema (DO NOT MODIFY structure)
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    created_at DATE
);

CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(50)
);

CREATE TABLE expenses (
    expense_id INT PRIMARY KEY,
    user_id INT,
    category_id INT,
    amount DECIMAL(10,2),
    expense_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);


/* 1. DDL Understanding (Theory)
Explain why foreign keys are used: 
Foreign keys enforce referential integrity. The user_id in expenses MUST correspond to a real ID in users so that we don't have expenses belonging to ghost/non-existent users.

Mention one issue if foreign keys were removed (Orphaned Records): 
If we delete a user, but forget to delete their expenses, those expenses become "Orphaned Records" because they point to a user that no longer exists, causing errors in reports.
*/


-- 2. DML Operations
-- Insert 5 users
INSERT INTO users (user_id, name, email, created_at) VALUES
(1, 'Arbaz Nilgar', 'arbaz@example.com', '2026-07-01'),
(2, 'Sadik Mansuri', 'sadik@example.com', '2026-07-02'),
(3, 'Rehan Khan', 'rehan@example.com', '2026-07-03'),
(4, 'Rahul Patel', 'rahul@example.com', '2026-07-04'),
(5, 'Amit Shah', 'amit@example.com', '2026-07-05');

-- Insert 3 categories
INSERT INTO categories (category_id, category_name) VALUES
(1, 'Food'),
(2, 'Rent'),
(3, 'Entertainment');

-- Insert 10 expense records 
-- (Note: User 1 is given 6 records intentionally to satisfy the View requirement later)
INSERT INTO expenses (expense_id, user_id, category_id, amount, expense_date) VALUES
(101, 1, 1, 250.00, '2026-07-05'),
(102, 1, 2, 5000.00, '2026-07-05'),
(103, 1, 3, 300.00, '2026-07-06'),
(104, 1, 1, 150.00, '2026-07-07'),
(105, 1, 1, 400.00, '2026-07-08'),
(106, 1, 3, 200.00, '2026-07-09'),
(107, 2, 2, 4500.00, '2026-07-05'),
(108, 2, 1, 600.00, '2026-07-06'),
(109, 3, 3, 1000.00, '2026-07-07'),
(110, 4, 1, 50.00, '2026-07-08');

-- Update one incorrect expense
UPDATE expenses 
SET amount = 350.00 
WHERE expense_id = 103;

-- Delete one expense (Remove record where amount is less than 100)
DELETE FROM expenses 
WHERE amount < 100.00;


-- 3. Data Retrieval
-- Display all expenses with details (INNER JOIN)
SELECT e.expense_date, e.amount, u.name, c.category_name
FROM expenses e
INNER JOIN users u ON e.user_id = u.user_id
INNER JOIN categories c ON e.category_id = c.category_id;

-- Show total expense amount per category (GROUP BY)
SELECT c.category_name, SUM(e.amount) AS Total_Expense
FROM expenses e
INNER JOIN categories c ON e.category_id = c.category_id
GROUP BY c.category_name;

-- Display users sorted by total spending (Highest to lowest)
SELECT u.name, SUM(e.amount) AS Total_Spent
FROM users u
INNER JOIN expenses e ON u.user_id = e.user_id
GROUP BY u.name
ORDER BY Total_Spent DESC;


-- 4. Views
-- Create a view named ActiveUsersView (> 5 expenses)
CREATE VIEW ActiveUsersView AS
SELECT u.name, u.email
FROM users u
INNER JOIN expenses e ON u.user_id = e.user_id
GROUP BY u.user_id, u.name, u.email
HAVING COUNT(e.expense_id) > 5;

-- Query the view
SELECT * FROM ActiveUsersView;


/* =====================================================================
   SECTION C: Mini Project
===================================================================== */

-- 1. Write CRUD queries
-- CREATE (Insert)
INSERT INTO categories (category_id, category_name) VALUES (4, 'Travel');
-- READ (Select)
SELECT * FROM categories;
-- UPDATE
UPDATE categories SET category_name = 'Transport' WHERE category_id = 4;
-- DELETE
DELETE FROM categories WHERE category_id = 4;


-- 2. Write a stored procedure to calculate monthly user expense
DELIMITER //
CREATE PROCEDURE CalculateMonthlyExpense(IN p_user_id INT, IN p_month INT, IN p_year INT)
BEGIN
    SELECT u.name, SUM(e.amount) AS Monthly_Total
    FROM expenses e
    INNER JOIN users u ON e.user_id = u.user_id
    WHERE e.user_id = p_user_id 
      AND MONTH(e.expense_date) = p_month 
      AND YEAR(e.expense_date) = p_year
    GROUP BY u.name;
END //
DELIMITER ;
-- To test the procedure: CALL CalculateMonthlyExpense(1, 7, 2026);


-- 3. Demonstrate COMMIT and ROLLBACK with example queries
-- COMMIT Example (Transaction successfully saved)
START TRANSACTION;
INSERT INTO expenses (expense_id, user_id, category_id, amount, expense_date) 
VALUES (111, 2, 3, 500.00, '2026-07-10');
COMMIT;

-- ROLLBACK Example (Transaction fails/canceled, data will not be saved)
START TRANSACTION;
INSERT INTO expenses (expense_id, user_id, category_id, amount, expense_date) 
VALUES (112, 3, 1, 9999.00, '2026-07-11');
-- Oh wait, amount is too high, cancel it!
ROLLBACK;