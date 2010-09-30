-- oracle equivalent source sha1 3cbf3124a75f788088e845ba3052176af48ab844
-- retrieved from ./1241102873/cdc6d42049bf86fbc9f1d3a5c54275eeacbd641d/schema/spacewalk/oracle/triggers/rhnKSInstallType.sql
create or replace function rhn_ksinstalltype_mod_trig_fun() returns trigger as
$$
begin
       new.modified := current_timestamp;
        
        return new;
end;
$$ language plpgsql;

create trigger
rhn_ksinstalltype_mod_trig
before insert or update on rhnKSInstallType
for each row
execute procedure rhn_ksinstalltype_mod_trig_fun();

