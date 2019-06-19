# Example-9.py

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='python_user', \
                                     password='some_pass', \
                                     database='mybuilddb')
cursor = mariadb_connection.cursor()

cursor.execute("SELECT domain_name,userid,cmd FROM domains, jobs " + \
 "WHERE domains.domain_name=%s " + \
 "AND domains.domain_name=jobs.domain_name", \
 ("RHEL7.2-x86_64-1",))

for job_name, userid, cmd in cursor:
    print("Job name: {}, Userid: {}, Cmd: {}").format(job_name, \
                                                      userid,cmd)
