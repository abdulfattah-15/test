import json
import os
import requests
import io
import time
from sys import stderr
from flask import Flask, request, jsonify, send_file
from requests.auth import HTTPBasicAuth
#from paramiko import SSHClient, AutoAddPolicy

app = Flask(__name__)

api_key = os.environ.get("API_KEY", "")
if api_key == "":
    print("api key is required", file=stderr)

api_base_url = "https://api.stagingv3.microgen.id/query/api/v1/" + api_key

@app.get("/")
def main():
    a = "server active"
    return a

@app.get("/hosts")
def hosts():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/hosts?fields=Hosts/rack_info,Hosts/host_name,Hosts/maintenance_state,Hosts/public_host_name,Hosts/cpu_count,Hosts/ph_cpu_count,alerts_summary,Hosts/host_status,Hosts/host_state,Hosts/last_heartbeat_time,Hosts/ip,host_components/HostRoles/state,host_components/HostRoles/maintenance_state,host_components/HostRoles/stale_configs,host_components/HostRoles/service_name,host_components/HostRoles/display_name,host_components/HostRoles/desired_admin_state,host_components/metrics/dfs/namenode/ClusterId,host_components/metrics/dfs/FSNamesystem/HAState,metrics/disk,metrics/load/load_one,Hosts/total_mem,stack_versions/HostStackVersions,stack_versions/repository_versions/RepositoryVersions/repository_version,stack_versions/repository_versions/RepositoryVersions/id,stack_versions/repository_versions/RepositoryVersions/display_name&minimal_response=true,host_components/logging&page_size=100&from=0&sortBy=Hosts/host_name.asc&_=1668495965572'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))
    return response.json()

@app.get("/host/memory")
def hostMem():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/hosts?fields=metrics/memory/mem_total,metrics/memory/mem_free,metrics/memory/mem_cached&_=1669173311623'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    return x

@app.get("/host/cpu")
def hostCPU():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/hosts?fields=metrics/cpu/cpu_wio&_=1669173311686'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    return x

@app.get("/host/disk")
def hostDisk():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/hosts?fields=metrics/disk/disk_free,metrics/disk/disk_total&_=1669173311729'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    return x

@app.get("/hive/summary")
def hive():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER%7CServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name&minimal_response=true&_=1667968440999'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    d = dict()
    b = 0
    d['items'] = {}
    for i in range(len(x["items"])):
        if x["items"][i]["ServiceComponentInfo"]["service_name"] == "HIVE":
            a = x["items"][i]
            d['items'][b] = a
            b += 1
    
    return d
@app.get("/mapreduce2")
def mapReduce():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER%7CServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name&minimal_response=true&_=1667968440999'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    a = x['items'][8]
    b = x['items'][15]
    d=dict()
    d['items'] = a,b

    return d

@app.get("/hbase/summary")
def hbase():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER%7CServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name&minimal_response=true&_=1667968440999'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    a = x['items'][6]

    return a

@app.get("/hbase/metrics")
def hbaseMetrics():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/services/HBASE/components/HBASE_REGIONSERVER?fields=metrics/hbase/regionserver/Server/Get_num_ops._rate[1668672332,1668675932,15],metrics/hbase/regionserver/Server/ScanNext_num_ops._rate[1668672332,1668675932,15],metrics/hbase/regionserver/Server/Append_num_ops._rate[1668672332,1668675932,15],metrics/hbase/regionserver/Server/Delete_num_ops._rate[1668672332,1668675932,15],metrics/hbase/regionserver/Server/Increment_num_ops._rate[1668672332,1668675932,15],metrics/hbase/regionserver/Server/Mutate_num_ops._rate[1668672332,1668675932,15],metrics/hbase/regionserver/Server/Get_95th_percentile._max[1668672332,1668675932,15],metrics/hbase/regionserver/Server/ScanNext_95th_percentile._max[1668672332,1668675932,15],metrics/hbase/regionserver/Server/Mutate_95th_percentile._max[1668672332,1668675932,15],metrics/hbase/regionserver/Server/Increment_95th_percentile._max[1668672332,1668675932,15],metrics/hbase/regionserver/Server/Append_95th_percentile._max[1668672332,1668675932,15],metrics/hbase/regionserver/Server/Delete_95th_percentile._max[1668672332,1668675932,15],metrics/hbase/ipc/IPC/numOpenConnections._sum[1668672332,1668675932,15],metrics/hbase/ipc/IPC/numActiveHandler._sum[1668672332,1668675932,15],metrics/hbase/ipc/IPC/numCallsInGeneralQueue._sum[1668672332,1668675932,15],metrics/hbase/regionserver/Server/updatesBlockedTime._rate[1668672332,1668675932,15],metrics/cpu/cpu_system._sum[1668672332,1668675932,15],metrics/cpu/cpu_user._sum[1668672332,1668675932,15],metrics/cpu/cpu_nice._sum[1668672332,1668675932,15],metrics/cpu/cpu_idle._sum[1668672332,1668675932,15],metrics/cpu/cpu_wio._sum[1668672332,1668675932,15],metrics/network/pkts_in._avg[1668672332,1668675932,15],metrics/network/pkts_out._avg[1668672332,1668675932,15],metrics/disk/read_bps._sum[1668672332,1668675932,15],metrics/disk/write_bps._sum[1668672332,1668675932,15]&format=null_padding&_=1668672315058'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    return x 



