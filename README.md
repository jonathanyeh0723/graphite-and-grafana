# graphite-and-grafana
Get better insights into your back-end performance. StatsD, Graphite, and Grafana are three popular open-source tools used to aggregate and visualize metrics about systems and applications.

## Metrics Gathering with StatsD
To provide an overview of the StatsD client server service and explain how it works and how metrics are ingested.

### StatsD Overview
What is StatsD? It is a network daemon that aggregates and summarizes application metrics. What makes StatsD so simple and appealing is that applications send metrics to the StatsD daemon via a language specific client library. This library then sends metrics to the StatsD daemon by default over UDP, the User Datagram Protocol. This means developers are free to instrument their own code however and whenever they see fit with little overhead.

### Installing StatsD

Step1: To download package information from all configured sources. It is useful to get info on an updated version of packages or their dependencies.
```$ sudo apt-get -y update```
