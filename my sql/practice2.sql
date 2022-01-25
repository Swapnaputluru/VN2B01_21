create table frds(
s_no serial,
frd_1 varchar(20),
frd_2 varchar(30),
frd_3 varchar(20),
frd_4 varchar(30)
);
drop table frds;
select * from frds;
insert into frds(frd_1,frd_2,frd_3,frd_4)
values("manu","anu","sai","tom");
insert into frds(frd_1,frd_2,frd_3,frd_4)
values("tommy","puppy","snoopy","syam");
select * from frds;
select frd_1 from frds;
select * from frds where frd_1 = "manu";
select * from frds where frd_1 like 'm%';
select * from frds order by frd_2 desc;
select * from frds order by frd_3 asc;
select frd_2,frd_3 from frds group by frd_1;
select * from frds having s_no <= 1;
update frds set frd_1 = "mani" where s_no = 1;
update frds set frd_2 = "ani" , frd_3 = "sai prasanna" where s_no = 1;
delete from frds where frd_1 = "mani";
select * from frds;
create table frds1(select * from frds);
select * from frds1;
delete from frds1;
select * from frds1;