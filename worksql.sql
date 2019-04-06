CREATE TABLE `ship` (
    `shipping_id` VARCHAR(40) NOT NULL,
    `item_id` VARCHAR(40) NOT NULL,
    `quantity` INTEGER(40) NOT NULL,
    `weight_KG` INTEGER(40) NOT NULL,
    `shipper_name` VARCHAR(40) NOT NULL,
    `shipper_email` VARCHAR(40) NOT NULL,
    `receiver_name` VARCHAR(40) NOT NULL,
    `receiver_address` VARCHAR(40) NOT NULL,
    `receiver_contact` VARCHAR(40) NOT NULL,
    `Import_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`shipping_id`)
);



select sum(quantity) from ship where item_id = "item1";


INSERT INTO stock(quantity) VALUES 1 where item_id = `item1`;

select sum(quantity) from ship where item_id = "item1";
drop tables ship;
select * from ship;






CREATE TABLE `additem` (
	`additem_id` int(40) NOT NULL,
    `item_id` VARCHAR(40) NOT NULL,
    `quantity` INTEGER(40) NOT NULL,
    `add_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE `additem`
  ADD PRIMARY KEY (`additem_id`);

ALTER TABLE `additem`
  MODIFY `additem_id` int(40) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
  
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

drop tables additem;

select * from additem;

INSERT INTO additem(item_id, quantity) VALUES("item1", 70);
INSERT INTO additem(item_id, quantity) VALUES("item2", 1);
INSERT INTO additem(item_id, quantity) VALUES("item3", 1);
INSERT INTO additem(item_id, quantity) VALUES("item4", 1);








select additem-ship as stock from (select sum(quantity) as additem from additem where item_id = "item1") as additem, (select sum(quantity) as ship from ship where item_id = "item1") as ship;

INSERT INTO additem(item_id, quantity) VALUES("item1", 123);

select sum(quantity) as additem from additem where item_id = "item1";
select sum(quantity) as ship from ship where item_id = "item1";

select sum(a.quantity),sum(b.quantity) as stock from additem a, ship b where a.item_id = b.item_id and a.item_id = "item1";


select sum(a.quantity-b.quantity) as stock from additem a, ship b where a.item_id = b.item_id and a.item_id = "item2";
select sum(a.quantity-b.quantity) as stock from additem a, ship b where a.item_id = b.item_id and a.item_id = "item3";
select sum(a.quantity-b.quantity) as stock from additem a, ship b where a.item_id = b.item_id and a.item_id = "item4";

insert into ship(shipping_id, item_id, quantity, weight_KG, shipper_name, shipper_email, receiver_name, receiver_address, receiver_contact) VALUES('ship1','item1',88,88,'EDMOND','SB@www','YIN','Tsim Sha Tsui SCOPE CP3LT1','999'),('ship2','item2',87,87,'Cheeper','0NX@www','COW','Tsim Sha Tsui SCOPE L1-2301','911'),('ship3','item1',54,54,'EDMOND','SB@www','YIN','Tsim Sha Tsui SCOPE CP3LT1','999')
