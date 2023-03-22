# What is this?

There is a "web application" that runs as `root` :facepalm:

If the user accesses `http://<server>/shell` it will run the reverse shell and try to connect to port 7777 on the VM IP address.

You can run `nc -lvp 7777` to listen for the remote shell connection.

# TODO
- `systemd` service file
- `Makefile` for installation

