# What is this?

There is a "web application" that runs as `root` :facepalm:

If the user accesses `http://<server>/shell` it will try to run the reverse shell and try to connect to port 7777 on your host using the host's IP address. You just need to figure out how to give the web application the IP address to connect to. The hint for this is that most VMs have a "default route" that is an IP address ending in `.1` that it uses to connect to the network. This IP address is likely the one you can try first.

## Linux
You can run `nc -lvp 7777` to listen for the remote shell connection.

## macOS
You can run `nc -l 0.0.0.0 7777` to listen for the remote shell connection.

## Windows
You can run `ncat -l 0.0.0.0 7777` to listen for the remote shell connection. To do this you will need to install `ncat` using the instructions found [here](https://www.configserverfirewall.com/windows-10/netcat-windows/)