@app.get("/yarn/summary")
def yarn():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER%7CServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name&minimal_response=true&_=1667968440999'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    e = x['items'][0]
    a = x['items'][20]
    b = x['items'][27]
    c = x['items'][29]
    d=dict()
    d['items'] = e,a,b,c

    return d 


@app.get("/yarn/metrics")
def yarnMetrics():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/services/YARN/components/NODEMANAGER?fields=metrics/yarn/ContainersFailed._rate[1668673339,1668676939,15],metrics/yarn/ContainersCompleted._rate[1668673339,1668676939,15],metrics/yarn/ContainersLaunched._rate[1668673339,1668676939,15],metrics/yarn/ContainersIniting._sum[1668673339,1668676939,15],metrics/yarn/ContainersKilled._rate[1668673339,1668676939,15],metrics/yarn/ContainersRunning._sum[1668673339,1668676939,15],metrics/memory/mem_total._avg[1668673339,1668676939,15],metrics/memory/mem_free._avg[1668673339,1668676939,15],metrics/disk/read_bps._sum[1668673339,1668676939,15],metrics/disk/write_bps._sum[1668673339,1668676939,15],metrics/network/pkts_in._avg[1668673339,1668676939,15],metrics/network/pkts_out._avg[1668673339,1668676939,15],metrics/cpu/cpu_system._sum[1668673339,1668676939,15],metrics/cpu/cpu_user._sum[1668673339,1668676939,15],metrics/cpu/cpu_nice._sum[1668673339,1668676939,15],metrics/cpu/cpu_idle._sum[1668673339,1668676939,15],metrics/cpu/cpu_wio._sum[1668673339,1668676939,15]&format=null_padding&_=1668672315144'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password)) 

    return response.json()   

@app.get("/zookeeper/summary")
def zookeeper():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER%7CServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name&minimal_response=true&_=1667968440999'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    e = x['items'][32]

    return e

@app.get("/zeppelin/summary")
def zeppelin():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER%7CServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name&minimal_response=true&_=1667968440999'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    e = x['items'][30]

    return e

@app.get("/spark2/summary")
def spark2():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER%7CServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name&minimal_response=true&_=1667968440999'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    e = x['items'][23]

    return e

@app.get("/ambari/summary")
def ambari():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER%7CServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name&minimal_response=true&_=1667968440999'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    e = x['items'][16]
    a = x['items'][17]
    d=dict()
    d['items'] = e,a
    return d

@app.get("/ambari/metrics")
def ambariMetrics():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/services/AMBARI_METRICS/components/METRICS_COLLECTOR?fields=metrics/hbase/master/AverageLoad[1668675124,1668678724,15],metrics/hbase/regionserver/storefiles[1668675124,1668678724,15],metrics/hbase/regionserver/regions[1668675124,1668678724,15],metrics/hbase/regionserver/requests._rate[1668675124,1668678724,15],metrics/hbase/regionserver/blockCacheHitPercent[1668675124,1668678724,15],metrics/hbase/regionserver/compactionQueueSize[1668675124,1668678724,15]&_=1668672315308'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))
    
    return response.json()

