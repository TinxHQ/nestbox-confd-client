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
