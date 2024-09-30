from .utils import is_canonical_version


class TestPackagingAttribute:
    def test_version_respect_pep440(self) -> None:
        from pet_protect_backend import __version__

        assert isinstance(__version__, str)
        assert is_canonical_version(__version__)

    def test_package_description(self) -> None:
        from pet_protect_backend import __doc__ as doc

        assert isinstance(doc, str)
        assert len(doc) > 0
