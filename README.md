# graphite-and-grafana
Get better insights into your back-end performance. StatsD, Graphite, and Grafana are three popular open-source tools used to aggregate and visualize metrics about systems and applications. We'll be able to use them in combination to stay on top of outages, diagnose issues related to database and server performance, and optimize your user experience.

Specifically, we'll have the ability to:
 - gather app-specific metrics with StatsD
 - store those metrics efficiently with Graphite
 - Monitor and beautifully visualize this information with Grafana

## Metrics Gathering with StatsD
To provide an overview of the StatsD client server service and explain how it works and how metrics are ingested.

### StatsD Overview
What is StatsD? It is a network daemon that aggregates and summarizes application metrics. What makes StatsD so simple and appealing is that applications send metrics to the StatsD daemon via a language specific client library. This library then sends metrics to the StatsD daemon by default over UDP, the User Datagram Protocol. This means developers are free to instrument their own code however and whenever they see fit with little overhead.

### Installing StatsD

Step1: To download package information from all configured sources. It is useful to get info on an updated version of packages or their dependencies.

```
$ sudo apt-get -y update
```

Step2: After that, we'll install the dependencies that we require. These are Git, Node JS, devscripts, debhelper, NPM, and dh-systemd.

```
$ sudo apt-get -y install git nodejs devscripts debhelper npm dh-systemd
```

Step3: Once all that has been installed, we'll further clone the StatsD repository and get ready to build a package.

```
$ cd tmp/
$ git clone https://github.com/etsy/statsd.git
```

We should be able to see the below message, if successful:
```
Cloning into 'statsd'...
remote: Enumerating objects: 3550, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 3550 (delta 0), reused 0 (delta 0), pack-reused 3541
Receiving objects: 100% (3550/3550), 816.23 KiB | 7.16 MiB/s, done.
Resolving deltas: 100% (1988/1988), done.
```

Step4: Now that's cloned, we can change directories into the directory we just cloned. And we're ready to build a deb.

```
$ cd statsd/
$ sudo dpkg-buildpackage
```

Once it's successful, we should be able to see the following output:
```
...
LINE: statsd (0.8.5-1) unstable; urgency=low
dpkg-genchanges: warning:     debian/changelog(l19): found end of file where expected more change data or trailer
dpkg-genchanges: info: including full source code in upload
 dpkg-source --after-build .
dpkg-source: warning: statsd/debian/changelog(l9): badly formatted trailer line
LINE:  -- Elliot Blackburn <elliot@elliotblackburn.com>   Thu, 27 Aug 2020 15:30:29 +0000
dpkg-source: warning: statsd/debian/changelog(l11): found start of entry where expected more change data or trailer
LINE: statsd (0.8.6-1) unstable; urgency=low
dpkg-source: warning: statsd/debian/changelog(l11): found end of file where expected more change data or trailer
dpkg-buildpackage: info: full upload; Debian-native package (full source is included)
```

Step5: OK. Now we'll change the directory up just one to the directory that the deb was built in. Find the target file we want and build it.

```
$ cd ..
$ ls
```

```
statsd_0.9.0-1_all.deb          statsd_0.9.0-1_amd64.changes  statsd_0.9.0-1.tar.gz
statsd  statsd_0.9.0-1_amd64.buildinfo  statsd_0.9.0-1.dsc
```

Type this command to build:

```
$ sudo dpkg -i statsd_0.9.0-1_all.deb
```

We should be able to see the following, if successful:

```
gyp ERR! node -v v10.19.0
gyp ERR! node-gyp -v v6.1.0
gyp ERR! not ok 
npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: modern-syslog@1.2.0 (node_modules/modern-syslog):
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: modern-syslog@1.2.0 install: `node-gyp rebuild`
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: Exit status 1

added 8 packages from 13 contributors and audited 252 packages in 7.873s
found 5 vulnerabilities (3 moderate, 2 high)
  run `npm audit fix` to fix them, or `npm audit` for details
dpkg-statoverride: warning: --update given but /var/run/statsd does not exist
Available systemd services are disabled by default:
 * statsd
 * statsd-proxy

To enable one of them use:
  systemctl enable NAME
```

Okay, and even though there was an error, StatsD actually has been installed. 

We can verify by running `sudo systemctl status statsd.service`
```
● statsd.service - Network daemon for aggregating statistics
     Loaded: loaded (/lib/systemd/system/statsd.service; disabled; vendor preset: enabled)
     Active: inactive (dead)
       Docs: https://github.com/etsy/statsd/
```

### Configuring StatsD

Now that our service is installed, we can configure it to run in debug mode and then send it some test metrics. Start by opening the configure file at `/etc/statsd/local/localConfig.js` and change it to run debug mode.

So first we'll type `sudo -s` to run shell as the target user. And then we will continue to open the config file.

```
$ vim /etc/statsd/localConfig.js
```

We should be able to see the following listed:
```
{
  graphitePort: 2003
, graphiteHost: "localhost"
, port: 8125
}
```

Now we'll comment out the `graphitePort` and `graphiteHost`, since we don't have graphite configured yet. After that, add a new line with `debug:"True"` key-value pair.

```
{
  //graphitePort: 2003
//, graphiteHost: "localhost"
  debug: "True"
, port: 8125
}
```

Okay. Now we can start the service, and check out the status.

```
$ systemctl start statsd.service
$ systemctl status statsd.service
```

We should be able to see the service is running shown from the console.

```
 statsd.service - Network daemon for aggregating statistics
     Loaded: loaded (/lib/systemd/system/statsd.service; disabled; vendor preset: enabled)
     Active: active (running) since Tue 2022-02-22 15:05:58 CST; 3s ago
       Docs: https://github.com/etsy/statsd/
   Main PID: 5360 (statsd /etc/sta)
      Tasks: 11 (limit: 4632)
     Memory: 10.3M
     CGroup: /system.slice/statsd.service
             └─5360 statsd /etc/statsd/localConfig.js

 二  22 15:05:58 openvino-VirtualBox systemd[1]: Started Network daemon for aggregating statistics.
 二  22 15:05:58 openvino-VirtualBox nodejs[5360]: 22 Feb 15:05:58 - [5360] reading config file: /etc/statsd/localConfig.js
 二  22 15:05:58 openvino-VirtualBox nodejs[5360]: 22 Feb 15:05:58 - DEBUG: Loading server: ./servers/udp
 二  22 15:05:58 openvino-VirtualBox nodejs[5360]: 22 Feb 15:05:58 - server is up INFO
 二  22 15:05:58 openvino-VirtualBox nodejs[5360]: 22 Feb 15:05:58 - DEBUG: Loading backend: ./backends/graphite
```

Once we start the service backup, we can send test metrics to it. So to send a test metric, we can input 

```
$ echo "foo:1|c" | nc -u -w0 127.0.0.1 8125
```

### Types of Metrics

As we knew, the StatsD server implements a protocol where data is understood in the form of the following:

```
<bucket>:<value>|<metric_type>
```

Take a look to an example below.

```
email_sending.emails.sent:300|c
```

In this case, **email_sending** is a `bucket`, **300** is a `value`, and **c** is a counter `metric type`.

StatsD supports several types of metrics, including:
 - Counters
 - Timers
 - Gauges
 - Sets
