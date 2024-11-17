CREATE TABLE Employees (
    Name VARCHAR(50),
    Position VARCHAR(50),
    Department VARCHAR(50),
    Salary FLOAT
);


INSERT INTO Employees (Name, Position, Department, Salary)
VALUES
    ("Иван Иванов", "Менеджер", "Продажи", 6000),
    ("Петр Петров", "Инженер", "Разработка", 4500),
    ("Мария Сидорова", "Бухгалтер", "Финансы", 3800),
    ("Алексей Кузнецов", "Специалист", "Маркетинг", 4200);


UPDATE Employees
SET Position = "Руководитель отдела"
WHERE Name = "Иван Иванов";


ALTER TABLE Employees
ADD HireDate DATE;


UPDATE Employees
SET HireDate = "2020-01-01"
WHERE Name = "Иван Иванов";

UPDATE Employees
SET HireDate = "2021-03-15"
WHERE Name = "Петр Петров";

UPDATE Employees
SET HireDate = "2019-07-01"
WHERE Name = "Мария Сидорова";

UPDATE Employees
SET HireDate = "2022-05-01"
WHERE Name = "Алексей Кузнецов";


SELECT * FROM Employees
WHERE Position = "Менеджер";


SELECT * FROM Employees
WHERE Salary > 5000;


SELECT * FROM Employees
WHERE Department = "Продажи";


SELECT AVG(Salary) AS AvgSalary FROM Employees;


DROP TABLE Employees;