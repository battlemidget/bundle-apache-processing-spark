#!/usr/bin/env python3

import os
import unittest

import amulet
import yaml


class TestBundle(unittest.TestCase):
    bundle_file = os.path.join(os.path.dirname(__file__), '..', 'bundle.yaml')

    @classmethod
    def setUpClass(cls):
        cls.d = amulet.Deployment(series='trusty')
        with open(cls.bundle_file) as f:
            bun = f.read()
        bundle = yaml.safe_load(bun)
        cls.d.load(bundle)
        cls.d.setup(timeout=1800)
        cls.d.sentry.wait_for_messages({'spark': 'Ready (standalone HA)'}, timeout=1800)
        cls.spark = cls.d.sentry['spark'][0]

    def test_components(self):
        """
        Confirm that all of the required components are up and running.
        """
        spark, retcode = self.spark.run("pgrep -a java")

        assert 'spark' in spark, 'Spark should be running on spark'

    def test_spark(self):
        output, retcode = self.spark.run("su ubuntu -c 'bash -lc /home/ubuntu/sparkpi.sh 2>&1'")
        assert 'Pi is roughly' in output, 'SparkPI test failed: %s' % output


if __name__ == '__main__':
    unittest.main()
