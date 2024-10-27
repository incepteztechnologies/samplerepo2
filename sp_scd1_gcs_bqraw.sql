CREATE SCHEMA IF NOT EXISTS `unified-financial-data-lake.inceptez_bank_raw` options(location='us');

CREATE OR REPLACE EXTERNAL TABLE `unified-financial-data-lake.inceptez_bank_raw.customer_staging` 
OPTIONS (
  FORMAT='JSON',
  uris=['gs://inceptez-banking-project/new_bank_dataset/customer.json']
);

CREATE OR REPLACE PROCEDURE `unified-financial-data-lake.inceptez_bank_raw.sp_scd1_customer_update`()
BEGIN


CREATE TABLE IF NOT EXISTS `unified-financial-data-lake.inceptez_bank_raw.customer_raw`(
  CustomerID int64,
  FirstName string,
  LastName string,
  DateOfBirth date,
  Email string,
  PhoneNumber string,
  Address string,
  BranchID int64,
  last_update timestamp
);

MERGE `unified-financial-data-lake.inceptez_bank_raw.customer_raw` T
USING `unified-financial-data-lake.inceptez_bank_raw.customer_staging` S
ON T.CustomerID = S.CustomerID
WHEN MATCHED THEN
UPDATE SET
  T.FirstName = S.FirstName,
  T.LastName = S.LastName,
  T.DateOfBirth = CAST(S.DateOfBirth AS DATE),
  T.Email = S.Email,
  T.PhoneNumber = S.PhoneNumber,
  T.Address = S.Address,
  T.BranchID = S.BranchID,
  T.last_update = CURRENT_TIMESTAMP()
WHEN NOT MATCHED THEN
INSERT (CustomerID, FirstName, LastName, DateOfBirth, Email, PhoneNumber, Address, BranchID, last_update)
VALUES (S.CustomerID, S.FirstName, S.LastName, CAST(S.DateOfBirth AS DATE), S.Email, S.PhoneNumber, S.Address, S.BranchID, CURRENT_TIMESTAMP());


END;



call `unified-financial-data-lake.inceptez_bank_raw.sp_scd1_customer_update`();


