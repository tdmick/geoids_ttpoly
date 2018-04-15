from tethys_sdk.base import TethysAppBase, url_map_maker


class GeoidsTtpoly(TethysAppBase):
    """
    Tethys app class for lygons in Utah.
    """

    name = 'Travel Time Polygons'
    index = 'geoids_ttpoly:home'
    icon = 'geoids_ttpoly/images/appicon.png'
    package = 'geoids_ttpoly'
    root_url = 'geoids-ttpoly'
    color = '#1DBD0A'
    description = 'This app allows a user to calculate the distance they could travel from a given point in a given time.'
    tags = 'CEEN514W18, Traveltime'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='geoids-ttpoly',
                controller='geoids_ttpoly.controllers.home'
            ),
        )

        return url_maps
