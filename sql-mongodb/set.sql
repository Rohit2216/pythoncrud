**Problem 1:**

- **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
- **Problem**: Create a **`Customers`** table / collection with the following fields: **`id`** (unique identifier), **`name`**, **`email`**, **`address`**, and **`phone_number`**.


CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);


// Create a collection named "users"
db.createCollection("users");

// Insert a document into the "users" collection
db.users.insertOne({
    _id: 1,
    name: "John Doe",
    email: "john@example.com"
});



**Problem 2:**

- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Customers`** table / collection with data of your choice.


INSERT INTO Users (ID, Name, Email)
VALUES (1, 'John Doe', 'john@example.com');



// Insert a single document into the "users" collection
db.users.insertOne({
    _id: 4,
    name: "Alice Brown",
    email: "alice@example.com"
});


**Problem 3:**

- **Prerequisite**: Understand basic data fetching in SQL / MongoDB
- **Problem**: Write a query to fetch all data from the **`Customers`** table / collection.

SELECT Name, Email
FROM Users
WHERE ID > 2;



// Find all documents in the "users" collection
db.users.find();

// Find documents with a specific condition
db.users.find({ _id: 4 });

// Find documents with a condition and project specific fields
db.users.find({ name: "John Doe" }, { name: 1, email: 1 });


**Problem 4:**

- **Prerequisite**: Understand how to select specific fields in SQL / MongoDB
- **Problem**: Write a query to select only the **`name`** and **`email`** fields for all customers.

SELECT ProductName, Price
FROM Products
WHERE Category = 'Electronics';


// Find documents with specific fields in the "products" collection
db.products.find(
  { category: 'Electronics' },
  { ProductName: 1, Price: 1, _id: 0 }
);


**Problem 5:**

- **Prerequisite**: Understand basic WHERE clause in SQL / MongoDB's find method
- **Problem**: Write a query to fetch the customer with the **`id`** of 3.

SELECT *
FROM Products
WHERE Price > 100;


// Find documents from the "products" collection where the price is greater than 100
db.products.find({ Price: { $gt: 100 } });

// Find documents with multiple conditions using the $and operator
db.products.find({
  $and: [
    { Category: 'Electronics' },
    { Price: { $gt: 200 } }
  ]
});


**Problem 6:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
- **Problem**: Write a query to fetch all customers whose **`name`** starts with 'A'.


SELECT *
FROM Customers
WHERE name LIKE 'A%';


db.customers.find({ name: /^A/ });


**Problem 7:**

- **Prerequisite**: Understand how to order data in SQL / MongoDB
- **Problem**: Write a query to fetch all customers, ordered by **`name`** in descending order.

SELECT *
FROM Customers
ORDER BY name DESC;



db.customers.find().sort({ name: -1 });




**Problem 8:**

- **Prerequisite**: Understand data updating in SQL / MongoDB
- **Problem**: Write a query to update the **`address`** of the customer with **`id`** 4.

UPDATE Customers
SET address = 'New Address'
WHERE id = 4;


db.customers.updateOne(
  { _id: 4 },
  { $set: { address: 'New Address' } }
);


**Problem 9:**

- **Prerequisite**: Understand how to limit results in SQL / MongoDB
- **Problem**: Write a query to fetch the top 3 customers when ordered by **`id`** in ascending order.

SELECT *
FROM Customers
ORDER BY id ASC
LIMIT 3;


db.customers.find().sort({ id: 1 }).limit(3);


**Problem 10:**

- **Prerequisite**: Understand data deletion in SQL / MongoDB
- **Problem**: Write a query to delete the customer with **`id`** 2.

DELETE FROM Customers
WHERE id = 2;


db.customers.deleteOne({ _id: 2 });


**Problem 11:**

- **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
- **Problem**: Write a query to count the number of customers.

SELECT COUNT(*) AS customer_count
FROM Customers;


db.customers.count();


**Problem 12:**

- **Prerequisite**: Understand how to skip rows / documents in SQL / MongoDB
- **Problem**: Write a query to fetch all customers except the first two when ordered by **`id`** in ascending order.


SELECT *
FROM Customers
ORDER BY id ASC
OFFSET 2;


db.customers.find().sort({ id: 1 }).skip(2);


**Problem 13:**

- **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all customers whose **`id`** is greater than 2 and **`name`** starts with 'B'.


SELECT *
FROM Customers
WHERE id > 2 AND name LIKE 'B%';


db.customers.find({ $and: [ { id: { $gt: 2 } }, { name: /^B/ } ] });


**Problem 14:**

- **Prerequisite**: Understand how to use OR conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all customers whose **`id`** is less than 3 or **`name`** ends with 's'.


SELECT *
FROM Customers
WHERE id < 3 OR name LIKE '%s';


db.customers.find({ $or: [ { id: { $lt: 3 } }, { name: /s$/ } ] });


**Problem 15:**

- **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
- **Problem**: Write a query to fetch all customers where the **`phone_number`** field is not set or is null.


SELECT *
FROM Customers
WHERE phone_number IS NULL;



db.customers.find({ phone_number: { $exists: false } });
