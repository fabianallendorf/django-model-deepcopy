import pytest

from django_model_deepcopy.deepcopy import deepcopy
from django_model_deepcopy.register import register
from django_model_deepcopy.tests.models import SimpleModel


@pytest.mark.django_db
def test_deepcopy_simple_model():
    """
    Test that a simple model can be copied.
    """
    register.register(SimpleModel)
    instance = SimpleModel.objects.create(text="a")

    copied_instance = deepcopy(instance)

    assert copied_instance.pk != instance.pk
    assert copied_instance.text == instance.text
