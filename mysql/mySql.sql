show databases;

use hr;

show tables;

select * from jobs;
select job_id from jobs;
select job_id as "ID JOB" from jobs;

select * from employees;
select upper(first_name) , lower(last_name) from employees;
select salary from employees;
select max(salary) from employees;
select min(salary) from employees;
select avg(salary) from employees;
select count(salary) from employees;

select * from employees;
select first_name from employees order by first_name desc;

select first_name from employees order by first_name ;

