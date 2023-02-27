# receive nested json message
# parse to list of json

def parseDES(msg_decode):
    parseJson = [
        {
        "measurement": msg_decode['messageType'],
        "tags":{
            "messageId": msg_decode['messageId'],
            "modelVersion": msg_decode['modelVersion'],
            "organizationId": msg_decode["organizationId"],
            "siteId": msg_decode["siteId"],
            "timeUtc": msg_decode["timeUtc"],
            "creator.applicationName": msg_decode["creator"]["applicationName"],
            "creator.applicationVersion": msg_decode["creator"]["applicationVersion"],
            "creator.computerName": msg_decode["creator"]["computerName"]
        },
        "fields": {
            "body.configurationManifestInfo.version": msg_decode["body"]["configurationManifestInfo"]["version"],
            "body.configurationManifestInfo.nextAttemptUtc": msg_decode["body"]["configurationManifestInfo"]["nextAttemptUtc"]
        }
        }
    ]
    return parseJson

def parseMET(msg_decode):
    parseJson = [
        {
        "measurement": msg_decode['messageType'],
        "tags":{
            "messageId": msg_decode['messageId'],
            "modelVersion": msg_decode['modelVersion'],
            "organizationId": msg_decode["organizationId"],
            "siteId": msg_decode["siteId"],
            "timeUtc": msg_decode["timeUtc"],
            "creator.applicationName": msg_decode["creator"]["applicationName"],
            "creator.applicationVersion": msg_decode["creator"]["applicationVersion"],
            "creator.computerName": msg_decode["creator"]["computerName"]
        },
        "fields": {
            "body.values.id": msg_decode["body"]["values"][i]["id"],
            "body.values.metricCategory": msg_decode["body"]["values"][i]["metricCategory"],
            "body.values.metricSubcategory": msg_decode["body"]["values"][i]["metricSubcategory"],
            "body.values.unit": msg_decode["body"]["values"][i]["unit"],
            "body.values.valueInt": msg_decode["body"]["values"][i]["valueInt"],
            "siteInfo.siteIds.id": msg_decode["siteInfo"]["siteIds"]["id"],
            "siteInfo.siteIds.idType": msg_decode["siteInfo"]["siteIds"]["idType"]
        }
        }
        for i in range(11)
    ]
    return parseJson

def parseSWR(msg_decode):
    parseJson = [
        {
        "measurement": msg_decode['messageType'],
        "tags":{
            "messageId": msg_decode['messageId'],
            "modelVersion": msg_decode['modelVersion'],
            "organizationId": msg_decode["organizationId"],
            "siteId": msg_decode["siteId"],
            "timeUtc": msg_decode["timeUtc"],
            "creator.applicationName": msg_decode["creator"]["applicationName"],
            "creator.applicationVersion": msg_decode["creator"]["applicationVersion"],
            "creator.computerName": msg_decode["creator"]["computerName"]
        },
        "fields": {
            "body.software.name": msg_decode["body"]["software"][i]["name"],
            "body.software.type": msg_decode["body"]["software"][i]["type"],
            "body.software.version": msg_decode["body"]["software"][i]["version"],
            "body.software.startType": msg_decode["body"]["software"][i]["startType"],
            "body.software.imagePath": msg_decode["body"]["software"][i]["imagePath"],
            "body.software.status": msg_decode["body"]["software"][i]["status"],
            "siteInfo.siteIds.id": msg_decode["siteInfo"]["siteIds"]["id"],
            "siteInfo.siteIds.idType": msg_decode["siteInfo"]["siteIds"]["idType"]
        }
        }
        for i in range(7)
    ]
    return parseJson

def parseLOG(msg_decode):
    parseJson = [
        {
        "measurement": msg_decode['messageType'],
        "tags":{
            "messageId": msg_decode['messageId'],
            "modelVersion": msg_decode['modelVersion'],
            "organizationId": msg_decode["organizationId"],
            "siteId": msg_decode["siteId"],
            "timeUtc": msg_decode["timeUtc"],
            "creator.applicationName": msg_decode["creator"]["applicationName"],
            "creator.applicationVersion": msg_decode["creator"]["applicationVersion"],
            "creator.computerName": msg_decode["creator"]["computerName"]
        },
        "fields": {
            "body.application.applicationName": msg_decode["body"]["application"]["applicationName"],
            "body.application.applicationVersion": msg_decode["body"]["application"]["applicationVersion"],
            "body.application.computerName": msg_decode["body"]["application"]["computerName"],
            "body.correlationid": msg_decode["body"]["correlationid"],
            "body.label.manifest": msg_decode["body"]["label"]["manifest"],
            "body.label.resource": msg_decode["body"]["label"]["resource"],
            "body.message": msg_decode["body"]["message"],
            "body.severity": msg_decode["body"]["severity"]
        }
        }
    ]
    return parseJson