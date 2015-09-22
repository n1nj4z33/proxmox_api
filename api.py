# -*- coding: utf-8 -*-
'''
A python wrapper for the Proxmox 2.x REST API
For more information see https://pve.proxmox.com/
'''
import requests
from requests.utils import urlparse
import logging

def prepare_logger():
    '''Prepare module logger'''
    inner_logger = logging.getLogger(__name__)
    inner_logger.setLevel(logging.DEBUG)
    chanel = logging.StreamHandler()
    chanel.setLevel(logging.DEBUG)
    inner_logger.addHandler(chanel)
    return inner_logger

LOGGER = prepare_logger()

class ProxmoxAPI(object):
    '''Class for communication with proxmox'''
    def __init__(self, url):
        self.base_url = urlparse(url).netloc
        self.url = 'https://%s/api2/json' % self.base_url
        self.session = requests.Session()
        requests.packages.urllib3.disable_warnings()
        self.session.headers.update({'Accept': 'application/json'})

    def prepare_url(self, url):
        '''Prepare url from methods url. Returns url STRING'''
        return '/'.join((self.url, url))

    def send_request(self, url=None, method=None, headers=None, data=None):
        '''Send request and logging the response. Returns RESPONSE'''
        url = self.prepare_url(url)
        LOGGER.info('Request url: %s', url)
        LOGGER.info('Request data: %s', data)
        response = self.session.request(method=method,
                                        url=url,
                                        headers=headers,
                                        data=data,
                                        verify=False)
        LOGGER.info('Response code: %s', response.status_code)
        LOGGER.info('Response text: %s', response.text)
        return response

    def get_tokens(self, username, password, realm):
        '''Get authtorization tokens. Returns TUPLE'''
        url = 'access/ticket'
        data = {'username': username,
                'password': password,
                'realm': realm}
        response = self.send_request(url=url,
                                     method='POST',
                                     data=data)
        ticket = response.json()['data']['ticket']
        token = response.json()['data']['CSRFPreventionToken']
        return ticket, token

    def auth(self, username, password, realm):
        '''Update session cookie. Returns TUPLE'''
        ticket, token = self.get_tokens(username,
                                        password,
                                        realm)
        self.session.cookies.update({'PVEAuthCookie': ticket})
        self.session.headers.update({'CSRFPreventionToken': token})
        return ticket, token

    def get_vmid(self):
        '''Get next VM ID of cluster. Returns ID(INTEGER)'''
        url = 'cluster/nextid'
        return self.send_request(url=url,
                                 method='GET')

    def get_nodes(self):
        '''Get all nodes of server. Returns JSON'''
        url = 'nodes'
        return self.send_request(url=url,
                                 method='GET')

    def get_task_status(self, node, upid):
        '''Get node task status by UPID. Returns JSON'''
        url = 'nodes/%s/tasks/%s/status' % (node, upid)
        return self.send_request(url=url,
                                 method='GET')

    def get_storage_contents(self, node, storage):
        '''Get all contents of node storage. Returns JSON'''
        url = 'nodes/%s/storage/%s/content' % (node, storage)
        return self.send_request(url=url,
                                 method='GET')

    def get_storage_volume_data(self, node, storage, volume):
        '''Get node storage content info. Returns JSON'''
        url = 'nodes/%s/storage/%s/content/%s' % (node, storage, volume)
        return self.send_request(url=url,
                                 method='GET')

    def delete_storage_content(self, node, storage, filename):
        '''Get node storage content info.'''
        url = 'nodes/%s/storage/%s/content/local:iso/%s' % (node, storage, filename)
        return self.send_request(url=url,
                                 method='DELETE')

    def create_vm(self, node, data):
        '''Create new QEMU virtual machine. Returns JSON'''
        url = 'nodes/%s/qemu' % node
        return self.send_request(url=url,
                                 method='POST',
                                 data=data)

    def get_all_vm(self, node):
        '''Get all QEMU virtual machines. Returns JSON'''
        url = 'nodes/%s/qemu' % node
        return self.send_request(url=url,
                                 method='GET')

    def get_vm_config(self, node, vmid):
        '''Get QEMU virtual machine config. Returns JSON'''
        url = 'nodes/%s/qemu/%s/config' % (node, vmid)
        return self.send_request(url=url,
                                 method='GET')

    def edit_vm(self, node, vmid, data):
        '''Edit QEMU virtual machine params. Returns JSON'''
        url = 'nodes/%s/qemu/%s/config' % (node, vmid)
        return self.send_request(url=url,
                                 method='PUT',
                                 data=data)

    def start_vm(self, node, vmid):
        '''Start QEMU virtual machine. Returns JSON'''
        url = 'nodes/%s/qemu/%s/status/start' % (node, vmid)
        return self.send_request(url=url,
                                 method='POST')

    def stop_vm(self, node, vmid):
        '''Stop QEMU virtual machine. Returns JSON'''
        url = 'nodes/%s/qemu/%s/status/stop' % (node, vmid)
        return self.send_request(url=url,
                                 method='POST')

    def delete_vm(self, node, vmid):
        '''Delete QEMU virtual machine. Returns JSON'''
        url = 'nodes/%s/qemu/%s' % (node, vmid)
        return self.send_request(url=url,
                                 method='DELETE')

    def send_key_vm(self, node, vmid, data):
        '''Send key to QEMU virtual machine.'''
        url = 'nodes/%s/qemu/%s/sendkey' % (node, vmid)
        return self.send_request(url=url,
                                 method='PUT',
                                 data=data)
