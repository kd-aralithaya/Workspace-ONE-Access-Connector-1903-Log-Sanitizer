# -*- coding: utf-8 -*-
"""

@author: dkrithi
"""

import re, os

def makeDirectories():

    for i in directories:
        path = os.path.join(parent_dir, i)
        os.makedirs(path)

def sanitizeLogs():
    for i in conf:
        with open(filepath+'/conf'+i,'r') as f:
            f = f.readlines()
        
        for line in f:
            with open(parent_dir + "/conf"+i, "a") as file1:
            # Writing data to a file
                if i == '/domain_krb.properties':
                    if re.match(LDAPname,str(line)):
                        m = re.match(LDAPname,str(line))
                        LDAP_server_name = m.group(2)
                        line_formatted = line.replace(LDAP_server_name, 'LDAPServerName')
                        print(line_formatted)
                        file1.write(line_formatted)
                    else:
                        print(line)
                        file1.write(line)
                elif i == '/runtime-config.properties':
                    if re.match(connector_hostname,str(line)):
                        m = re.match(connector_hostname,str(line))
                        connector = m.group(2)
                        line_formatted = line.replace(connector, 'ConnectorHostname')
                        print(line_formatted)
                        file1.write(line_formatted)
                    else:
                        print(line)
                        file1.write(line)
                else:
                        print(line)
                        file1.write(line)

           
    for filename in os.listdir(filepath+'/installerlogs'):
        print(filename)
        with open(filepath+'/installerlogs/'+filename, "r") as f:
            # Read each line of the file
            f = f.readlines()
        for line in f:
            with open(parent_dir +'/installerlogs/'+filename, "a") as file1:
                if connector in line:
                    line_formatted = line.replace(connector, 'ConnectorHostname')
                    print(line_formatted)
                    file1.write(line_formatted)
                else:
                    #print(line)
                    file1.write(line)


    for filename in os.listdir(filepath+'/logs'):
        print(filename)
        with open(filepath+'/logs/'+filename, "r") as f:
            # Read each line of the file
            f = f.readlines()
        for line in f:
            with open(parent_dir +'/logs/'+filename, "a") as file1:
                if connector in line:
                    line_formatted = line.replace(connector, 'ConnectorHostname')
                    print(line_formatted)
                    file1.write(line_formatted)
                elif LDAP_server_name in line:
                    line_formatted = line.replace(LDAP_server_name, 'LDAPServerName1')
                    print(line_formatted)
                    file1.write(line_formatted)
                elif re.match(servername,line):
                    m = re.match(servername,line)
                    LDAP_server_name_2 = m.group(2)
                    line_formatted = line.replace(LDAP_server_name_2, 'LDAPServerName2')
                    print(line_formatted)
                    file1.write(line_formatted)
                #elif LDAP_server_name_2 in line:
                   # line_formatted = line.replace(LDAP_server_name_2, 'LDAPServerName2')
                   # print(line_formatted)
                  #  file1.write(line_formatted)
                else:
                    #print(line)
                    file1.write(line)
                

    
filepath = "C:/Users/dkrithi/OneDrive - VMware, Inc/VMwareCorp/Desktop/Connector" #Enter your log file path here
directories = ['conf', 'installerlogs', 'logs', 'systemroot']
conf = ['/domain_krb.properties','/runtime-config.properties','/system-config.properties']
parent_dir = 'C:/Users/dkrithi/OneDrive - VMware, Inc/VMwareCorp/Desktop/SanitizedLogs'
servername = r'(\s+"java.naming.provider.url" : "ldap://)([A-Za-z0-9\.-]+)'
LDAPname = r'([A-Za-z0-9\.]+)=([A-Za-z0-9\.-]+)'
connector_hostname = r'([a-z]+.hostname=)([A-Za-z0-9\.-]+)'
makeDirectories()
sanitizeLogs()
    

