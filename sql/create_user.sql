CREATE DATABASE IF NOT EXISTS hotel;

CREATE USER IF NOT EXISTS 'hotel_user'@'localhost'
IDENTIFIED BY 'hotel_pass';

GRANT ALL PRIVILEGES ON hotel.* TO 'hotel_user'@'localhost';

FLUSH PRIVILEGES;