@app.get("/infrasolr/summary")
def infraSolr():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER%7CServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name&minimal_response=true&_=1667968440999'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    e = x['items'][13]
    return e

@app.get("/superset/summary")
def superset():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER%7CServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name&minimal_response=true&_=1667968440999'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    e = x['items'][25]
    return e

@app.get("/druid/summary")
def druid():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER%7CServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name&minimal_response=true&_=1667968440999'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    e = x['items'][1]
    a = x['items'][2]
    b = x['items'][3]
    c = x['items'][4]
    d=dict()
    d['items'] = e,a,b,c

    return d 

@app.post("/hdfs/rename")
def hdfsRename():
    url = 'http://10.10.65.1:8080/api/v1/views/FILES/versions/1.0.0/instances/hdfs_viewer/resources/files/fileops/rename'
    username = "sapujagad"
    password = "kayangan"
    data = request.get_json()
    response = requests.post(url,json = data, auth = HTTPBasicAuth(username, password))
   

    return response.json()

def urlDownload(path):
    extensions = ['.png','jpg','jpeg','pdf', '.doc','.docx', '.xls','xlsx','.csv', '.tsv']
    if all(ext not in path for ext in extensions):
        username = "sapujagad"
        password = "kayangan"
        url = 'http://10.10.65.1:8080/api/v1/views/FILES/versions/1.0.0/instances/hdfs_viewer/resources/files/download/zip/generate-link'
        #data = request.get_json()
        data = {"download":True,
                "entries":["/"+ path]}
        response= requests.post(url, json=data, auth = HTTPBasicAuth(username, password))
        x = response.json()
        url1='http://10.10.65.1:8080/api/v1/views/FILES/versions/1.0.0/instances/hdfs_viewer/resources/files/download/zip?requestId='
        url1 += x['requestId']
        response1 = requests.get(url1, auth = HTTPBasicAuth(username, password))

        x = path 
        last = x.rsplit('/', 1)[-1]+".zip"

        z = response1.content
        memory_file = last
        with open(memory_file, 'wb') as zf:
            zf.write(z)
        
        return send_file(memory_file, attachment_filename=last, as_attachment=True)
    else:   
        username = "sapujagad"
        password = "kayangan" 
        url = 'http://10.10.65.1:8080/api/v1/views/FILES/versions/1.0.0/instances/hdfs_viewer/resources/files/download/browse?path=/' + path + '&download=true'
        response = requests.get(url, auth = HTTPBasicAuth(username, password))
        x = path 
        last = x.rsplit('/', 1)[-1]
        return send_file(io.BytesIO(response.content), attachment_filename=last, as_attachment=True)
    
@app.get("/hdfs/download/<path:path>")
def hdfsDownload(path):
    zf = urlDownload(path)
    return zf


@app.get("/hdfs/bytesw")
def hdfsBytesWrite():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/services/HDFS/components/DATANODE?fields=host_components/metrics/dfs/datanode/bytes_written&format=null_padding&_=1669268400225'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    return x

@app.get("/hdfs/gctime")
def hdfsGCTime():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/services/HDFS/components/DATANODE?fields=host_components/metrics/jvm/gcTimeMillis&format=null_padding&_=1669268400267'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    return x

@app.get("/hdfs/memuse")
def hdfsMemUsed():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/services/HDFS/components/DATANODE?fields=host_components/metrics/jvm/memHeapUsedM&format=null_padding&_=1669268400291'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    return x

@app.get("/hdfs/memcommit")
def hdfsMemCommit():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/services/HDFS/components/DATANODE?fields=host_components/metrics/jvm/memHeapCommittedM&format=null_padding&_=1669268400306'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    return x

@app.get("/hdfs/processdisk")
def hdfsProcessDisk():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/services/HDFS/components/DATANODE?fields=host_components/metrics/dfs/datanode/bytes_read,host_components/metrics/dfs/datanode/bytes_written,host_components/metrics/dfs/datanode/TotalReadTime,host_components/metrics/dfs/datanode/TotalWriteTime&format=null_padding&_=1669268400419'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    return x

@app.get("/hdfs/processnet")
def hdfsProcessNet():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/services/HDFS/components/DATANODE?fields=host_components/metrics/dfs/datanode/RemoteBytesRead,host_components/metrics/dfs/datanode/reads_from_remote_client,host_components/metrics/dfs/datanode/RemoteBytesWritten,host_components/metrics/dfs/datanode/writes_from_remote_client&format=null_padding&_=1669268400463'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    return x

