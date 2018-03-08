# nestbox-confd-client

A python client library to access nestbox-confd

## Usage

## Config

```python
client.config()
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
