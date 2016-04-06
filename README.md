# Apache Hadoop with Spark

This bundle provides a complete deployment of the core components of the
[Apache Hadoop 2.7.1](http://hadoop.apache.org/docs/r2.7.1/)
platform to along with [Apache Spark 1.6.1](https://spark.apache.org/).
These components include:

  * NameNode (HDFS)
  * ResourceManager (Yarn)
  * Slaves (DataNode and NodeManager)
  * Spark
    - Plugin (colocated with Spark)

Deploying this bundle gives you a fully configured and connected Apache Hadoop
cluster on any supported cloud, which can be easily scaled to meet workload
demands.


## Deploying this bundle

In this deployment, the aforementioned components are deployed on separate
units. To deploy this bundle, simply use:

    juju quickstart apache-processing-spark

See `juju quickstart --help` for deployment options, including machine
constraints and how to deploy a locally modified version of `bundle.yaml`.

The default bundle deploys three slave nodes and one node of each of
the other services. To scale the cluster, use:

    juju add-unit slave -n 2

This will add two additional slave nodes, for a total of five.


### Verify the deployment

The services provide extended status reporting to indicate when they are ready:

    juju status --format=tabular

This is particularly useful when combined with `watch` to track the on-going
progress of the deployment:

    watch -n 0.5 juju status --format=tabular

The charms for each master component (namenode, resourcemanager, spark)
also each provide a `smoke-test` action that can be used to verify that each
component is functioning as expected.  You can run them all and then watch the
action status list:

    juju action do namenode/0 smoke-test
    juju action do resourcemanager/0 smoke-test
    juju action do spark/0 smoke-test
    watch -n 0.5 juju action status

Eventually, all of the actions should settle to `status: completed`.  If
any go instead to `status: failed` then it means that component is not working
as expected.  You can get more information about that component's smoke test:

    juju action fetch <action-id>


## Contact Information

- <bigdata@lists.ubuntu.com>


## Help

- [Juju mailing list](https://lists.ubuntu.com/mailman/listinfo/juju)
- [Juju community](https://jujucharms.com/community)
