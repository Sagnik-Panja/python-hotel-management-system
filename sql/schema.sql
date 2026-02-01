CREATE DATABASE IF NOT EXISTS hotel;
USE hotel;

CREATE TABLE custdata (
    Cid INT PRIMARY KEY,
    Custname VARCHAR(30),
    Address VARCHAR(50),
    Phone BIGINT,
    Bill FLOAT,
    Indate DATE,
    Outdate DATE
);

CREATE TABLE rooms (
    Roomtype VARCHAR(10),
    Number INT,
    Cost FLOAT,
    Available INT
);

CREATE TABLE hotelmenu (
    Item VARCHAR(30),
    Cost FLOAT
);
