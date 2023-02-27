import random
import datetime
import string
import csv
import uuid


#Right value for generate
organizationId = ["ft10" + str(i) for i in range(1,10)]
organizationId.append("ft110")
modelVersion = [i for i in range(1,6)]
applicationName = ["FsoftAgent.FsoftStreaming","FsoftAgent.FsoftStreamingMetricsCollector"]
id = ["A","B","C","D","E","F","G","H"]
message = ["Script finished without errors.","Can't start","Wrong ID","Pending"]
metricSubcategory = ['FREE', 'TOTAL', 'VARIABLE']
metricCategory = ['DISK', 'MEMORY', 'ENVIRONMENT']
unit = ['1', 'B']



def randomVersion():
	return str(random.randint(1,1000))+'.'+str(random.randint(1,1000))+'.'+str(random.randint(1,1000))+'.'+str(random.randint(1,1000))

def randomComputerName():
	return "DESKTOP-"+''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def randomTimeUtc():
	x = datetime.datetime.now()
	return(x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d")+"T"+x.strftime("%X"+"."+x.strftime("%f")+"Z"))

def randomService():
	with open('services.csv', newline='') as csvfile:
		services = csv.DictReader(csvfile)
		return random.choice([row['Name'] for row in services])


class MESSAGE:
    def __init__(self):
        self.messageId = str(uuid.uuid4())
        self.modelVersion = random.choice(modelVersion)
        self.organizationId = random.choice(organizationId)
        self.siteId = random.randint(100,5000)
        self.timeUtc = randomTimeUtc()
        self.creator = {
            'applicationName': random.choice(applicationName),
            'applicationVersion': randomVersion(),
            'computerName': randomComputerName()
            }
            
    def jSon(self):
        data = {
            'messageId': self.messageId,
            'modelVersion': self.modelVersion,
            'organizationId': self.organizationId,
            'siteId': self.siteId,
            'timeUtc': self.timeUtc,
            'creator': self.creator
            }
        return data
        
class DES(MESSAGE):
    def __init__(self):
        super().__init__()
        self.messageType = 'DES'
        self.body = {
            'configurationManifestInfo':{
                'version': "default-collector",
                'nextAttemptUtc': randomTimeUtc()
                }
            }
        
    def jSon(self):
        base = super().jSon()
        derive = {
            'messageType': self.messageType,
            'body': self.body
            }
        data = {**base, **derive}
        return data

        
class MET(MESSAGE):
    def __init__(self):
        super().__init__()
        self.messageType = 'MET'
        self.body = {
            'values':[
                {
                'id': random.choice(id),
                'metricCategory': random.choice(metricCategory),
                'metricSubcategory': random.choice(metricSubcategory),
                'unit': random.choice(unit),
                'valueInt': random.randint(1000000000,99999999999)
                }
                for i in range(11)
                ]
            }
        self.siteInfo = {
            'siteIds':{
                'id': "dp-preprod",
                'idType': "BSP_COMPANY_ID"
                }
        }
            
    def jSon(self):
        base = super().jSon()
        derive = {
            'messageType': self.messageType,
            'body': self.body,
            'siteInfo': self.siteInfo
            }
        data = {**base, **derive}
        return data
        
class SWR(MESSAGE):
    def __init__(self):
        super().__init__()
        self.messageType = 'SWR'
        self.body = {
            'software':[
                {
                'name': randomService(),
                'type': "TYPE_SERVICE",
                'version': "19.3.23.44",
                'startType': "START_MANUAL",
                'imagePath': "C:\\Program Files (x86)\\Fsoft Agent\\FsoftAgent.exe",
                'status': "STATUS_RUNNING"
                }
                for i in range(7)    
                ]
            }
        self.siteInfo = {
            'siteIds':{
                'id': str(uuid.uuid1().hex),
                'idType': "BSP_EU_ID"
                }
            }
            
    def jSon(self):
        base = super().jSon()
        derive = {
            'messageType': self.messageType,
            'body': self.body,
            'siteInfo': self.siteInfo
            }
        data = {**base, **derive}
        return data
        
class LOG(MESSAGE):
    def __init__(self):
        super().__init__()
        self.messageType = 'LOG'
        self.body = {
            'application':{
                'applicationName': random.choice(applicationName),
                'applicationVersion': randomVersion(),
                'computerName': randomComputerName()
                },
            'correlationid': str(uuid.uuid4()),
            'label':{
                'manifest': "master-manifest-1.0.7658.33113-3",
                'resource': "fluentBit"
                },
            'message': random.choice(message),
            'severity': "INFO"
            }

    def jSon(self):
        base = super().jSon()
        derive = {
            'messageType': self.messageType,
            'body': self.body
            }
        data = {**base, **derive}
        return data

