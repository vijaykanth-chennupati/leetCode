select name as Customers
from customers
left join orders on customers.id = orders.customerid
where customerid is null