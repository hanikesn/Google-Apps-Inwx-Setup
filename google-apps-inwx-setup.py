#!/usr/bin/python2

# This file is part of Google-Apps-Inwx-Setup.
#
# Google-Apps-Inwx-Setup is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Google-Apps-Inwx-Setup is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Google-Apps-Inwx-Setup. If not, see <http://www.gnu.org/licenses/>.
__author__ = 'Steffen Hanikel'

from inwx import domrobot
import getpass

def main():
    username = raw_input("Please enter your user name: ")
    password = getpass.getpass("Please enter your password: ")

    inwx_conn = domrobot('https://api.domrobot.com/xmlrpc', username, password, 'en', True, False)

    domainname = raw_input("Please enter the domain name: ")

    site_verification =  raw_input("Please enter the site verification code: ")

    # verification
    inwx_conn.nameserver.createRecord({'domain':domainname, 'type':'TXT', 'content':site_verification})

    # mx records
    inwx_conn.nameserver.createRecord({'domain':domainname, 'type':'MX', 'prio':1, 'content':'ASPMX.L.GOOGLE.COM'})
    inwx_conn.nameserver.createRecord({'domain':domainname, 'type':'MX', 'prio':5, 'content':'ALT1.ASPMX.L.GOOGLE.COM'})
    inwx_conn.nameserver.createRecord({'domain':domainname, 'type':'MX', 'prio':5, 'content':'ALT2.ASPMX.L.GOOGLE.COM'})
    inwx_conn.nameserver.createRecord({'domain':domainname, 'type':'MX', 'prio':10, 'content':'ASPMX2.GOOGLEMAIL.COM'})
    inwx_conn.nameserver.createRecord({'domain':domainname, 'type':'MX', 'prio':10, 'content':'ASPMX3.GOOGLEMAIL.COM'})

    inwx_conn.nameserver.createRecord({'domain':domainname, 'type':'CNAME', 'name':'mail', 'content':'ghs.google.com'})

    dkim_name =  raw_input("Please enter the dkim name : ")
    dkim_data =  raw_input("Please enter the dkim record : ")

    # dkim
    inwx_conn.nameserver.createRecord({'domain':domainname, 'type':'TXT', 'name':dkim_name, 'content':dkim_data})

if __name__ == '__main__':
    main()
