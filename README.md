# nestbox-confd-client

A python client library to access nestbox-confd

## Usage

### Creating a client

```python
from nestbox_confd_client import Client
client = Client('<nestbox hostname>', token='<auth token>')
```

### Fetching the server config

```python
client.config.get()
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
