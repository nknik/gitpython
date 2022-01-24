/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/
select student_information.roll_number,student_information.name from student_information  JOIN faculty_information ON student_information.advisor=faculty_information.employee_id where faculty_information.salary>20000 and faculty_information.gender='F' OR faculty_information.salary>15000 and faculty_information.gender='M' 