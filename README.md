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

