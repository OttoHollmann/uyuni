-- oracle equivalent source sha1 6b577e5806e2c41e33cdfd9dea237fc65b7f3e03
-- retrieved from ./1241102873/cdc6d42049bf86fbc9f1d3a5c54275eeacbd641d/schema/spacewalk/oracle/triggers/rhnBeehivePathMap.sql
create or replace function rhn_beehive_path_map_mod_trig_fun() returns trigger as
$$
begin
        new.modified := current_timestamp;
        return new;
end;
$$ language plpgsql;

create trigger
rhn_beehive_path_map_mod_trig
before insert or update on rhnBeehivePathMap
for each row
execute procedure rhn_beehive_path_map_mod_trig_fun();
