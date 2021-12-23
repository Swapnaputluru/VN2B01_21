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
create table tablet(
m_no int,
mobile_name varchar,
mobile_price int
);
drop table mobiles
select * from mobiles
insert into tablet(m_no,mobile_name,mobile_price)
values(2,'Iphone',50000),
      (4,'Appo',20000),
      (7,'Vivo',23000),
      (1,'Realme',15000),
      (8,'Redme',17000),
      (10,'1+',25000);
     select * from tablet
   select m.buyer_name,m.buyer_address,m.mobile_number, t.m_no  from mobile_buyers as m, tablet as t
   where m.s_no=t.m_no






  