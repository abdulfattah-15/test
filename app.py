import json
import os
import requests
from sys import stderr
from flask import Flask, request, jsonify

app = Flask(__name__)

api_key = os.environ.get("API_KEY", "")
if api_key == "":
    print("api key is required", file=stderr)

api_base_url = "https://api.stagingv3.microgen.id/query/api/v1/" + api_key

@app.get("/hosts")
def hosts():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/hosts?fields=Hosts/rack_info,Hosts/host_name,Hosts/maintenance_state,Hosts/public_host_name,Hosts/cpu_count,Hosts/ph_cpu_count,alerts_summary,Hosts/host_status,Hosts/host_state,Hosts/last_heartbeat_time,Hosts/ip,host_components/HostRoles/state,host_components/HostRoles/maintenance_state,host_components/HostRoles/stale_configs,host_components/HostRoles/service_name,host_components/HostRoles/display_name,host_components/HostRoles/desired_admin_state,host_components/metrics/dfs/namenode/ClusterId,host_components/metrics/dfs/FSNamesystem/HAState,metrics/disk,metrics/load/load_one,Hosts/total_mem,stack_versions/HostStackVersions,stack_versions/repository_versions/RepositoryVersions/repository_version,stack_versions/repository_versions/RepositoryVersions/id,stack_versions/repository_versions/RepositoryVersions/display_name&minimal_response=true,host_components/logging&page_size=100&from=0&sortBy=Hosts/host_name.asc&_=1668495965572'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)
