from database import db_op

db_host = "localhost"
db_name= "dabbu-postgres"
db_username = "dabbu"
db_password = "dinero"

SQL = """
CREATE TABLE Customers (
    ID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(100),
    City VARCHAR(50),
    State VARCHAR(50),
    Zip VARCHAR(10)
);

CREATE TABLE Accounts (
    ID SERIAL PRIMARY KEY,
    Type VARCHAR(50) NOT NULL,
    Balance NUMERIC(15,2) NOT NULL,
    OpenDate DATE NOT NULL,
    Status VARCHAR(50) NOT NULL,
    CustomerID INTEGER NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(ID)
);

CREATE TABLE Transactions (
    ID SERIAL PRIMARY KEY,
    Type VARCHAR(50) NOT NULL,
    Amount NUMERIC(15,2) NOT NULL,
    Date DATE NOT NULL,
    AccountID INTEGER NOT NULL,
    FOREIGN KEY (AccountID) REFERENCES Accounts(ID)
);
"""



_DBI_OBJ = db_op.DabbuDBI(db_host, db_name, db_username, db_password)

def run():
    _DBI_OBJ.execute(SQL)
    _DBI_OBJ.commit()
