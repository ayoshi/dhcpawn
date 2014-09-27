MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'user'
MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'api_test'
IF_MATCH = False
# HATEOAS = False

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

hosts_schema = {
    'name': {
        'type': 'string',
    },
    'mac': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'unique': True,
        'required': True,
    },
    'group': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'groups',
            'field': '_id',
            'embeddable': True,
        },
    },
    'static_lease': {
        'type': 'dict',
        'schema': {
            'subnet': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'subnets',
                    'field': '_id',
                    # 'embeddable': True,
                },
            },
            # 'ip_address': {
            #     'type': 'string',
            #     'readonly': True,
            # }
        },
        'nullable': True,
    },
    'ip_address': {
        'type': 'string',
        'readonly': True,
    }
}

groups_schema = {
    'name': {
        'type': 'string',
    }
}

subnets_schema = {
    'name': {
        'type': 'string',
    },
    'netmask': {
        'type': 'string',
    },
    'broadcast_address': {
        'type': 'string',
    },
    'routers': {
        'type': 'string',
    },
}

dhcp_server_schema ={ 
    'hostname': {
        'type': 'string',
    },
}

hosts = {
    'schema': hosts_schema
}

groups = {
    'schema': groups_schema
}

subnets = {
    'schema': subnets_schema
}


DOMAIN = {
    'hosts': hosts,
    'subnets': subnets,
    'groups': groups,
}
