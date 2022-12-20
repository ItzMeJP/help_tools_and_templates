

Its easy to setup a LAN between two Ubuntu machines connected over ethernet. If one of those machines, which we will call the server, is also connected to the internet via another device (like a wireless card) it will automagically share its internet connection as well. Begin by connecting the client and server machines via ethernet.

On the server machine, click the network icon on the top right and select "Edit Connections > Wired connection 1 > Edit > IPv4 Settings" and change "Method" to "Shared to other computers". Then open the network icon menu again and click "Wired connection 1" to ensure that the connection has been established. Running ifconfig in the terminal should show that the wired interface has an ip address.

On the client machine, click the network icon on the top right and select "Wired connection 1". All done. Run ifconfig on this machine as well to see the ip address you've been assigned.
