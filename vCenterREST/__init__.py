import requests
import urllib3


class vCenter:
    def __init__(self, name):
        self.servername = name
        self.rest_url = 'https://%s/rest' % self.servername
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.session_id = False
        
    def connect(self, username, password):
        try:
            sess = requests.post(self.rest_url + '/com/vmware/cis/session', auth=(username, password), verify=False)
            response = sess.json()
            if type(response['value']) is str:
                self.session_id = response['value']
                print('successfully connected with session ID:', self.session_id, self.name)
            else:
                print('authentication failed', self.name, sess.text)
        except Exception as oops:
            print(oops)        
        
    def get_hosts(self):
        if self.session_id:
            response = requests.get(self.rest_url + '/vcenter/host', verify=False, headers={"vmware-api-session-id": self.session_id})
            data = response.json()
            print('enumerated', len(data['value']), 'hosts')
            return data['value']
        else:
            print('no session ID, please connect to vCenter first')
            return []

    def get_health(self):
        if self.session_id:
            response = requests.get(self.rest_url + '/appliance/health/system', verify=False, headers={"vmware-api-session-id": self.session_id})
            data = response.json()
            print('acquired appliance health')
            return data['value']
        else:
            print('no session ID, please connect to vCenter first')
            return None