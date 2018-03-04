pytest-moto
===========

.. image:: https://img.shields.io/pypi/v/pytest-moto.svg
    :target: https://pypi.python.org/pypi/pytest-moto/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/pytest-moto.svg
    :target: https://pypi.python.org/pypi/pytest-moto/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/pypi/wheel/pytest-moto.svg
    :target: https://pypi.python.org/pypi/pytest-moto/
    :alt: Wheel Status

.. image:: https://pypip.in/egg/pytest-moto/badge.png
    :target: https://pypi.python.org/pypi/pytest-moto/
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/l/pytest-moto.svg
    :target: https://pypi.python.org/pypi/pytest-moto/
    :alt: License

Package status
--------------

.. image:: https://travis-ci.org/jotes/pytest-moto.svg?branch=v0.2.0
    :target: https://travis-ci.org/jotes/pytest-moto
    :alt: Tests

.. image:: https://coveralls.io/repos/jotes/pytest-moto/badge.png?branch=v0.2.0
    :target: https://coveralls.io/r/jotes/pytest-moto?branch=v0.2.0
    :alt: Coverage Status

.. image:: https://requires.io/github/jotes/pytest-moto/requirements.svg?tag=v0.2.0
     :target: https://requires.io/github/jotes/pytest-moto/requirements/?tag=v0.2.0
     :alt: Requirements Status


Usage
-----
Pytest-moto is collection of fixtures which are running standalone moto server which can be later
used by larger integration tests.
All available fixtures:

* moto_autoscaling - runs moto server with `autoscaling` api endpoint on port 7002 
* moto_cloudwatch - runs moto server with `cloudwatch` api endpoint on port 7002
* moto_dynamodb - runs moto server with `dynamodb` api endpoint on port 7003
* moto_ec2 - runs moto server with `ec2` api endpoint on port 7004
* moto_elb - runs moto server with `elb` api endpoint on port 7005
* moto_emr - runs moto server with `emr` api endpoint on port 7006
* moto_glacier - runs moto server with `glacier` api endpoint on port 7007
* moto_kinesis - runs moto server with `kinesis` api endpoint on port 7009
* moto_kms - runs moto server with `kms` api endpoint on port 7010
* moto_rds - runs moto server with `rds` api endpoint on port 7011
* moto_redshift - runs moto server with `redshift` api endpoint on port 7012
* moto_s3 - runs moto server with `s3` api endpoint on port 7014
* moto_ses - runs moto server with `ses` api endpoint on port 7015
* moto_sqs - runs moto server with `sqs` api endpoint on port 7017
* moto_sts - runs moto server with `sts` api endpoint on port 7018


TODO
----
* Cloudformation isn't supported in standalone mode of moto (requires patch to upstream repository).
* IAM isn't supported in standalone mode of moto.
* SNS isn't supported in standalone mode of moto.
* Route53 can't use insecure connections requires changes in boto.



Package resources
-----------------

* Bug tracker: https://github.com/jotes/pytest-moto/issues
* Documentation: http://pytest-moto.readthedocs.org/



Travis-ci
---------

After creating package on github, move to tracis-ci.org, and turn on ci builds for given package.
