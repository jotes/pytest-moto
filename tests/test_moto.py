"""Unit and integration tests for fixtures in pytest-moto."""
import pytest

from pytest_moto.plugin import (UnsupportedService,
                                moto_fixture)


def test_unsupported_service():
    """We have to check if unsupported services are handled properly."""
    with pytest.raises(UnsupportedService):
        moto_fixture('ultrafancyservice')


def test_moto_autoscaling(moto_autoscaling):
    """Check if moto_autoscaling fixture returns working connection."""
    assert moto_autoscaling.get_all_launch_configurations() == []


@pytest.mark.skipif(True, reason="Cloudformation isn't supported via"
                                 "standalone moto.")
def test_moto_cloudformation(moto_cloudformation):
    """Check if moto_cloudformation fixture returns working connection."""
    assert moto_cloudformation.list_stacks() == []


def test_moto_cloudwatch(moto_cloudwatch):
    """Check if moto_cloudwatch fixture returns working connection."""
    assert moto_cloudwatch.list_metrics() == []


def test_moto_dynamodb(moto_dynamodb):
    """Check if moto_dynamodb fixture returns working connection."""
    assert moto_dynamodb.list_tables()['TableNames'] == []


def test_moto_ec2(moto_ec2):
    """Check if moto_dynamodb fixture returns working connection."""
    assert moto_ec2.get_all_instances() == []


def test_moto_elb(moto_elb):
    """Check if moto_elb fixture returns working connection."""
    assert moto_elb.get_all_load_balancers() == []


def test_moto_emr(moto_emr):
    """Check if moto_emr fixture returns working connection."""
    assert moto_emr.list_clusters().clusters == []


def test_moto_glacier(moto_glacier):
    """Check if moto_glacier fixture returns working connection."""
    assert moto_glacier.list_vaults()['VaultList'] == []


@pytest.mark.skipif(True, reason="IAM isn't supported via standalone moto.")
def test_moto_iam(moto_iam):
    """Check if moto_iam fixture returns working connection."""
    assert moto_iam.get_all_users() == []


def test_moto_kinesis(moto_kinesis):
    """Check if moto_kinesis fixture returns working connection."""
    assert moto_kinesis.list_streams()['StreamNames'] == []


def test_moto_kms(moto_kms):
    """Check if moto_kms fixture returns working connection."""
    assert moto_kms.list_keys()['Keys'] == []


def test_moto_rds(moto_rds):
    """Check if moto_rds fixture returns working connection."""
    assert moto_rds.get_all_dbinstances() == []


def test_moto_redshift(moto_redshift):
    """Check if moto_rds fixture returns working connection."""
    assert moto_redshift.describe_clusters()["DescribeClustersResponse"]["DescribeClustersResult"]["Clusters"] == []


@pytest.mark.skipif(True, reason="Can't create connection to Route53 because boto don't support plain http protocol.")
def test_moto_route53(moto_route53):
    """Check if moto_rds fixture returns working connection."""
    assert moto_route53.get_all_hosted_zones() == []


def test_moto_s3(moto_s3):
    """Check if moto_s3 fixture returns working connection."""
    assert moto_s3.get_all_buckets() == []


def test_moto_ses(moto_ses):
    """Check if moto_ses fixture returns working connection."""
    assert moto_ses.get_send_quota()["GetSendQuotaResponse"]["GetSendQuotaResult"]["SentLast24Hours"] == "0"


@pytest.mark.skipif(True, reason="SNS isn't supported via standalone moto.")
def test_moto_sns(moto_sns):
    """Check if moto_ses fixture returns working connection."""
    assert moto_sns.get_all_topics() == []


def test_moto_sqs(moto_sqs):
    """Check if moto_sqs fixture returns working connection."""
    assert moto_sqs.get_all_queues() == []


def test_moto_sts(moto_sts):
    """Check if moto_sts fixture returns working connection."""
    assert moto_sts.get_session_token().access_key == "AKIAIOSFODNN7EXAMPLE"
