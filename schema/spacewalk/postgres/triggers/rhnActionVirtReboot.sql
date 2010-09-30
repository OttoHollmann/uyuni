-- oracle equivalent source sha1 7d854b97762ee011e781feb4cf59c17b114af4ea
-- retrieved from ./1239053651/49a123cbe214299834e6ce97b10046d8d9c7642a/schema/spacewalk/oracle/triggers/rhnActionVirtReboot.sql
create or replace function rhn_avreboot_mod_trig_fun() returns trigger as
$$
begin
	new.modified := current_timestamp;
	return new;
end;
$$ language plpgsql;

create trigger
rhn_avreboot_mod_trig
before insert or update on rhnActionVirtReboot
for each row
execute procedure rhn_avreboot_mod_trig_fun();

