create table home_appliances(
number serial primary key,
name varchar not null);
select * from home_appliances 

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

delete from home_appliances where name='cooler';
select * from home_appliances 

insert into home_appliances (name)
values('cooler');

alter table home_appliances add column buyingdate varchar;
update home_appliances set buyingdate ='12 october' where name='heater';
update home_appliances set buyingdate ='2 december' where name='fridge';
update home_appliances set buyingdate ='14 may' where name='AC';
update home_appliances set buyingdate ='8 july' where number=21;
update home_appliances set buyingdate ='17 june' where name='cooler';

 select * from home_appliances 
 