create database employee;
use employee;
create table employee_details(
employee_name varchar(30),
employee_id varchar(20),
employee_address varchar(40)
);
select * from employee_details;

insert into employee_details (employee_name,employee_id,employee_address)
values("swapna","525","anantapuramu");
select * from employee_details;
insert into employee_details (employee_name,employee_id,employee_address)
values("hanu","5674","tadpatri");
insert into employee_details (employee_name,employee_id,employee_address)
values("manu","62562","karnool");
select * from employee_details;
ALTER table employee_details add column  blood_group varchar(10);
select * from employee_details;

rename table employee_details to Employee_Data;
SELECT * from Employee_Data;
alter table Employee_Data modify b_d varchar(12);
alter table Employee_Data change blood_group b_d varchar(10);
alter table Employee_Data rename column b_d to blood;

alter table Employee_Data drop column employee_id;
select * from Employee_Data;

create table employee.Employee_Data2(select * from Employee_Data);
SELECT * from Employee_Data2;
truncate table Employee_Data2;
select * from Employee_Data2;
alter table Employee_Data comment = "some employee details";
show table status where name = "Employee_Data";
