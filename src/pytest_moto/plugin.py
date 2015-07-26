"""Module contains code for all moto fixtures and their generator."""
import importlib

import pytest

from mirakuru import TCPExecutor

CONNECTION_MAP = {
    'autoscaling': 'boto.ec2.autoscale:AutoScaleConnection',
    'cloudformation': 'boto.cloudformation:CloudFormationConnection',
    'cloudwatch': 'boto.ec2.cloudwatch:CloudWatchConnection',
    'dynamodb': 'boto.dynamodb.layer1:Layer1',
    'dynamodb2': 'boto.dynamodb2.layer1:DynamoDBConnection',
    'ec2': 'boto.ec2:EC2Connection',
    'elb': 'boto.ec2.elb:ELBConnection',
    'emr': 'boto.emr.EmrConnection',
    'glacier': 'boto.glacier.layer1:Layer1',
    'iam': 'boto.iam.connection:IAMConnection',
    'kinesis': 'boto.kinesis.layer1:KinesisConnection',
    'kms': 'boto.kms.layer1:KMSConnection',
    'rds': 'boto.rds:RDSConnection',
    'redshift': 'boto.redshift.layer1:RedshiftConnection',
    'route53': 'boto.route53:Route53Connection',
    's3': 'boto.s3:S3Connection',
    'ses': 'boto.ses:SESConnection',
    'sns': 'boto.sns:SNSConnection',
    'sqs': 'boto.sqs:SQSConnection',
    'sts': 'boto.sts:STSConnection',
}


class UnsupportedService(Exception):

    """Exception is raised if user called unsupported service."""

    pass


def get_connection(service, connection_params):
    """Function returns connection for given service."""
    if service not in CONNECTION_MAP:
        raise UnsupportedService(service)

    module, klass = CONNECTION_MAP[service].split(':')
    return getattr(importlib.import_module(module), klass)(**connection_params)


def moto_fixture(service, host='127.0.0.1', port=7000, timeout=10,
                 connection_params=None):
    """Create moto-based fixture which runs selected mock of AWS service.

    :param str service: service
    :param str host:
    :param int port:
    :param int timeout:
    :param dict connection_params:
    :rtype: Object
    :returns: Connection to selected AWS service
    """
    connection_params = connection_params or {}

    if service not in CONNECTION_MAP:
        raise UnsupportedService(service)

    @pytest.yield_fixture
    def moto_service():
        executor = TCPExecutor(
            ('moto_server', '-H', host, '-p', str(port), service),
            host=host, port=port, timeout=10)
        connection_params.setdefault('proxy', host)
        connection_params.setdefault('proxy_port', port)
        connection_params.setdefault('aws_access_key_id', '')
        connection_params.setdefault('aws_secret_access_key', '')
        connection_params.setdefault('is_secure', False)
        with executor:
            yield get_connection(service, connection_params)
    return moto_service


# Fixtures for every AWS service which can be mocked via moto
moto_autoscaling = moto_fixture('autoscaling')
moto_cloudformation = moto_fixture('cloudformation', port=7001)
moto_cloudwatch = moto_fixture('cloudwatch', port=7002)
moto_dynamodb = moto_fixture('dynamodb', port=7003)
moto_ec2 = moto_fixture('ec2', port=7004)
moto_elb = moto_fixture('elb', port=7005)
moto_emr = moto_fixture('emr', port=7006)
moto_glacier = moto_fixture('glacier', port=7007)
moto_iam = moto_fixture('iam', port=7008)
moto_kinesis = moto_fixture('kinesis', port=7009)
moto_kms = moto_fixture('kms', port=7010)
moto_rds = moto_fixture('rds', port=7011)
moto_redshift = moto_fixture('redshift', port=7012)
moto_route53 = moto_fixture('route53', port=7013)
moto_s3 = moto_fixture('s3', port=7014)
moto_ses = moto_fixture('ses', port=7015)
moto_sns = moto_fixture('sns', port=7016)
moto_sqs = moto_fixture('sqs', port=7017)
moto_sts = moto_fixture('sts', port=7018)
