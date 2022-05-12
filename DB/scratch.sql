CREATE DATABASE testDB;
CREATE TABLE Persons (
    CustomerID int,
    FirstName varchar(255),
    LastName varchar(255),
    ContactName varchar(255),
    Address varchar(255),
    City varchar(255),
    PostalCode int,
    Country varchar(255)
);
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');
