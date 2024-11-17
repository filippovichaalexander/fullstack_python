# Создание таблицы authors:
CREATE TABLE authors ( id INT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50) );

# Создание таблицы books:
CREATE TABLE books ( id INT PRIMARY KEY, title VARCHAR(100), author_id INT, publication_year INT, FOREIGN KEY (author_id) REFERENCES authors(id) );

# Создание таблицы sales:
CREATE TABLE sales ( id INT PRIMARY KEY, book_id INT, quantity INT, FOREIGN KEY (book_id) REFERENCES books(id) );

# Добавление авторов в таблицу authors:
INSERT INTO authors (id, first_name, last_name) VALUES (1, "Иван", "Иванов"), (2, "Петр", "Петров"), (3, "Анна", "Сидорова");

# Добавление книг в таблицу books:
INSERT INTO books (id, title, author_id, publication_year) VALUES (1, "Книга 1", 1, 2020), (2, "Книга 2", 2, 2021), (3, "Книга 3", 1, 2022), (4, "Книга 4", 3, 2023);

# Добавление записей о продажах в таблицу sales:
INSERT INTO sales (id, book_id, quantity) VALUES (1, 1, 10), (2, 2, 5), (3, 1, 3), (4, 3, 8), (5, 4, 2);



# Получение списка всех книг и их авторов с помощью INNER JOIN:
SELECT b.title, a.first_name, a.last_name FROM books b INNER JOIN authors a ON b.author_id = a.id;

# Получение списка всех авторов и их книг (включая авторов, у которых нет книг) с помощью LEFT JOIN:
SELECT a.first_name, a.last_name, b.title FROM authors a LEFT JOIN books b ON a.id = b.author_id;

# Получение списка всех книг и их авторов, включая книги, у которых автор не указан, с помощью RIGHT JOIN:
SELECT b.title, a.first_name, a.last_name FROM books b RIGHT JOIN authors a ON b.author_id = a.id;



# Получение списка всех книг, их авторов и продаж с помощью INNER JOIN:
SELECT a.first_name, a.last_name, b.title, s.quantity FROM authors a INNER JOIN books b ON a.id = b.author_id INNER JOIN sales s ON b.id = s.book_id;


# Получение списка всех авторов, их книг и продаж (включая авторов без книг и книги без продаж) с помощью LEFT JOIN:
SELECT a.first_name, a.last_name, b.title, s.quantity FROM authors a LEFT JOIN books b ON a.id = b.author_id LEFT JOIN sales s ON b.id = s.book_id;


# Определение общего количества проданных книг каждого автора с помощью INNER JOIN и функций агрегации:
SELECT a.first_name, a.last_name, SUM(s.quantity) AS total_sales FROM authors a INNER JOIN books b ON a.id = b.author_id INNER JOIN sales s ON b.id = s.book_id GROUP BY a.first_name, a.last_name;

# Определение общего количества проданных книг каждого автора, включая авторов без продаж, с помощью LEFT JOIN и функций агрегации:
SELECT a.first_name, a.last_name, COALESCE(SUM(s.quantity), 0) AS total_sales FROM authors a LEFT JOIN books b ON a.id = b.author_id LEFT JOIN sales s ON b.id = s.book_id GROUP BY a.first_name, a.last_name;


# Нахождение автора с наибольшим количеством проданных книг:
SELECT a.first_name, a.last_name, SUM(s.quantity) AS total_sales FROM authors a INNER JOIN books b ON a.id = b.author_id INNER JOIN sales s ON b.id = s.book_id GROUP BY a.first_name, a.last_name ORDER BY total_sales DESC LIMIT 1;

# Нахождение книг, которые были проданы в количестве, превышающем среднее количество продаж всех книг:
SELECT b.title, SUM(s.quantity) AS total_sales FROM books b INNER JOIN sales s ON b.id = s.book_id GROUP BY b.title HAVING SUM(s.quantity) > ( SELECT AVG(total_sales) FROM ( SELECT SUM(s.quantity) AS total_sales FROM sales s GROUP BY s.book_id ) AS subquery );