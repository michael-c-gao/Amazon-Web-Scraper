CREATE DATABASE Amazon;

CREATE TABLE Amazon.AmazonProducts (
Product VARCHAR(300) NOT NULL,
Link VARCHAR(300) NOT NULL,
Stars DECIMAL(2,1),
Reviews INT,
PrimeAvailable VARCHAR(1),
Price DECIMAL(7,2),
Shipping VARCHAR(45),
TotalCost DECIMAL(7,2)
);
