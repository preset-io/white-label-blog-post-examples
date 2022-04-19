import yarl
from sqlalchemy.engine.url import URL


def get_sqlalchemy_uri(instance: yarl.URL) -> str:
    """
    Given a Preset workspace, return its SQLAlchemy URI.
    """
    hostnames = {
        "ws1.region.app.preset.io": "db1",
        "ws2.region.app.preset.io": "db2",
    }
    if instance.host not in hostnames:
        raise Exception(f"Invalid workspace: {instance}")

    url = URL(
        "postgresql",
        username="username",
        password="password123",
        host=hostnames[instance.host],
        port=5432,
        database="examples",
    )
    return str(url)
