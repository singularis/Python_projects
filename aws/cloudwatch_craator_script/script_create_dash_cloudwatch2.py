import boto3
import json
client = boto3.client('elasticache')
client1 = boto3.client('cloudwatch', region_name='us-east-2')
arr = []
res = client.describe_replication_groups()
for i in res["ReplicationGroups"]:
    arr.append({i["ReplicationGroupId"] : i["MemberClusters"]})
dash = []
oy0 = 0 
oy1 = 1


def name_func(oy0, data):
    db_name = list(data.keys())[0]
    return {
   "height":1,
   "width":24,
   "y":oy0,
   "x":0,
   "type":"text",
   "properties":{
      "markdown":"# {}".format(db_name)
   }
}

def first_chart(oy1, data):
    db_name = list(data.keys())[0]
    nodes_list = list(data.values())[0]
    counter = 0
    payload = {
   "height":6,
   "width":12,
   "y":oy1,
   "x":0,
   "type":"metric",
   "properties":{
      "metrics":[
         [
            {
               "expression":"SUM(METRICS())",
               "label":db_name,
               "id":"e1",
               "region":"us-east-2",
               "period":60
            }
         ],
      ],
      "view":"timeSeries",
      "stacked": False,
      "region":"us-east-2",
      "stat":"Maximum",
      "period":60,
      "title":"Current DB Memory - {}".format(db_name)
   }
}
    for i in nodes_list:
        counter += 1
        payload["properties"]["metrics"].append([
            "AWS/ElastiCache",
            "BytesUsedForCache",
            "CacheClusterId",
            i,
            {
               "id":"m{}".format(counter),
               "visible": False
            }
         ])
    return payload

def second_chart(oy1, data):
    db_name = list(data.keys())[0]
    nodes_list = list(data.values())[0]
    counter = 0
    payload = {
   "height":6,
   "width":12,
   "y":oy1,
   "x":12,
   "type":"metric",
   "properties":{
      "metrics":[
         [
            {
               "expression":"SUM(METRICS())",
               "label":db_name,
               "id":"e1",
               "region":"us-east-2",
               "period":60
            }
         ],

      ],
      "view":"timeSeries",
      "stacked":False,
      "region":"us-east-2",
      "stat":"Maximum",
      "period":60,
      "title":"Current DB Ops/sec - {}".format(db_name)
   }
}
    for i in nodes_list:
        counter += 1
        payload["properties"]["metrics"].append([
            "AWS/ElastiCache",
            "SetTypeCmds",
            "CacheClusterId",
            i,
            {
               "id":"m{}".format(counter),
               "visible":False
            }
         ])
    for i in nodes_list:
        counter += 1
        payload["properties"]["metrics"].append([
            "AWS/ElastiCache",
            "GetTypeCmds",
            "CacheClusterId",
            i,
            {
               "id":"m{}".format(counter),
               "visible":False
            }
         ])
    return payload

for i in arr:
    dash.append(name_func(oy0, i))
    dash.append(first_chart(oy1, i))
    dash.append(second_chart(oy1, i))
    oy0 += 7
    oy1 += 7

client1.put_dashboard(DashboardName="PM_SRE_ElastiCaches_Basic_Dash_via_API", DashboardBody= str(json.dumps({"widgets" : dash})))
