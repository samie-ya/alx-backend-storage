-- This script will create trigger decreases the quantity of an
-- item after adding a new order
CREATE TRIGGER amount AFTER INSERT on orders
	FOR EACH ROW
	UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name
