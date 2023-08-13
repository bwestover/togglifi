# togglifi

Toggle a Wi-Fi network on/off in a Unifi Controller managed network.

Includes a basic Flask UI and an API for enabling/disabling a single Wi-FI network using the unificontrol Python package.

### Build using an ENV file

1. Create a `.env` file containing:

   ```
   UNIFI_HOST=<ip or hostname for your Unifi controler>
   UNIFI_PW=<unifi admin password>
   UNIFI_WLAN_ID=<wlan ID for the network you want to toggle>
   ```

   Todo: I should create a tool/docs for determining the `UNIFI_WLAN_ID`. I got it using the `unificontrol` package locally

2. Build docker container:

   (From the repo directory)
   ```
   $ docker build -t togglifi:latest .
   $ docker run --rm -it --env-file .env --name wifi-toggle -p 8000:8000 wifi-toggle
   ```
3. Access via localhost: `http://0.0.0.0:8000`


