# graphite-and-grafana
Get better insights into your back-end performance.

## Metrics Gathering with StatsD
To provide an overview of the StatsD client server service and explain how it works and how metrics are ingested.

### StatsD Overview
What is StatsD? It is a network daemon that aggregates and summarizes application metrics. What makes StatsD so simple and appealing is that applications send metrics to the StatsD daemon via a language specific client library. This library then sends metrics to the StatsD daemon by default over UDP, the User Datagram Protocol. This means developers are free to instrument their own code however and whenever they see fit with little overhead.
