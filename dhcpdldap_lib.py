#!/usr/bin/env python

LDAP_URI = 'ldap://localhost:10389/'
LDAP_BASE = 'dc=dhcpawn,dc=net'
LDAP_ADMIN = 'cn=Manager,dc=dhcpawn,dc=net'
LDAP_PASSWD = 'dhcpawn'

from ldapdict.ldapcache import LdapCacheWrite
from ldapdict.ldapdict import GenericLdapDictWrite
from logbook import Logger

log = Logger('dhcpawn')

lc = LdapCacheWrite(GenericLdapDictWrite, LDAP_URI, LDAP_ADMIN, LDAP_PASSWD )

# DHCP Server LDAP Object creation and modification

class dhcpServer(object):
    def __init__(self, dhcp_server_name):
        self.name = dhcp_server_name
        self.server_class_list = ['top','dhcpServer']
        self.service_class_list = ['top', 'dhcpService', 'dhcpOptions']
        try:
            self.server = lc.bdn + "cn={}".format(self.name)
            self.config = lc.bdn + "cn=config,cn={}".format(self.name)
            log.info('Initialising existing DHCP Server {}'.format(self.name))
        except:
            log.info('Adding new DHCP Server {}'.format(self.name))
            self.server = lc.bdn.addchild("cn={}".format(self.name), self.server_class_list, {'cn': self.name, 'dhcpServiceDN': "cn=config,cn={},{}".format(self.name, LDAP_BASE),'objectClass': self.server_class_list})
            self.config = self.server.addchild('cn=config', self.service_class_list, {'cn': 'config', 'dhcpPrimaryDN': self.server.dn, 'objectClass': self.service_class_list})

    def update(self):
        pass

    def delete(self):
        pass


class dhcpSubnet(object):
    def __init__(self, subnet, netmask, dhcp_server):
        self.name = subnet
        dhcpNetMask = netmask
        subnet_class_list = ['top', 'dhcpSubnet', 'dhcpOptions']
        try:
            self.subnet = dhcp_server.config + "cn={}".format(self.name)
            log.info('Initialising existing Subnet {}'.format(self.name))
        except:
            log.info('Adding new Subnet {}'.format(self.name))
            self.subnet = dhcp_server.config.addchild("cn={}".format(self.name), subnet_class_list, {'cn': self.name, 'dhcpNetMask': dhcpNetMask,'objectClass': subnet_class_list})

    def update(self):
        pass

    def delete(self):
        log.info('Removing Group {}'.format(self.name))
        self.subnet.parents[0].getchildren()
        self.subnet.deldn()


class dhcpGroup(object):
    def __init__(self, name, dhcp_server):
        self.name = name
        group_class_list = ['top', 'dhcpGroup']
        try:
            self.group = dhcp_server.config + "cn={}".format(self.name)
            log.info('Initialising existing Group {}'.format(self.name))
        except:
            log.info('Adding new Group {}'.format(self.name))
            self.group = dhcp_server.config.addchild("cn={}".format(self.name), group_class_list, {'cn': self.name, 'objectClass': group_class_list})
            
            self.group.commit()

    def update(self, new_name=None, attrlist=None):
        if new_name is not None:
            pass
        if attrlist is not None:
            pass
        

    def delete(self):
        # TODO: Move all hosts from group prior to group removal
        log.info('Removing Group {}'.format(self.name))
        self.group.parents[0].getchildren()
        self.group.deldn()


class dhcpHost(object):
    def __init__(self, name, dhcpserver):
        self.name = name

    def update(self):
        pass

    def delete(self):
        pass

if __name__ == '__main__':
    
    dhcpsrv = dhcpServer('dhcpawn')
    new_subnet = dhcpSubnet('10.0.0.0', '24', dhcpsrv)
    another_subnet = dhcpSubnet('192.168.1.0', '24', dhcpsrv)
    another_subnet.delete()
    new_group = dhcpGroup('kickstart', dhcpsrv)
    another_group = dhcpGroup('local-disk', dhcpsrv)
    another_group.delete()
    # group_to_remove = dhcpGroup('local-disk', new_test)
    # group_to_remove.delete()