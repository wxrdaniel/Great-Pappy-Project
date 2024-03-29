#!/usr/bin/env python3
# @Date:   Jul-05-2017
# @Project: Great Pappy Project
# @Filename: getpappy.py
# @Last modified time: Jul-08-2017
#
#
#
#                      `-:+poweredo+:-`
#                 `:whmmhyo+/::::/+oyhNmhe:`
#              `+rNh+-               +Nh:ohNe+`
#            :dBy:                 .ve+     :sPr:
#          /mm+`                  :Nd.scafeyo:.+Nd:
#        .dN+`                   sMo     `.:+hNy.oMh.
#       /Nd`                   -dN:           -mm..dN:
#      +Ms                    /Mh`ym           .My  yM/
#     /Ms                   `hM+  hM            Nh   yM:
#    .MN                   -Nm-   hM           -My    dN`
#    yMM-                 oMy.dmy.hM         -sMy/o.  :Ms
#   `MdMh               .dN:   `+.hMold-fashion- .eN.  dN
#   .MsyM-             /Nh.       hM++/s//:.      +Mo  sM.
#   .Ms-Ms           `yMo         hM  :M+         yM-  sM.
#   .Ms dM.         -mm/o.        hM  :M+ ...-:/smm/   yM.
#    Nm :Ms        oMy`:My        hM  :MmddmMMMd/-     Nm
#    sM: mN      .dN/   :Nm+.     hM  :M+   `:omNs.   +M+
#    `mm`+M+    /Nd.      :yNmyo/.+s  :M+       .yMs``Nd
#     -Nd`Nm  `sMo `:        `:oyhmmh+:s.         :NhdN.
#      :MhsM/-mm: +Nh`             `:smmo.         +MN-
#       .mNMmNy` yM/                   -hNs       :Nd.
#        `oMMs  sM/                      /Nh    -hNo
#          .yMy/Md                        +M+ :hNs`
#            `omMm-                       :Mmmm+`
#               -sdNh+:`              `:ohNdo.
#                  `/oydNdhyssssssyhdNdyo:`
#                        `.::::::::.`
#
# Copyright (c) 2017 by wxrdaniel. All Rights Reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import requests
import sys
import time
import os

from html.parser import HTMLParser

# General Settings
name_db  = [('Test', 'Name')]
log_file = "log"
name_log = "name.log"
email_log = "mail.log"

# Set Target
target_post = "http://www.abcfws.com/catalog/oos_email.cmd"

# POST Data Dictionary
post_data   = {'productName': 'bourbon',
                'fname': '',
                'lname': '',
                'email': '',
                'form_state': 'ajaxToken',
                'csrfToken': 'ZmM0OGVjNmZmNWM4NDBhOGE0OTM2NDhkNTYxYTA1OTA=',
                'keep_tokens': 'keep_tokens'}


# Add Welcome and Help Info.
def welcome_help():
    os.system("clear")
    print("""
          * ***
        *  ****  *                                 *
       *  *  ****                                 **
      *  **   **                                  **
     *  ***        ***  ****                    ********
    **   **         **** **** * ***       **** ********
    **   **   ***    **   **** * ***     * ***  * **
    **   **  ****  * **       *   ***   *   ****  **
    **   ** *  ****  **      **    *** **    **   **
    **   ***    **   **      ********  **    **   **
     **  **     *    **      *******   **    **   **
      ** *      *    **      **        **    **   **
       ***     *     ***     ****    * **    **   **
        *******       ***     *******   ***** **   **
          ***                  *****     ***   **
            ***** **
         ******  ****
        **   *  *  ***
       *    *  *    ***
           *  *      **             ****     ****   **   ****
          ** **      **  ****      * ***  * * ***  * **    ***  *
          ** **      ** * ***  *  *   **** *   ****  **     ****
        **** **      * *   ****  **    ** **    **   **      **
       * *** **     * **    **   **    ** **    **   **      **
          ** *******  **    **   **    ** **    **   **      **
          ** ******   **    **   **    ** **    **   **      **
          ** **       **    **   **    ** **    **   **      **
          ** **       **    **   *******  *******     *********
          ** **        ***** **  ******   ******        **** ***
     **   ** **         ***   ** **       **                  ***
    ***   *  *                   **       **           *****   ***
     ***    *                    **       **         ********  **
      ******                      **       **       *      ****
        *** ***** **
         ******  ****                           *                         *
        **   *  *  ***                         ***                       **
       *    *  *    ***                         *                        **
           *  *      ** ***  ****     ****                             ********
          ** **      **  **** **** * * ***  * ***      ***       **** ********
          ** **      **   **   **** *   ****   ***    * ***     * ***  * **
        **** **      *    **       **    **     **   *   ***   *   ****  **
       * *** **     *     **       **    **     *   **    *** **         **
          ** *******      **       **    **    *    ********  **         **
          ** ******       **       **    **   ***   *******   **         **
          ** **           **       **    **    ***  **        **         **
          ** **           ***       ******      *** ****    * ***     *  **
          ** **            ***       ****        *** *******   *******    **
     **   ** **                                   **  *****     *****
    ***   *  *                                    **
     ***    *                                     *
      ******                                     *
        ***                                     *
""")
    time.sleep(2.35)
    print("""
                    [ Version: 1.0 beta ]

    ========================================================

    ===                                                  ===
    =-           Usage: python ./getpappy.py              -=
    =                                                      =
    =-          Help: ./getpappy.py -h  (--help)          -=
    ===                                                  ===

    ========================================================


    """)


