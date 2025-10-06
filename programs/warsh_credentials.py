import warshaccess as wa

CS_credentials = wa.get_credentials('CS_3')
host_ip = CS_credentials['host']
cluster = CS_credentials['cluster_name']