@app.get("/hdfs/spaceutil")
def hdfsSpaceUtil():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/services/HDFS/components/DATANODE?fields=host_components/metrics/FSDatasetState/org/apache/hadoop/hdfs/server/datanode/fsdataset/impl/FsDatasetImpl/Remaining,host_components/metrics/dfs/datanode/Capacity&format=null_padding&_=1669268400383'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    return x

@app.get("/hdfs/bytesr")
def hdfsBytesRead():
    url = 'http://10.10.65.1:8080/api/v1/clusters/sapujagad/services/HDFS/components/DATANODE?fields=host_components/metrics/dfs/datanode/bytes_read&format=null_padding&_=1669268400355'
    username = "sapujagad"
    password = "kayangan"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    return x
@app.get("/namenode/cpu")
def namenodeCPU():
    url = 'http://10.207.26.20:8080/api/v1/clusters/gudanggaram/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER|ServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name,host_components/HostRoles/host_name,host_components/HostRoles/public_host_name,host_components/HostRoles/state,host_components/HostRoles/maintenance_state,host_components/HostRoles/stale_configs,host_components/HostRoles/ha_state,host_components/HostRoles/desired_admin_state,,host_components/metrics/jvm/memHeapUsedM,host_components/metrics/jvm/HeapMemoryMax,host_components/metrics/jvm/HeapMemoryUsed,host_components/metrics/jvm/memHeapCommittedM,host_components/metrics/mapred/jobtracker/trackers_decommissioned,host_components/metrics/cpu/cpu_wio,host_components/metrics/rpc/client/RpcQueueTime_avg_time,host_components/metrics/dfs/FSNamesystem/*,host_components/metrics/dfs/namenode/Version,host_components/metrics/dfs/namenode/LiveNodes,host_components/metrics/dfs/namenode/DeadNodes,host_components/metrics/dfs/namenode/DecomNodes,host_components/metrics/dfs/namenode/TotalFiles,host_components/metrics/dfs/namenode/UpgradeFinalized,host_components/metrics/dfs/namenode/Safemode,host_components/metrics/runtime/StartTime,host_components/metrics/dfs/namenode/ClusterId,host_components/metrics/yarn/Queue,host_components/metrics/yarn/ClusterMetrics/NumActiveNMs,host_components/metrics/yarn/ClusterMetrics/NumLostNMs,host_components/metrics/yarn/ClusterMetrics/NumUnhealthyNMs,host_components/metrics/yarn/ClusterMetrics/NumRebootedNMs,host_components/metrics/yarn/ClusterMetrics/NumDecommissionedNMs&minimal_response=true&_=1670226192151'
    username = "admin"
    password = "admin"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    d = dict()
    b = 0
    d['items'] = {}
    for i in range(len(x["items"])):
        if x["items"][i]["ServiceComponentInfo"]["component_name"] == "NAMENODE":
            a = x["items"][i]["host_components"][0]['metrics']["cpu"]
            d['items'][b] = a
            b += 1

    return d

