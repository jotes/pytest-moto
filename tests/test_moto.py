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

    launch_config = LaunchConfiguration(name='Launch config 1', image_id='ami-xxx')
    moto_autoscaling.create_launch_configuration(launch_config)

    launch_configs = moto_autoscaling.get_all_launch_configurations()
    assert len(launch_configs) == 1
    assert launch_configs[0].name == launch_config.name
    assert launch_configs[0].image_id == launch_config.image_id
