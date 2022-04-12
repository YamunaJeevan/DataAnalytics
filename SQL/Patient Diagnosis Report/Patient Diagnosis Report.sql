/*Patient Diagnosis Report.
DESCRIPTION
The data analyst of a hospital wants to store the patient diagnosis reports with the details of the doctors 
and the patients for good medical practice and continuity of care.*/

 /*Objective:

The database design helps to retrieve, update, and modify the patient’s details 
to keep track of the patient's health care routine.*/

/*Tasks performed:*/

/*Query to create a patients table with the fields such as 
date, patient id, patient name, age, weight, gender, location, phone number, disease, doctor name, and doctor id.*/

/*Query to select the database SQL basics.*/
USE SQL_basics;

CREATE TABLE IF NOT EXISTS
	SQL_basics.PATIENTS_TABLE (
		DATE_INFO DATE,
        P_ID VARCHAR(10) NOT NULL,
        P_NAME VARCHAR(50) NOT NULL,
        AGE INT NOT NULL,
        WEIGHT INT,
        GENDER VARCHAR(10),
        LOCATION VARCHAR(25),
        PHONENO INT,
        DISEASE VARCHAR(50),
        DOCTOR_NAME VARCHAR(50),
        DOCTOR_ID INT
        ) ENGINE = InnoDB;

DESCRIBE SQL_basics.PATIENTS_TABLE;

/* Query to insert values into the patients table.*/
INSERT INTO SQL_basics.PATIENTS_TABLE (DATE_INFO,P_ID,P_NAME,AGE,WEIGHT,GENDER,LOCATION,PHONENO,DISEASE,
DOCTOR_NAME,DOCTOR_ID)VALUES('2022-04-04','ECPA01','YAMUNA',34,55,'FEMALE','MANCHESTER',86032,'NODISEASE',
'GAYATHRI',11);

SELECT * FROM SQL_basics.PATIENTS_TABLE;

-- Import patients_datasets via Table data Import data    
select * from SQL_basics.patients_datasets;
DESCRIBE SQL_basics.patients_datasets;

/*Query to display the total number of patients in the table.*/
SELECT count( * ) as  TOTAL_PATIENTS FROM SQL_basics.patients_datasets;

/*Query to display the patient id, patient name, gender, and disease of the patient whose age is maximum.*/
-- select pid,p_name,gender,disease, MAX(AGE) from SQL_basics.patients_datasets GROUP BY AGE;

SELECT pid,p_name,gender,disease,age as "Age", count(*) AS  "No of Patient's"
FROM SQL_basics.patients_datasets GROUP BY age HAVING count(*) =
(SELECT max(MaxAge) AS Highest_age
   FROM
(SELECT age , count(*) AS MaxAge
      FROM SQL_basics.patients_datasets GROUP BY age) AS Agetable) ORDER BY age DESC;

/*Query to display patient id and patient name with the current date.*/

SELECT pid,p_name,date,curdate() from SQL_basics.patients_datasets;

/*Query to display the old patient’s name and new patient's name in uppercase.*/
SELECT * FROM SQL_basics.patients_datasets;
SELECT UPPER(p_name) FROM SQL_basics.patients_datasets;

/*Query to display the patient’s name along with the length of their name.*/
SELECT p_name, LENGTH(p_name) FROM SQL_basics.patients_datasets;

/*Query to display the patient’s name, and the gender of the patient must be mentioned as M or F.*/
UPDATE SQL_basics.patients_datasets 
SET gender = 'M' WHERE gender = 'Male';
UPDATE SQL_basics.patients_datasets 
SET gender = 'F' WHERE gender = 'Female';

SELECT p_name, gender from SQL_basics.patients_datasets;

/*Query to combine the names of the patient and the doctor in a new column. */

ALTER TABLE SQL_basics.patients_datasets 
	ADD PATIENT_DOCTOR_NAME VARCHAR(100)
    GENERATED ALWAYS AS (CONCAT(p_name,' ',doctor_name));

SELECT * FROM SQL_basics.patients_datasets;

/*Query to display the patients’ age along with the logarithmic value (base 10) of their age.*/

SELECT pid, p_name, age, LOG10(age) AS LOG10_AGE FROM SQL_basics.patients_datasets;

/*Query to extract the year from the given date in a separate column.*/
SELECT EXTRACT(YEAR FROM CURRENT_DATE);
SELECT YEAR(CURRENT_TIMESTAMP);

-- ALTER TABLE SQL_basics.patients_datasets DROP COLUMN YEAR_FROM;

DESCRIBE SQL_basics.patients_datasets;

-- Alter table name date into date_info
ALTER TABLE SQL_basics.patients_datasets
	CHANGE COLUMN date date_info TEXT;

ALTER TABLE SQL_basics.patients_datasets
	MODIFY date_info DATE;

ALTER TABLE SQL_basics.patients_datasets 
	ADD YEAR_FROM DATE
    GENERATED ALWAYS AS (EXTRACT(YEAR FROM date_info));
    
SELECT * FROM SQL_basics.patients_datasets;

SELECT date_info,
       YEAR(date_info)
         AS  year_from
FROM SQL_basics.patients_datasets;
-- Year from returns Null

/*Query to return NULL if the patient’s name and doctor’s name are similar else return the patient’s name.*/
SELECT NULLIF(p_name,doctor_name) AS SIMILARNAME FROM SQL_basics.patients_datasets;

/*Query to return Yes if the patient’s age is greater than 40 else return No.*/
SELECT IF(age > 40, 'YES','NO') AS AGE40 FROM SQL_basics.patients_datasets;

/* Query to display the doctor’s duplicate name from the table.*/
SELECT doctor_name, doctor_id, COUNT(*)
FROM SQL_basics.patients_datasets
GROUP BY doctor_id
HAVING COUNT(*) > 1