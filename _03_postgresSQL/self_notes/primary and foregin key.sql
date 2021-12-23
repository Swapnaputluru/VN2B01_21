create table colleges (
college_number INT GENERATED ALWAYS AS IDENTITY,
college_name varchar not null,
primary key (college_number)
); 
drop table colleges 
select * from colleges

create table student_details(
student_number INT GENERATED ALWAYS AS IDENTITY,
college_number int,
student_name varchar,
branch varchar not null,
year varchar,
primary key (student_number),
constraint fk_college
foreign key (college_number)
references colleges(college_number)
on delete set null
);
select * from student_details 
drop table student_details 
insert into colleges(college_name)
values('k.s.r.m'),
	  ('jntua'),
	  ('jntuk')
insert into student_details (college_number,student_name,branch,year)
values(3,'swapna','civil','2nd year'),
	  (1,'hanu','cse','finalyear'),
	  (1,'padma','EEE','first year');

select * from student_details
select * from colleges

delete from student_details where student_number=5;


