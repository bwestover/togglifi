# togglifi

Toggle Wi-Fi networks on/off in a Unifi Controller managed network.

Includes a basic Flask UI and an API for enabling/disabling selected Wi-FI networks using the unificontrol Python package.

### Build using an ENV file

1. Create a `.env` file containing:

   ```
   UNIFI_HOST=<ip or hostname for your Unifi controler>
   UNIFI_PW=<unifi admin password>
   MANAGED_NETWORK_IDS=<comma separate list of SSID/network names you want to manage>
   ```


2. Build docker container:

   (From the repo directory)
   ```
   $ docker build -t togglifi:latest .
   $ docker run --rm -it --env-file .env --name wifi-toggle -p 8000:8000 wifi-toggle
   ```
3. Access via localhost: `http://0.0.0.0:8000`


