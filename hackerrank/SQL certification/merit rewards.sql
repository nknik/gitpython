/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/
select employee_ID,name from employee_information natural join last_quarter_bonus where bonus > 4999 and division='HR'