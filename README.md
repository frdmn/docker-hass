# docker-hass

My docker-compose [Home Assistant](https://www.home-assistant.io/) setup.

## Installation

1. Make sure you've installed all requirements
2. Clone this repository:

```shell
git clone https://github.com/frdmn/docker-hass
```

3. Create a copy of the sample `.env` file and adjust it at will:

```shell
cp .env.sample .env
```

4. Spin up the containers:

```shell
docker-compose up -d
```

## Configuration

You can make use of the following environment variables / configurations:

| Environment variable | Default value | Description
|----------------------|---------------|------------|
| `TZ` | `Europe/Berlin` | Default timezone |
| `HASS_IMAGEVERSION` | `0.77.3` | Image version for Home Assistant |
| `DOCKERMON_IMAGEVERSION` | `v0.0.10` | Image version for docker-mon |
| `DOCKERMON_PORT` | `8126` | Default port for docker-mon |
| `OWNTRACKS_IMAGEVERSION` | `latest` | Image version for Owntracks |
| `OWNTRACKS_MQTTHOSTNAME` | `vpn.hostname.io` | Default MQTT hostname for Owntracks |
| `OWNTRACKS_IPLIST` | `192.168.1.250` | Default IP list for Owntracks |
| `OWNTRACKS_HOSTLIST` | `vpn.hostname.io` | Default host list for Owntracks |
| `OWNTRACKS_PORT_MQTT` | `1883` | Default port for Owntracks' MQTT |
| `OWNTRACKS_PORT_MQTTTLS` | `8883` | Default port for Owntracks' MQTT over TLS |
| `OWNTRACKS_PORT_WEB` | `8083` | Default port for Owntracks' webinterface |

## Usage

### Services

#### Start/create services

```shell
$ docker-compose up -d
Creating hass_dockermon_1 ... done
Creating hass_hass_1 ...      done
Creating hass_owntracks_1 ... done
```

#### Stop services

```shell
$ docker-compose stop
Stopping hass_dockermon_1 ... done
Stopping hass_hass_1 ...      done
Stopping hass_owntracks_1 ... done
```

#### Upgrade services

```shell
$ docker-compose stop
$ docker-compose pull
$ docker-compose rm
$ docker-compose up -d
```

#### Check logs

```shell
$ docker-compose logs -f
```

or for a specific container:

```shell
$ docker-compose logs -f hass
```

## Contributing

1. Fork it
2. Create your feature branch:

```shell
git checkout -b feature/my-new-feature
```

3. Commit your changes:

```shell
git commit -am 'Add some feature'
```

4. Push to the branch:

```shell
git push origin feature/my-new-feature
```

5. Submit a pull request

## Requirements / Dependencies

* Docker (incl. `docker-compose`)

## Version

1.0.0

## License

[MIT](LICENSE)
