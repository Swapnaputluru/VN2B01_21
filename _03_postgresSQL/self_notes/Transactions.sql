
create table home_appliances(
number serial ,
name varchar not null);
select * from home_appliances 
drop table home_appliances 
insert into home_appliances (name)
values('heater');
insert into home_appliances (name)
values('fridge');
insert into home_appliances (name)
values('AC');
insert into home_appliances (name)
values('cooler');
insert into home_appliances 
values(21,'washing machine');


select * from home_appliances 
begin;
delete from home_appliances where name='fridge';
rollback;

select * from home_appliances 
begin;
delete from home_appliances where name='fridge';
commit;


