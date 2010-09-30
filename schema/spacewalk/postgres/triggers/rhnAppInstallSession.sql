-- oracle equivalent source sha1 99fe744c62087aa5302bd64041adf27145a946d1
-- retrieved from ./1239053651/49a123cbe214299834e6ce97b10046d8d9c7642a/schema/spacewalk/oracle/triggers/rhnAppInstallSession.sql
create or replace function rhn_appinst_session_mod_trig_fun() returns trigger as
$$
begin
	new.modified := current_timestamp;
	return new;
end;
$$ language plpgsql;

create trigger
rhn_appinst_session_mod_trig
before insert or update on rhnAppInstallSession
for each row
execute procedure rhn_appinst_session_mod_trig_fun();

