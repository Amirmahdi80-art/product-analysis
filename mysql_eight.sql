-- Create the new table
CREATE TABLE salesoptimizer.invoiceitems_parent AS
SELECT 
    InvoiceItemID,
    PartyID,
    FullName,
    SalesOfficeID,
    Name,
    InvoiceID,
    Number,
    Expr2,
    PartID,
    SUBSTRING(Code, 1, LENGTH(Code) - 2) AS ParentCode,  -- Modified column
    Expr1,
    MajorUnitQuantity,
    Mobile,
    Price,
    ReductionAmount,
    AdditionAmount,
    NetPrice,
    FirstName,
    LastName
FROM salesoptimizer.invoiceitems
WHERE Code IS NOT NULL 
    AND LENGTH(Code) > 2;

-- Add indexes
ALTER TABLE salesoptimizer.invoiceitems_parent
ADD PRIMARY KEY (InvoiceItemID),
ADD INDEX idx_parentcode (ParentCode),
ADD INDEX idx_expr2 (Expr2),
ADD INDEX idx_salesoffice (SalesOfficeID),
ADD INDEX idx_majorquantity (MajorUnitQuantity);

ALTER TABLE salesoptimizer.invoiceitems_parent 
MODIFY COLUMN ParentCode VARCHAR(128) COLLATE utf8mb4_unicode_ci;