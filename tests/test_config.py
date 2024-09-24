from pet_protect_backend.config import _AppConfig
from pet_protect_backend.config import get_config


class TestConfig:
    def test_get_config(self) -> None:
        get_config.cache_clear()
        config_instance = get_config()
        assert isinstance(config_instance, _AppConfig)

        new_config = get_config()
        assert config_instance == new_config

    def test_get_sqlite_config(self, sqlite_db_info: None) -> None:
        config_instance = get_config()
        assert config_instance.db_type == 'SQLITE'
        assert config_instance.db_dialect == 'sqlite'
        assert config_instance.db_url == 'sqlite:///test.db'

    def test_get_postres_config(self, postgres_db_info: None) -> None:
        config_instance = get_config()
        assert config_instance.db_type == 'POSTGRES'
        assert config_instance.db_dialect == 'postgresql+psycopg'
        assert config_instance.db_url == 'postgresql+psycopg://postgres:mypwd@localhost/test_db'
