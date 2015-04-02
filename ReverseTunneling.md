# Reverse ssh tunnel from a windows workstation #

As the measurement workstations (IR, CAM, ..) do not necessarily reside in the same network as the workstation running lumikki, it may be necessary to use a ssh tunnel to allow connections between the lumikki server and the measurement workstation.

On the measurement workstation (windows) open command line and run

`sshg3 -l<USER> hugo.hut.fi -R<HPORT>:localhost:<MPORT>`

where `<USER>` is your fyslab username, `<HPORT>` is some port (`<` 1024, e.g. 57924) on hugo and `<MPORT>` is the port which lighthttpd is listening on the measurement machine (80 or 81). This creates a tunnel from hugo's port `<HPORT>` to the measurement workstation's port `<MPORT>` and opens a shell on hugo. Now run

`ssh <host> -R<LPORT>:localhost:<HPORT>`

where `<host>` is the hostname of the linux workstation running lumikki (e.g. vanessa) and `<LPORT>` is the port we wish to use for opening a http connection to the mesurement workstation (>1024, can be the same as `<HPORT>` if not in use). Now opening http//localhost:`<LPORT>` in a web browser should show the measurement workstation's lighthttpd default page.

So with `<USER> = sse`, `<MPORT> = 81`, `<HPORT> = 57924`, `<host> = vanessa` and `<LPORT> = 57925` the commands are

`sshg3 -lsse hugo.hut.fi -R57924:localhost:81`

`ssh vanessa -R57925:localhost:57924`

and on lumikki running on vanessa can connect to the measurement workstation through `localhost:57925` and the connection can be tested by opening http://localhost:57925/ in a web browser.