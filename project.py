"""This will configure your project.
"""

# This will add a few methods that you can use.
from medaf.conf.project import ProjectConfigProperty

class Main(ProjectConfigProperty):
    """This class has to be defined, and the name is case-sensitive."""

    def main(self) -> None:
        """This function has to be defined, and the name is case-sensitive."""

        # Configure your installed apps. WARNING: The order of your installed plugins matters!
        # If an app 'example' uses an app called 'example1', load 'example1' first!
        self.installed_apps = ["standard_app"]

        # This will configure your installed plugins, use your plugin's package name.
        # MEDAF plugin is a Python package that contains a MEDAF standard app. WARNING: The
        # order of your installed plugins matters! For example, a plugin called 'example' uses a
        # plugin called 'example1', load 'example1' first!
        self.installed_plugins = ["medaf_http"]

        # Configure your installed middleware, use your middleware's package name. WARNING: The
        # order of your installed middleware matters! For example, middleware called 'example'
        # uses a middleware called 'example1', load 'example1' first!
        self.installed_middleware = ["standard_middleware"]

        # This will set the gateway. A gateway is the one that is going to establish a
        # connection between MEDAF and WSGI Server/Web Server/etc.
        self.gateway = "medaf_http.gateway"

        # Set port.
        self.port = 8080

        # Set host.
        self.host = '0.0.0.0'

        # Set debug mode.
        self.debug = True
