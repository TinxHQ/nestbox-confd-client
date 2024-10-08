# nestbox-confd-client

A python client library to access nestbox-confd

## Usage

### Creating a client

```python
from nestbox_confd_client import Client
client = Client('<nestbox hostname>', token='<auth token>')
```

## Config

### Fetching the server config

```python
client.config.get()
```

## Status

### Check the server status

```python
client.status.check()
```

## Customers

### Listing customers

```python
client.customers.list()
```

### Add a new customer

```python
customer = {
    'name': 'test',
    'reseller_uuid': '00000000-0000-0000-0000-000000000001'
}
client.customers.create(customer)
```

### Get a customer

```python
client.customers.get(customer_uuid)
```

### Update a customer

```python
client.customers.update(customer_uuid, new_customer)
```

### Delete a customer

```python
client.customers.delete(customer_uuid)
```

## Locations

### Listing locations

```python
client.locations.list()
```

### Add a new location

```python
location = {
    'name': 'test',
    'customer_uuid': '00000000-0000-0000-0000-000000000001'
}
client.locations.create(location)
```

### Get a location

```python
client.locations.get(location_uuid)
```

### Update a location

```python
client.locations.update(location_uuid, new_location)
```

### Delete a location

```python
client.locations.delete(location_uuid)
```

### Update wazo tenants

```python
wazo_tenants = [
    {'uuid': '1234-abcd', 'instance_uuid': '5678-efgh', 'credential_uuid': '32425-srfegs'},
    {'uuid': '9874-xyzw', 'instance_uuid': '7896-mnop', 'credential_uuid': '34623-sdbfxc'},
]
client.locations.update_wazo_tenants(location_uuid, wazo_tenants)
```

## Resellers

### Listing resellers

```python
client.resellers.list()
```

### Add a new reseller

```python
reseller = {
    'name': 'test',
}
client.resellers.create(reseller)
```

### Get a reseller

```python
client.resellers.get(reseller_uuid)
```

### Update a reseller

```python
client.resellers.update(reseller_uuid, new_reseller)
```

### Delete a reseller

```python
client.resellers.delete(reseller_uuid)
```

## User

### Listing users

```python
client.users.list()
```

### Add a new user

```python
user = {
    'visualizarion': 'some data'
}
client.users.create(user)
```

### Get a user

```python
client.users.get(user_uuid)
```

### Update a user

```python
client.users.update(user_uuid, new_user)
```

### Delete a user

```python
client.users.delete(user_uuid)
```

## Initialize

### Initialize nestbox-confd

```python
init = {
    'reseller': {
        'uuid': '00000000-0000-0000-0000-000000000001',
        'name': 'Super admin'
    }
}
client.init.run(init)
```

## Instance

### listing instances

```python
client.instances.list()
```

## Engine

### Send an account event

```python
event = {
    'name': 'create',
    'engine_uuid': '00000000-0000-0000-0000-000000000001',
    'engine_tenant_uuid': '00000000-0000-0000-0000-000000000002',
    'engine_account_uuid': '00000000-0000-0000-0000-000000000003',
    'engine_account_subscription': 1,
    'timestamp': '2018-04-10T12:59:09',
}
client.engines.create_account_event(instance_uuid, event)
```

### Check accounts hash

```python
client.engines.check_accounts_hash(instance_uuid, hash_)
```

### Synchronize accounts

```python
engine_version = '22.02'
accounts = [{
    'engine_uuid': '00000000-0000-0000-0000-000000000001',
    'engine_tenant_uuid': '00000000-0000-0000-0000-000000000002',
    'engine_account_uuid': '00000000-0000-0000-0000-000000000003',
    'engine_account_subscription': 1,
    'created_at': '2018-04-10T12:59:09',
}]
client.engines.synchronize_accounts(instance_uuid, accounts, engine_version)
```

## Accounts

### List accounts summaries

```python
client.accounts.get_summaries()
```

### List accounts

```python
client.accounts.list()
```

## Tenants

### Get a tenant

```python
client.tenants.get(tenant_uuid)
```

## Plugins

### Get a plugin

```python
client.plugins.get(plugin_uuid)
```

### List plugins

```python
client.plugins.list_(tenant_uuid)
```

### Create a plugin

```python
plugin_args = {
    'configuration': {},
    'manifest_url': '<url>',
    'enabled': <true/false>,
    'shared': <true/false>,
}
client.plugins.create(plugin_args)
```

### Update a plugin

```python
plugin_args = {
    'configuration': {},
    'enabled': <true/false>,
    'shared': <true/false>,
}
client.plugins.update(plugin_uuid, plugin_args)
```

### Delete a plugin

```python
client.plugins.delete(plugin_uuid)
```

### Install (copy) a plugin to a subtenant

```python
# for a reseller
client.plugins.install_to_reseller(plugin_uuid, reseller_uuid)

# for a customer
client.plugins.install_to_customer(plugin_uuid, customer_uuid)

# for a location
client.plugins.install_to_location(plugin_uuid, location_uuid)
```

### List a plugin installations into subtenants

```python
# list this plugin installations on resellers
client.plugins.list_reseller_installs(plugin_uuid)

# list this plugin installations on customers
client.plugins.list_customer_installs(plugin_uuid)

# list this plugin installations on locations
client.plugins.list_location_installs(plugin_uuid)
```

## Debian package

Follow the following steps to build a debian package for nestbox-confd-client manually.

1. Copy the source directory to a machine with all dependencies installed

```sh
rsync -av . <builder-host>:~/nestbox-confd-client
```

2. On the host, increment the changelog

```sh
dch -i
```

3. Build the package

```sh
dpkg-buildpackage -us -uc
```
