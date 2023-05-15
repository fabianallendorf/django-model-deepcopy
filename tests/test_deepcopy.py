from django_models.models import Author
from django_model_deepcopy.deepcopy import deepcopy


def test_deepcopy_returns_other_instance():
    author = Author()

    copied = deepcopy(author)

    assert author.pk != copied.pk
    assert author.name == copied.name
    assert author is not copied
