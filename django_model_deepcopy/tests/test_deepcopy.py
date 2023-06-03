import datetime
import uuid
from decimal import Decimal

import pytest
from django.core.files.base import ContentFile

from django_model_deepcopy.deepcopy import deepcopy
from django_model_deepcopy.register import register
from django_model_deepcopy.tests.models import SimpleModel


@pytest.mark.django_db
def test_deepcopy_simple_model(faker):
    """
    Test that a simple model can be copied.
    """
    register.register(SimpleModel)
    instance = SimpleModel.objects.create(
        integer=1,
        big_integer=1,
        boolean=True,
        char="a",
        binary=b"a",
        date=datetime.date(2020, 1, 1),
        date_time=datetime.datetime(2020, 1, 1),
        decimal=Decimal("1.3"),
        duration=datetime.timedelta(days=1),
        email="test@example.org",
        file=ContentFile("test"),
        file_path="/tmp/test",
        float=1.5,
        generic_ip="127.0.0.1",
        image=ContentFile(faker.image()),
        positive_integer=1,
        positive_small_integer=1,
        slug="test",
        small_integer=1,
        text="a",
        time=datetime.time(12, 0, 0),
        url="www.example.org",
        json={"a": "b"},
        uuid=uuid.uuid4(),
    )

    copied_instance = deepcopy(instance)

    assert copied_instance.pk != instance.pk
    assert copied_instance.integer == instance.integer
    assert copied_instance.big_integer == instance.big_integer
    assert copied_instance.boolean == instance.boolean
    assert copied_instance.char == instance.char
    assert copied_instance.binary == instance.binary
    assert copied_instance.date == instance.date
    assert copied_instance.date_time == instance.date_time
    assert copied_instance.decimal == instance.decimal
    assert copied_instance.duration == instance.duration
    assert copied_instance.email == instance.email
    assert copied_instance.file == instance.file
    assert copied_instance.file_path == instance.file_path
    assert copied_instance.float == instance.float
    assert copied_instance.generic_ip == instance.generic_ip
    assert copied_instance.positive_integer == instance.positive_integer
    assert copied_instance.positive_small_integer == instance.positive_small_integer
    assert copied_instance.slug == instance.slug
    assert copied_instance.small_integer == instance.small_integer
    assert copied_instance.text == instance.text
    assert copied_instance.time == instance.time
    assert copied_instance.url == instance.url
    assert copied_instance.json == instance.json
    assert copied_instance.uuid == instance.uuid
