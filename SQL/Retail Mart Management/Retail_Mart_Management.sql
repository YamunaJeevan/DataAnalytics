/*Retail Mart Management.
DESCRIPTION
A data analyst of a retail shop, Happy Mart, wants to store the product details, the customer details, 
and the order details to provide unparalleled insights about customer behavior and product stock details daily.
Objective:
The design of the database helps to easily evaluate and identify the performance of the shop 
to increase the daily sales.*/

/*Tasks performed:*/

/*Query to create a database named SQL basics.*/
create database SQL_basics;

/*Query to select the database SQL basics.*/
USE SQL_basics;

/*Query to create a 
	product table with fields as product code, product name, price, stock and category, 
    customer table with the fields as customer id, customer name, customer location, and customer phone number and,
    sales table with the fields as date, order number, product code, product name, quantity, and price.*/
    
CREATE TABLE IF NOT EXISTS
	SQL_basics.PRODUCT_TABLE (
		P_CODE INT NOT NULL,
        P_NAME VARCHAR(100) NOT NULL,
        PRICE INT NOT NULL,
        STOCK INT,
        CATEGORY VARCHAR(100)
        ) ENGINE = InnoDB;

DESCRIBE SQL_basics.PRODUCT_TABLE;

CREATE TABLE IF NOT EXISTS
	SQL_basics.CUSTOMER_TABLE (
		C_ID INT NOT NULL,
        C_NAME VARCHAR(50),
        C_LOCATION VARCHAR(50),
        C_PHONENO INT
        ) ENGINE = InnoDB;

DESCRIBE SQL_basics.CUSTOMER_TABLE;

CREATE TABLE IF NOT EXISTS
	SQL_basics.SALES_TABLE (
		ORDER_DATE DATE,
        ORDER_NO INT,
        C_ID INT,
        C_NAME VARCHAR(50),
        S_CODE INT,
        P_NAME VARCHAR(50),
        QTY INT,
        PRICE INT
        ) ENGINE = InnoDB;

DESCRIBE SQL_basics.SALES_TABLE;

/*Query to insert values into the tables.*/
-- PRODUCT TABLE
INSERT INTO SQL_basics.PRODUCT_TABLE (P_CODE,P_NAME,PRICE,STOCK,CATEGORY)
	VALUES('1','tulip',198,5,'perfume');
-- Import product_datasets via Table data Import data    
select * from SQL_basics.product_datasets;

-- CUSTOMER TABLE
INSERT INTO SQL_basics.CUSTOMER_TABLE (C_ID,C_NAME,C_LOCATION,C_PHONENO)
	VALUES('1111','Nisha','kerala',8392320);
-- Import customer_datasets via Table data Import data    
select * from SQL_basics.customer_datasets;

-- SALES TABLE
INSERT INTO SQL_basics.SALES_TABLE (ORDER_DATE,ORDER_NO,C_ID,C_NAME,S_CODE,P_NAME,QTY,PRICE)
	VALUES('2016-07-24','06',9212,'Jessica',11,'pencil',3,30);

-- Import sales_datasets via Table data Import data    
select * from SQL_basics.sales_datasets;

/*Query to add two new columns such as S_no and categories to the sales table.*/

ALTER TABLE SQL_basics.sales_datasets 
	ADD s_no INT;
ALTER TABLE SQL_basics.sales_datasets
    ADD categories varchar(50);
    
DESCRIBE SQL_basics.sales_datasets;

/*Query to change the column type of stock in the product table to varchar.*/

ALTER TABLE SQL_basics.product_datasets
	MODIFY stock VARCHAR(50);
    
DESCRIBE SQL_basics.product_datasets;

/*Query to change the table name from customer-to-customer details.*/

ALTER TABLE SQL_basics.customer_datasets
	RENAME TO SQL_basics.customer_details;
    
SELECT * FROM SQL_basics.customer_details;

/*Query to drop the columns S_no and categories from the sales table.*/
ALTER TABLE SQL_basics.sales_datasets
	DROP COLUMN s_no;
ALTER TABLE SQL_basics.sales_datasets
	DROP COLUMN categories;

DESCRIBE SQL_basics.sales_datasets;

/*Query to display order id, customer id, order date, price, and quantity from the sales table.*/
SELECT order_no,c_id,order_date,price,qty FROM SQL_basics.sales_datasets;

/*Query to display all the details in the product table if the category is stationary.*/
SELECT * FROM SQL_basics.product_datasets
	WHERE category = 'stationary';

/*Query to display a unique category from the product table.*/
SELECT DISTINCT category FROM SQL_basics.product_datasets;

/*Write a query to display the sales details 
if quantity is greater than 2 and 
price is lesser than 500 from the sales table.*/

SELECT * FROM SQL_basics.sales_datasets
WHERE qty > 2 AND price < 500 ;

/*Write a query to display the customer’s name if the name ends with a.*/
DESCRIBE SQL_basics.customer_details;
SELECT * FROM SQL_basics.customer_details
WHERE c_name like "%a" ;

/*Write a query to display the product details in descending order of the price.*/
SELECT * FROM SQL_basics.product_datasets
ORDER BY price DESC;

/*Write a query to display the product code and category 
from similar categories that are greater than or equal to 2.*/
DESCRIBE SQL_basics.product_datasets;
SELECT * FROM SQL_basics.product_datasets
GROUP BY category HAVING p_code >=2;

/*Write a query to display the order number and the customer name 
to combine the results of the order and the customer tables including duplicate rows.*/
SELECT order_no,c_name FROM SQL_basics.sales_datasets;