# User Pick Name Function
# User pick name from the name list in general settings.
def set_name(input_name_list):
    # Set variables
    name_pool = input_name_list
    name_pool_size = len(name_pool)

    # Print Section name_pool
    print("===== Select Name Section =====\n......\n......\n")

    for i in range(name_pool_size):
        print('[%s]' % (i) + ' ' + str(name_pool[i][0]) + ' ' + str(name_pool[i][1]))
        i += 1

    # User input verification
    while True:
        try:
            user_input = int(input("\nPlease select a name:[0-9]  "))
        except ValueError:
            print("Can't you read!?")
            continue
        else:
            if 0 <= user_input < name_pool_size:
                break
            else:
                print("Are you an idiot!?")
                continue

    # Return Chosen Name.
    picked_name = name_pool[user_input]
    # uncomment for debug
#    print(picked_name)
    return picked_name


# Get all email from email list
def email_sample(input_email_list):
    ef = open(input_email_list, 'r')
    email_pool = []
    for e in ef:
        email_pool.append(e.rstrip())
    return email_pool
    ef.close()


# List out current folder file to find email list.
# Cross-platform supported: OSX/*nix/Windows
def list_current_dir():
    os_run = os.name
    if os_run == "nt":
        os.system("dir")
    elif os_run == "posix":
        os.system("ls")


# Main fucntion
def dump_it_in():
    # Print welcome message
    welcome_help()
    name        = set_name(name_db)
    fname = name[0]
    lname = name[1]
    full_name = str(fname + ' ' + lname)
    list_current_dir()
    email_sample_list  = input("Email List Filename: ")
    email_list       = email_sample(email_sample_list)
    email_size = len(email_list)

    # Add timestamp to the log file
    timestamp = "\n" + time.ctime() + "\n"
    log = open("response.log", "a+")
    log.write(timestamp)
    log.close()

    while True:
        print("Start Submitting...\n...\n...\n...")
        for count in range(email_size):
            email = email_list[count]
            left_count = email_size - count
            post_data['fname'] = fname
            post_data['lname'] = lname
            post_data['email'] = email
            print("Submitting:\n%s %s : %s (%d left)" % (fname, lname, email, left_count))

            # Remove for debug
            #print(email)

            # Hijack Stdout for logfile
            response_log = open("response.log", "a+")
            response_output = sys.stdout
            sys.stdout = response_log

            # Log Current Entry
            print("%s %s : %s" % (fname, lname, email))

            # POST Request
            r = requests.post(target_post, post_data)
            print("............ %d %s" % (r.status_code, r.reason))

            # End stdout hijack
            sys.stdout = response_output
            response_log.close()

            print("............ %d %s" % (r.status_code, r.reason))

            count += 1

            # Delay Factor
            time.sleep(0.45)
        break


welcome_help()
#dump_it_in()
#set_name(name_db)
#output_log("Daniel Pan", "asdfdfa@adf.com")
