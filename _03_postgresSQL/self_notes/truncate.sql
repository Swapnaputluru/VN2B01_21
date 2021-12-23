create table mobile_buyers (
s_no serial primary key,
buyer_name varchar not null,
buyer_address varchar,
mobile_number bigint
);
select * from mobile_buyers
drop table mobile_buyers

insert into mobile_buyers (buyer_name,buyer_address,mobile_number)
values('swapna','Tadpatri',8252875841),
	  ('hanu','Anantapur',5252451418),
	  ('padma','Tirupathi',2527545667),
	  ('Anu','Darmavaram',7654666747),
	  ('Divyansh','Tadpatri',5621565765),
	  ('Devansh','Tadpatri',5745846678);
select * from mobile_buyers

truncate table mobile_buyers 
select * from mobile_buyers 