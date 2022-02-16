# graphite-and-grafana
Get better insights into your back-end performance. StatsD, Graphite, and Grafana are three popular open-source tools used to aggregate and visualize metrics about systems and applications.

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
