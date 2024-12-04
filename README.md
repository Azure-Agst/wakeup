# WakeUp! (A Docker WoL Solution)

A simple webapp to dispatch Wake-on-LAN packets on a given network.

## Config

Located at `/app/config/config.json`:

```json
{
    "broadcastAddr": "10.0.0.255",
    "port": 9,
    "servers": [
        {
            "name": "Test Server",
            "mac": "12:34:56:78:90:AB"
        }
    ]
}
```

## Docker Notes

Because Docker images operate within their own network interface, we have to patch the Linux Kernel to allow for broadcast packets to be bridged across the main interface and docker's. This is done via the following 3 settings:

```txt
net.ipv4.icmp_echo_ignore_broadcasts=0
net.ipv4.conf.all.bc_forwarding=1
net.ipv4.conf.${interface}.bc_forwarding=1
```

Be sure to replace `${interface}` with the interface identifier for your docker network. In my case, that was `docker0`. Double check via `ip addr` first.

You can apply these by either in the terminal by using `sudo sysctl -w`, or by making a config file in `/etc/sysctl.d/` which contains them.