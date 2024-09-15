{ pkgs, ... }:
{
  project.name = "pet-protect";
  services = {

    postgres = {
      service.image = "postgres:16";
      service.volumes = [ "${toString ./.}/postgres-data:/var/lib/postgresql/data" ];
      service.environment = {
        POSTGRES_DB = "$DB_NAME";
        POSTGRES_PASSWORD = "$DB_PWD";
        POSTGRES_USER = "$DB_USER";
      };
      service.ports = [ "5432:5432" ];
    };
  };
}
