# Apache Spark

This bundle provides a complete deployment of the processing components using
[Apache Spark 1.6.1](https://spark.apache.org/) in standalone HA mode.
These components include:

  * Spark (3 units)
  * Zookeeper (3 units)

In addition to monitoring facilities offered by Spark (the job history server)
this bundle pairs Spark with an ELK stack (Elasticsearch-Logstash-Kibana)
in order to analyse Spark logs.

Deploying this bundle gives you a fully configured and connected Apache Spark
cluster on any supported cloud, which can be easily scaled to meet workload
demands.


## Deploying this bundle

In this deployment, the aforementioned components are deployed on separate
units. To deploy this bundle, simply use:

    juju quickstart apache-processing-spark

See `juju quickstart --help` for deployment options, including machine
constraints and how to deploy a locally modified version of `bundle.yaml`.

The default bundle deploys three Spark nodes. To scale the cluster, use:

    juju add-unit spark -n 2

This will add two additional Spark nodes, for a total of five.


### Verify the deployment

The services provide extended status reporting to indicate when they are ready:

    juju status --format=tabular

This is particularly useful when combined with `watch` to track the on-going
progress of the deployment:

    watch -n 0.5 juju status --format=tabular

The Spark charm provides a `smoke-test` action that can be used to verify that
it functions as expected:

    juju action do spark/0 smoke-test
    watch -n 0.5 juju action status

Eventually, the action should settle to `status: completed`.  If not
then it means that component is not working as expected.
You can get more information about that component's smoke test:

    juju action fetch <action-id>

Using Spark job history server you can inspect the status of the curently running jobs
as well as the ones finished. The Spark and system logs of the Spark nodes are collected
and indexed at the Elasticsearch node. By navigatng to http://<kibana-host> you gain
access to the log analysis facilities of this bundle.

## Contact Information

- <bigdata@lists.ubuntu.com>


## Help

- [Juju mailing list](https://lists.ubuntu.com/mailman/listinfo/juju)
- [Juju community](https://jujucharms.com/community)
