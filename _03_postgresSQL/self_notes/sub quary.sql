create table students(
s_no serial,
name varchar,
roll_number int,
specilization varchar,
year varchar
);
select * from students
drop table students
insert into students values(1,'swapna',12,'btech','firstyear');
insert into students values(3,'hanu',124,'btech','finalyear');
insert into students values(14,'padma',127,'btech','secondyear');
insert into students values(15,'laxmi',145,'btech','firstyear');
insert into students values(10,'divyansh',12,'btech','thirdyear');


select * from students where roll_number in ( select roll_number  from students where roll_number=12); 


delete from students where s_no in( select s_no from students where s_no>14);


