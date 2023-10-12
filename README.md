# NRC Download

Simple Python script to download the latest ePub paper daily.

Uses environment variables for logging in and download location:

* NRC_USERNAME - username
* NRC_PASSWORD - password
* NRC_FOLDER   - folder to save epub

## Systemd

Example systemd unit's can be found in the [systemd](./systemd) folder and uses
an env for secrets `/etc/conf.d/nrc-download`:
```
NRC_FOLDER=/home/syncthing/paper
NRC_LOGIN=foo
NRC_PASSWORD=secret
```
