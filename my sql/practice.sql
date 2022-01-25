

create table student(
name_student varchar(10),
id varchar(20),
address varchar(50)
)
comment = 'some student details';
select * from student;
drop table student;
insert into student (name_student,id,address)
values("swapna","525","anantapuramu");
select * from student;
show table status where name = "student"
