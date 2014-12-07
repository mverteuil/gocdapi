"""
Module for gocdapi Go class
"""

from gocdapi.admin import Admin
from gocdapi.agents import Agents
from gocdapi.pipeline_groups import PipelineGroups


class Go(object):
    """
    Class that represents Go Server environment.
    """
    def __init__(self, baseurl, username=None, password=None):
        """Inits Go objects.

        Args:
            baseurl (str): The base url of Go Server
            username (str): The username to login in the Go Server
            password (str): The username's password
        """
        self.baseurl = baseurl
        self.username = username
        self.password = password

    @property
    def agents(self):
        """Return agents of the Go Server
        """
        return Agents(self)

    @property
    def pipeline_groups(self):
        """Return Pipeline Groups of the Go Server
        """
        return PipelineGroups(self)

    @property
    def pipelines(self):
        """Return Pipeline Groups of the Go Server
        """
        return dict(self._iter_through_pipelines())

    @property
    def admin(self):
        """Return an Admin object
        """
        return Admin(self)

    def pipeline_exist(self, name):
        """ Check if pipeline exists.

        Args:
            name (str): name of the pipeline to find

        Returns:
            bool: True if pipeline with the given name exists
        """
        for pipeline_group in self.pipeline_groups.values():
            if any(name == pipe_name for pipe_name in pipeline_group):
                return True
        return False

    def _iter_through_pipelines(self):
        """ Return a iterable containing every pipeline

        Generator: Yields a pipeline
        """
        for pipeline_group in self.pipeline_groups.values():
            for pipeline in pipeline_group:
                yield pipeline