@app.get("/namenode/rpc")
def namenodeRPC():
    url = 'http://10.207.26.20:8080/api/v1/clusters/gudanggaram/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER|ServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name,host_components/HostRoles/host_name,host_components/HostRoles/public_host_name,host_components/HostRoles/state,host_components/HostRoles/maintenance_state,host_components/HostRoles/stale_configs,host_components/HostRoles/ha_state,host_components/HostRoles/desired_admin_state,,host_components/metrics/jvm/memHeapUsedM,host_components/metrics/jvm/HeapMemoryMax,host_components/metrics/jvm/HeapMemoryUsed,host_components/metrics/jvm/memHeapCommittedM,host_components/metrics/mapred/jobtracker/trackers_decommissioned,host_components/metrics/cpu/cpu_wio,host_components/metrics/rpc/client/RpcQueueTime_avg_time,host_components/metrics/dfs/FSNamesystem/*,host_components/metrics/dfs/namenode/Version,host_components/metrics/dfs/namenode/LiveNodes,host_components/metrics/dfs/namenode/DeadNodes,host_components/metrics/dfs/namenode/DecomNodes,host_components/metrics/dfs/namenode/TotalFiles,host_components/metrics/dfs/namenode/UpgradeFinalized,host_components/metrics/dfs/namenode/Safemode,host_components/metrics/runtime/StartTime,host_components/metrics/dfs/namenode/ClusterId,host_components/metrics/yarn/Queue,host_components/metrics/yarn/ClusterMetrics/NumActiveNMs,host_components/metrics/yarn/ClusterMetrics/NumLostNMs,host_components/metrics/yarn/ClusterMetrics/NumUnhealthyNMs,host_components/metrics/yarn/ClusterMetrics/NumRebootedNMs,host_components/metrics/yarn/ClusterMetrics/NumDecommissionedNMs&minimal_response=true&_=1670226192151'
    username = "admin"
    password = "admin"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    d = dict()
    b = 0
    d['items'] = {}
    for i in range(len(x["items"])):
        if x["items"][i]["ServiceComponentInfo"]["component_name"] == "NAMENODE":
            a = x["items"][i]["host_components"][0]['metrics']["rpc"]
            d['items'][b] = a
            b += 1

    return d

@app.get("/namenode/uptime")
def namenodeRunTime():
    url = 'http://10.207.26.20:8080/api/v1/clusters/gudanggaram/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER|ServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name,host_components/HostRoles/host_name,host_components/HostRoles/public_host_name,host_components/HostRoles/state,host_components/HostRoles/maintenance_state,host_components/HostRoles/stale_configs,host_components/HostRoles/ha_state,host_components/HostRoles/desired_admin_state,,host_components/metrics/jvm/memHeapUsedM,host_components/metrics/jvm/HeapMemoryMax,host_components/metrics/jvm/HeapMemoryUsed,host_components/metrics/jvm/memHeapCommittedM,host_components/metrics/mapred/jobtracker/trackers_decommissioned,host_components/metrics/cpu/cpu_wio,host_components/metrics/rpc/client/RpcQueueTime_avg_time,host_components/metrics/dfs/FSNamesystem/*,host_components/metrics/dfs/namenode/Version,host_components/metrics/dfs/namenode/LiveNodes,host_components/metrics/dfs/namenode/DeadNodes,host_components/metrics/dfs/namenode/DecomNodes,host_components/metrics/dfs/namenode/TotalFiles,host_components/metrics/dfs/namenode/UpgradeFinalized,host_components/metrics/dfs/namenode/Safemode,host_components/metrics/runtime/StartTime,host_components/metrics/dfs/namenode/ClusterId,host_components/metrics/yarn/Queue,host_components/metrics/yarn/ClusterMetrics/NumActiveNMs,host_components/metrics/yarn/ClusterMetrics/NumLostNMs,host_components/metrics/yarn/ClusterMetrics/NumUnhealthyNMs,host_components/metrics/yarn/ClusterMetrics/NumRebootedNMs,host_components/metrics/yarn/ClusterMetrics/NumDecommissionedNMs&minimal_response=true&_=1670226192151'
    username = "admin"
    password = "admin"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    d = dict()
    b = 0
    d['items'] = {}
    for i in range(len(x["items"])):
        if x["items"][i]["ServiceComponentInfo"]["component_name"] == "NAMENODE":
            a = x["items"][i]["host_components"][0]['metrics']["runtime"]
            d['items'][b] = a
            b += 1

    return d

