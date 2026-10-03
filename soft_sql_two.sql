-- run this in powershell: & "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" --default-character-set=utf8mb4 -u root -p salesoptimizer -e "source C:/projects/project-1.0.0/salesop/soft_sql_two.sql"

TRUNCATE TABLE salesoptimizer.invoiceitems_parent;

INSERT INTO salesoptimizer.invoiceitems_parent
    (InvoiceItemID, PartyID, FullName, SalesOfficeID, Name, InvoiceID, 
     Number, Expr2, PartID, ParentCode, Expr1, MajorUnitQuantity, 
     Mobile, Price, ReductionAmount, AdditionAmount, NetPrice, 
     FirstName, LastName)
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
    SUBSTRING(Code, 1, LENGTH(Code) - 2) AS ParentCode,
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