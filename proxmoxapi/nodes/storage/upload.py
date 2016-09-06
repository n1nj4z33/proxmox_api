# -*- coding: utf-8 -*-
"""Module for upload resource."""

from proxmoxapi.resource import Resource
from requests_toolbelt.multipart.encoder import MultipartEncoder


class Upload(Resource):
    """Class for storage resource."""

    def __init__(self, api, node_id, storage_id):
        """
        :param obj api: :class:`ProxmoxAPI <proxmoxapi.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        :param str storage_id: The storage identifier.
        """
        super(Upload, self).__init__(api)
        self.node_id = node_id
        self.storage_id = storage_id
        self.url = "nodes/{node_id}/storage/{storage_id}/upload".format(
            node_id=self.node_id,
            storage_id=self.storage_id)

    def upload(self, content_type, filename, filepath):
        """
        Upload templates and iso images.

        :param str content_type: Content type.
        :param str filename: The name of the file to create.
        :param str filepath: Path of file for upload.

        :returns: :class:`UPID <proxmoxapi.nodes.tasks.upid.UPID>`.
        """

        with open(filepath, "rb") as uploadfile:
            data = MultipartEncoder(
                fields={
                    "content": content_type,
                    "filename": (filename, uploadfile, "application/octet-stream")
                }
            )
            headers = {"Content-Type": data.content_type}
            response = self.send_request("POST", data=data, headers=headers)

        task_id = response.json()["data"]
        return self.api.nodes.node(self.node_id).tasks.get_task_by_task_id(task_id)