@app.get("/namenode/hdfs")
def namenodeHDFS():
    url = 'http://10.207.26.20:8080/api/v1/clusters/gudanggaram/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER|ServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name,host_components/HostRoles/host_name,host_components/HostRoles/public_host_name,host_components/HostRoles/state,host_components/HostRoles/maintenance_state,host_components/HostRoles/stale_configs,host_components/HostRoles/ha_state,host_components/HostRoles/desired_admin_state,,host_components/metrics/jvm/memHeapUsedM,host_components/metrics/jvm/HeapMemoryMax,host_components/metrics/jvm/HeapMemoryUsed,host_components/metrics/jvm/memHeapCommittedM,host_components/metrics/mapred/jobtracker/trackers_decommissioned,host_components/metrics/cpu/cpu_wio,host_components/metrics/rpc/client/RpcQueueTime_avg_time,host_components/metrics/dfs/FSNamesystem/*,host_components/metrics/dfs/namenode/Version,host_components/metrics/dfs/namenode/LiveNodes,host_components/metrics/dfs/namenode/DeadNodes,host_components/metrics/dfs/namenode/DecomNodes,host_components/metrics/dfs/namenode/TotalFiles,host_components/metrics/dfs/namenode/UpgradeFinalized,host_components/metrics/dfs/namenode/Safemode,host_components/metrics/runtime/StartTime,host_components/metrics/dfs/namenode/ClusterId,host_components/metrics/yarn/Queue,host_components/metrics/yarn/ClusterMetrics/NumActiveNMs,host_components/metrics/yarn/ClusterMetrics/NumLostNMs,host_components/metrics/yarn/ClusterMetrics/NumUnhealthyNMs,host_components/metrics/yarn/ClusterMetrics/NumRebootedNMs,host_components/metrics/yarn/ClusterMetrics/NumDecommissionedNMs&minimal_response=true&_=1670226192151'
    username = "admin"
    password = "admin"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    d = dict()
    b = 0
    d['items'] = {}
    for i in range(len(x["items"])):
        if x["items"][i]["ServiceComponentInfo"]["component_name"] == "NAMENODE":
            a = x["items"][i]["host_components"][0]['metrics']["dfs"]["FSNamesystem"]
            d['items'][b] = a
            b += 1

    return d

@app.get("/namenode/heap")
def namenodeHeap():
    url = 'http://10.207.26.20:8080/api/v1/clusters/gudanggaram/components/?ServiceComponentInfo/component_name=APP_TIMELINE_SERVER|ServiceComponentInfo/category.in(MASTER,CLIENT)&fields=ServiceComponentInfo/service_name,host_components/HostRoles/display_name,host_components/HostRoles/host_name,host_components/HostRoles/public_host_name,host_components/HostRoles/state,host_components/HostRoles/maintenance_state,host_components/HostRoles/stale_configs,host_components/HostRoles/ha_state,host_components/HostRoles/desired_admin_state,,host_components/metrics/jvm/memHeapUsedM,host_components/metrics/jvm/HeapMemoryMax,host_components/metrics/jvm/HeapMemoryUsed,host_components/metrics/jvm/memHeapCommittedM,host_components/metrics/mapred/jobtracker/trackers_decommissioned,host_components/metrics/cpu/cpu_wio,host_components/metrics/rpc/client/RpcQueueTime_avg_time,host_components/metrics/dfs/FSNamesystem/*,host_components/metrics/dfs/namenode/Version,host_components/metrics/dfs/namenode/LiveNodes,host_components/metrics/dfs/namenode/DeadNodes,host_components/metrics/dfs/namenode/DecomNodes,host_components/metrics/dfs/namenode/TotalFiles,host_components/metrics/dfs/namenode/UpgradeFinalized,host_components/metrics/dfs/namenode/Safemode,host_components/metrics/runtime/StartTime,host_components/metrics/dfs/namenode/ClusterId,host_components/metrics/yarn/Queue,host_components/metrics/yarn/ClusterMetrics/NumActiveNMs,host_components/metrics/yarn/ClusterMetrics/NumLostNMs,host_components/metrics/yarn/ClusterMetrics/NumUnhealthyNMs,host_components/metrics/yarn/ClusterMetrics/NumRebootedNMs,host_components/metrics/yarn/ClusterMetrics/NumDecommissionedNMs&minimal_response=true&_=1670226192151'
    username = "admin"
    password = "admin"
    response = requests.get(url, auth = HTTPBasicAuth(username, password))

    x = response.json()
    d = dict()
    b = 0
    d['items'] = {}
    for i in range(len(x["items"])):
        if x["items"][i]["ServiceComponentInfo"]["component_name"] == "NAMENODE":
            a = x["items"][i]["host_components"][0]['metrics']["jvm"]
            d['items'][b] = a
            b += 1

    return d

@app.get("/pythonPackage")
def pythonPackage():
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect('10.207.26.22', username="apps", password="apps247")
    stdin, stdout, stderr = client.exec_command('python3 -m pip list --format json\n')
    time.sleep(2)
    x = json.load(stdout)
    d = dict()
    d["items"]= {}
    d["items"] = x
    return  d

if __name__ == "__main__":
    app.run(debug=True)
