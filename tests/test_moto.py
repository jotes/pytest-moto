"""Unit and integration tests for fixtures in pytest-moto."""
import pytest

from boto.ec2.autoscale import LaunchConfiguration
from pytest_moto.plugin import (UnsupportedService,
                                moto_fixture,
                                moto_autoscaling,)


def test_unsupported_service():
    """We have to check if unsupported services are handled properly."""
    with pytest.raises(UnsupportedService):
        moto_fixture('ultrafancyservice')


def test_moto_autoscaling(moto_autoscaling):
    """Check if moto_autoscaling fixture returns connection which is operable."""
    assert moto_autoscaling.get_all_launch_configurations() == []

@pytest.mark.skipif(True, reason="Cloudformation isn't supported via standalone moto.")
def test_moto_cloudformation(moto_cloudformation):
    """Check if moto_cloudformation fixture returns connection which is operable."""
    assert moto_cloudformation.list_stacks() == []


def test_moto_cloudwatch(moto_cloudwatch):
    """Check if moto_cloudwatch fixture returns connection which is operable."""
    assert moto_cloudwatch.list_metrics() == []


def test_moto_dynamodb(moto_dynamodb):
    """Check if moto_dynamodb fixture returns connection which is operable."""
    assert moto_dynamodb.list_tables()['TableNames'] == []


def test_moto_ec2(moto_ec2):
    """Check if moto_dynamodb fixture returns connection which is operable."""
    assert moto_ec2.get_all_instances() == []


def test_moto_elb(moto_elb):
    """Check if moto_elb fixture returns connection which is operable."""
    assert moto_elb.get_all_load_balancers() == []


def test_moto_emr(moto_emr):
    """Check if moto_emr fixture returns connection which is operable."""
    assert moto_emr.list_clusters().clusters == []


def test_moto_glacier(moto_glacier):
    """Check if moto_glacier fixture returns connection which is operable."""
    assert moto_glacier.list_vaults()['VaultList'] == []