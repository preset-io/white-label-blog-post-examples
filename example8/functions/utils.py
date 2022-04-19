from yarl import URL


def get_dash_title(instance: URL) -> str:
    """
    Return the chart title given a workspace.
    """
    return "This is the title"


def get_team_id(instance: URL) -> int:
    """
    Return the team name given a workspace URL.
    """
    return 42


def get_chart_title(instance: URL, viz_type: str) -> str:
    """
    Return the chart title given a workspace and a visualization type.
    """
    return "This is the title"


def get_image(instance: URL) -> str:
    """
    Return the link to an image.
    """
    return "https://images.contentful.com/ykljvmtfxwdz/1deKWcvFKpEfPbDA68xoVN/4158f27ee34f01f0fa61fe7e696e1529/superset-logo-horiz_2x.png"
