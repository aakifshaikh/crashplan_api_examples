# Copyright (c) 2016, 2017, 2018 Code42, Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.

# File: c42SharedLibrary.py
# Last Modified: 2018-09-24
#   Modified By: Paul H.

# Author: AJ LaVenture
# Author: Paul Hirst
# Author: Hank Brekke
# Author: Jack Phinney
#
# Common and reused functions to allow for rapid script creation
#
# install pip
# sudo pip install requests
# sudo pip install python-dateutil [-update]

# *****************************************************************************


# Check if the shared library is being run and not imported.  If being run exit.

isBeta = False
import sys

if __name__ == '__main__':
    print ""
    print "********** " + str(__file__) + " is a shared library and not meant to be run independently."
    print "           Exiting."
    print ""
    sys.exit(0)

if isBeta:
    print ("\n\n")
    print ("*****************************************************************************")
    print ("*****************************************************************************")
    print ("**********                                                         **********")
    print ("**********                                                         **********")
    print ("**********                                                         **********")
    print ("**********   THIS IS A DEVELOPMENT BRANCH OF THE SHARED LIBRARY.   **********")
    print ("**********                                                         **********")
    print ("**********               DO NOT USE FOR PRODUCTION!!!              **********")
    print ("**********                                                         **********")
    print ("**********                                                         **********")
    print ("*****************************************************************************")
    print ("*****************************************************************************")
    print ("\n\n")
    '''
    okToBeta = False
    okToBeta = raw_input("Yes, I know it's beta.  Use it anyway (y/n)? ")


    if okToBeta.lower() != 'y' and \
       okToBeta.lower() != 'yes' and \
       okToBeta.lower() != "ok":
       sys.exit(0)
    '''

import math
import json
import csv
import base64
import logging
import requests
import math
from dateutil.relativedelta import *
import datetime
import calendar
import re
import getpass
import os
import collections
from requests.exceptions import ConnectionError
import time
#import ijson.backends.yajl2 as ijson
import ijson
import pandas as pd
from contextlib import closing
import codecs
import ssl

class c42Lib(object):

    cp_c42Lib_version = '1.7.9'.split('.')

    # Set to your environments values
    #cp_host = "<HOST OR IP ADDRESS>" ex: http://localhost or https://localhost
    #cp_port = "<PORT>" ex: 4280 or 4285
    #cp_username = "<username>"
    #cp_password = "<pw>"

    # Test values
    #cp_host = "http://localhost"
    #cp_port = "4280"
    #cp_username = "admin"
    #cp_password = "admin"
    #cp_magic_restoreRecordKey = '987db1c5-8840-41f1-8c97-460d03347895'

    # REST API Calls

    cp_api_restoreHistory = "/api/restoreHistory"
    #?pgNum=1&pgSize=50&srtKey=startDate&srtDir=desc&days=9999&orgId=35
    cp_api_archive = "/api/Archive"
    cp_api_archiveMetadata = "/api/ArchiveMetadata"
    cp_api_authToken = "/api/AuthToken"
    cp_api_cli = "/api/cli"
    cp_api_coldStorage = "/api/ColdStorage"
    cp_api_computer = "/api/Computer"
    cp_api_computerBlock = "/api/ComputerBlock"
    cp_api_computerActivity = "/api/ComputerActivity"
    cp_api_customerLicense = "/c42api/v3/customerLicense"  #Unsupported API - use at your own peril!
    cp_api_dataKeyToken = "/api/DataKeyToken"
    cp_api_deacivateDevice = "/api/ComputerDeactivation"
    cp_api_deactivateUser = "/api/UserDeactivation"
    cp_api_destination = "/api/Destination"
    cp_api_deviceBackupReport = "/api/DeviceBackupReport"
    cp_api_deviceUpgrade = "/api/DeviceUpgrade"
    cp_api_directorySync = "/api/DirectorySync"
    cp_api_ekr = "/api/EKR"
    cp_api_fileContent = "/api/FileContent"
    cp_api_fileMetadata = "/api/FileMetadata"
    cp_api_jwtAuthToken = '/c42api/v3/auth/jwt'
    cp_api_legaHold = "/api/LegalHold"
    cp_api_legalHoldMembership = "/api/LegalHoldMembership"
    cp_api_legalHoldMembershipDeactivation = "/api/LegalHoldMembershipDeactivation"
    cp_api_loginToken = "/api/v1/LoginToken"
    cp_api_masterLicense = "/api/MasterLicense"
    cp_api_networkTest = "/api/NetworkTest"
    cp_api_org = "/api/Org"
    cp_api_orgDeactivation = "/api/OrgDeactivation"
    cp_api_orgSettings = "/api/OrgSettings"
    cp_api_ping = "/api/Ping"
    cp_api_plan = "/api/Plan"
    cp_api_pushRestoreJob = "/api/PushRestoreJob"
    cp_api_restoreRecord = "/api/RestoreRecord"
    cp_api_server = "/api/Server"
    cp_api_smartsearch = "/api/SmartSearch"
    cp_api_storage = "/api/Storage"
    cp_api_storageAuthToken = "/api/StorageAuthToken"
    cp_api_storedBytesHistory = "/api/StoredBytesHistory"
    cp_api_storePoint = "/api/StorePoint"
    cp_api_user = "/api/User"
    cp_api_userMoveProcess = "/api/UserMoveProcess"
    cp_api_userRole = "/api/UserRole"
    cp_api_webRestoreJob = "/api/WebRestoreJob"
    cp_api_webRestoreJobResult = "/api/WebRestoreJobResult"
    cp_api_webRestoreSearch = "/api/WebRestoreSearch"
    cp_api_webRestoreSession = "/api/WebRestoreSession"
    cp_api_webRestoreTreeNode = "/api/WebRestoreTreeNode"
    cp_api_webRestoreInfo = "/api/WebRestoreInfo"
    cp_api_ekr = "/api/EKR"
    cp_api_legalHoldMembershipSummary = "/api/LegalHoldMembershipSummary"
    cp_api_legalHoldMembership = "/api/LegalHoldMembership"
    cp_api_legalHoldMembershipDeactivation = "/api/LegalHoldMembershipDeactivation"


    # Overwrite `cp_authorization` to use something other than HTTP-Basic auth.
    cp_authorization = None
    cp_logLevel = "INFO"
    cp_logFileName = "c42SharedLibrary.log"
    MAX_PAGE_NUM = 250
    cp_verify_ssl = False

    # set dates

    cp_todayHMS  = time.strftime("%Y-%m-%d-%H-%M_%S")
    cp_todayHM   = time.strftime("%Y%m%d-%H-%M")
    cp_todayDate = time.strftime("%Y%m%d")

    cp_startTime   = None
    cp_endTime     = None
    cp_elapsedTime = None


    # Check if Python is using an up-to-date version of OpenSSL.  Anything over 1.0 is Good.
    # Using version < 1 will cause SSL errors.  This validator will notify users they need to
    # fix their SSL issues before continuing.

    @staticmethod
    def checkSSLVersion():
        logging.info('[start] - checkSSLVersion')

        sslRaw = ssl.OPENSSL_VERSION

        sslOK = True

        sslVersion = sslRaw[8:13].split(".")

        if sslVersion[0] == "0" or \
          (sslVersion[0] == "1" and \
           sslVersion[2] == "0"):
            sslOK = False

        if sslOK:
            logging.info("SSL Version : " + str(sslRaw) + " is good.")
            print "**********"
            print "********** OpenSSL OK.  Continuing..."
            print "**********"
        else:
            logging.info("SSL Version : " + str(sslRaw) + " is < 1.0.1.  Exiting...")
            print "**********"
            print "********** SSL Version " + str(sslRaw) + " used with Python needs updating to at least 1.0.1.  Exiting."
            print "**********"

        logging.info('[  end] - checkSSLVersion : ' + str(sslRaw))

        return sslOK 


    # startupSharedLibraryValidate
    #
    # Common function to validate the correct shared library is being used.

    @staticmethod
    def startupSharedLibraryValidate(scriptName,scriptVersion,requiredC42Lib,**kwargs):

        logging.debug('[begin] - startupSharedLibraryValidate')

        #c42Lib.cls()

        patchStrict = False
        minorStrict = False
        majorStrict = False

        if kwargs:
            if 'majorStrict' in kwargs:
                majorStrict = kwargs['majorStrict']
            if 'minorStrict' in kwargs:
                minorStrict = kwargs['minorStrict']
            if 'patchStrict' in kwargs:
                patchStrict = kwargs['patchStrict']

        print ""
        print "**********"
        print "********** Starting " + scriptName + " v" + scriptVersion
        print "**********"
        print "********** Using: c42SharedLibrary v" + str(c42Lib.cp_c42Lib_version[0])+"."+str(c42Lib.cp_c42Lib_version[1])+"."+str(c42Lib.cp_c42Lib_version[2])
        print "**********"
        if not c42Lib.validateVersion(version=requiredC42Lib,patchStrict=patchStrict,minorStrict=minorStrict,majorStrict=majorStrict):
            print "This script requires v" + str(requiredC42Lib) + " of the C42SharedLibary.py to run.\nPlease make sure you have the correct version of the shared library."
            print ""
            print "Exiting..."
            print ""
            sys.exit()
        print "********** Shared Library OK.  Continuing..."
        print "**********"
        print ""

        logging.info('  [end] - startupSharedLibraryValidate')

    
    # startupDisclaimer
    #
    # Presents disclaimer language at the top of a script when running it.

    @staticmethod
    def startupDisclaimer(**kwargs):

        logging.debug('[begin] - startupDisclaimer')

        disclaimerFilePath = None

        if kwargs:
            if 'filePath' in kwargs:
                disclaimerFilePath = kwargs['filePath']

        print "" 
        disclaimerFilePath = "../../../Disclaimers/StandardC42Disclaimer2017.txt"
        if not os.path.exists(disclaimerFilePath):
            print 'Copyright 2015,2016,2017,2018 Code42'
            print ''
            print 'THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.'
        else:
            c42Lib.printFileToScreen('../../../Disclaimers/StandardC42Disclaimer2017.txt')
        print ""
        print ""

        logging.info('  [end] - startupDisclaimer')


    # Common function at the beginning of scripts to validate username & server info.
    #
    # Returns true if everything OK, but has built-in exit paths if something doesn't jive.

    @staticmethod
    def startupValidate(arguments,cp_userName,cp_credentialFile,cp_serverHostURL,cp_serverHostPort,cp_serverInfoFileName):

        logging.info('[begin] - startupValidate')

        print "========== User Inputs =========="
        print ""
        print arguments
        print ""
        print "================================="

        if cp_userName:
            userAuth = c42Lib.authenticateUser(cp_userName=cp_userName)  # Sets the variables to authenticate the user.
        elif cp_credentialFile:
            userAuth = c42Lib.authenticateUser(cp_credentialFile=cp_credentialFile)
        else:
            userAuth = c42Lib.authenticateUser() 
        print ""
        print "User Authentication Type: " + str(userAuth)
        print ""
        print "================================="
        print ""
        print "Validating Server Connection"
        print ""
        print "================================="

        if cp_serverHostURL:
            c42Lib.cpServerInfo(cp_serverHostURL=cp_serverHostURL,cp_serverHostPort=cp_serverHostPort)
        elif cp_serverInfoFileName:
            c42Lib.cpServerInfo(cp_serverInfoFileName=cp_serverInfoFileName)
        else:
            c42Lib.cpServerInfo()


        if not c42Lib.validateUserCredentials():
            print ""
            print "=============== Invalid Credentials ================="
            print ""
            print "Please check the credentials and try again."
            print ""
            sys.exit(0)
        else:
            print ""
            print "[ " + str(c42Lib.cp_username) + " ]'s Credentials Appear to Be Valid"
            print ""
            print "====================================================="

            return True

        logging.info('  [end] - startupValidate')

        return False


    #
    # getRequestHeaders:
    # Returns the dictionary object containing headers to pass along with all requests to the API,
    #
    # Params:
    # login_token (kwargs): use login_token
    # auth_token (kwargs): use auth token
    #
    # Uses global / class variables for username and password authentication if 'auth_token' or 'login_token'
    # are not passed in as type
    #
    @staticmethod
    def getRequestHeaders(**kwargs):
        header = {}

        if not c42Lib.cp_authorization:
            if kwargs and 'login_token' in kwargs:
                logging.info("---- headers eval = login_token ----")
                header["Authorization"] = "login_token {0}".format(kwargs['login_token'])
            elif kwargs and 'auth_token' in kwargs:
                logging.info("---- headers eval = auth_token ----")
                header["Authorization"] = "token {0}".format(kwargs['auth_token'])
            else:
                logging.info("---- headers eval = create basic_auth ----")
                header["Authorization"] = c42Lib.getAuthHeader(c42Lib.cp_username,c42Lib.cp_password)
        else:
            logging.info("---- headers eval = use current basic auth ----")
            header['Authorization'] = c42Lib.cp_authorization

        header["Content-Type"] = "application/json"

        # logging.info("-getRequestHeaders: " + str(header))
        return header

    #
    # getRequestUrl(cp_api):
    # Returns the full URL to execute an API call,
    # Params:
    # cp_api: what the context root will be following the host and port (global / class variables)
    # host (kwargs): host address to use when building request url. Uses global / class variables by default
    # port (kwargs): port to use when bulding request url. Uses global / class variables by default
    #
    @staticmethod
    def getRequestUrl(cp_api, **kwargs):
        host = ''
        port = ''

        if kwargs and 'host' in kwargs:
            host = kwargs['host']
        else:
            host = c42Lib.cp_host

        if kwargs and 'port' in kwargs:
            port = str(kwargs['port'])
        else:
            port = c42Lib.cp_port


        if port == '':           # Some customers have port forwarding and adding a port breaks the API calls
            url = host+ cp_api
        else:
            url = host + ":" + str(port) + cp_api

        return url

    #
    # executeRequest(type, cp_api, params, payload):
    # Executes the request to the server based on type of request
    # Params:
    # type: type of rest call: valid inputs: "get|delete|post|put" - returns None if not specified
    # cp_api: the context root to be appended after server:port when generating the URL
    # params: URL parameters to be passed along with the request
    # payload: json object to be sent in the body of the request
    # host (kwargs): host address to target request at. Uses global / class variables by default
    # port (kwargs): port to target request at. Uses global / class variables by default
    # auth_token (kwargs): auth type to use. Uses basic auth with global username and password by default
    # login_token (kwargs): token to use based on auth type. Unused by default.

    # Returns: the response object directly from the call to be parsed by other methods
    #

    @staticmethod
    def executeRequest(type, cp_api, params={}, payload={}, **kwargs):

        requests.packages.urllib3.disable_warnings()
        #logging.getLogger("urllib3").setLevel(logging.warning)
        
        header = c42Lib.getRequestHeaders(**kwargs)
        url = c42Lib.getRequestUrl(cp_api, **kwargs)

        # for our purposes, we always want this set for fileContent requests so that a restore record
        # is not stamped out on the server
        if cp_api == c42Lib.cp_api_fileContent:
            assert 'restoreRecordKey' in params and params['restoreRecordKey'] is cp_magic_restoreRecordKey

        cookies = None
        timeout = None

        if kwargs:
            if 'cookie' in kwargs:
                cookies = kwargs['cookie']
            if 'timeout' in kwargs:
                timeout = kwargs['timeout']

        try:
            if type == "get":
                logging.debug("Payload : " + str(payload))
                r = requests.get(url, params=params, data=json.dumps(payload), headers=header, verify=c42Lib.cp_verify_ssl,cookies=cookies,timeout=timeout)
                logging.debug(r.text)
                return r
            elif type == "delete":
                r = requests.delete(url, params=params, data=json.dumps(payload), headers=header, verify=c42Lib.cp_verify_ssl)
                logging.debug(r.text)
                return r
            elif type == "post":
                r = requests.post(url, params=params, data=json.dumps(payload), headers=header, verify=c42Lib.cp_verify_ssl)
                logging.debug(r.text)
                return r
            elif type == "put":
                r = requests.put(url, params=params, data=json.dumps(payload), headers=header, verify=c42Lib.cp_verify_ssl)
                logging.debug(r.text)
                return r
            else:
                return None
        except requests.exceptions.RequestException as e:
            return e


    #
    # getRequestHeaders:
    # Returns the dictionary object containing headers to pass along with all requests to the API,
    # Params: None
    # Uses global / class variables for username and password authentication
    #
    @staticmethod
    def getGenericRequestHeaders(username,password):
        header = {}
        header["Authorization"] = c42Lib.getAuthHeader(username,password)
        header["Content-Type"] = "application/json"

        # print header
        return header

    #
    # getRequestUrl(cp_api):
    # Returns the full URL to execute an API call,
    # Params:
    # cp_api: what the context root will be following the host and port (global / class variables)
    #

    @staticmethod
    def getGenericRequestUrl(url,port,apiCall):
        if port  == '':           # Some customers have port forwarding and adding a port breaks the API calls
            url = url + apiCall
        else: 
            url = url + ":" + str(port) + apiCall

        return url

    #
    # executeRequest(type, cp_api, params, payload):
    # Executes the request to the server based on type of request
    # Params:
    # type: type of rest call: valid inputs: "get|delete|post|put" - returns None if not specified
    # cp_api: the context root to be appended after server:port when generating the URL
    # params: URL parameters to be passed along with the request
    # payload: json object to be sent in the body of the request
    # Returns: the response object directly from the call to be parsed by other methods
    #

    @staticmethod
    def executeGenericRequest( username, password, type, api_URL, api_Port, apiCall ,params, payload):
        # logging.debug
        header = c42Lib.getGenericRequestHeaders(username,password)
        # print header
        url = c42Lib.getGenericRequestUrl(api_URL,api_Port,apiCall)
        # url = cp_host + ":" + cp_port + cp_api
        # payload = cp_payload
        #print url
        #raw_input()
        if type == "get":
            logging.debug("Payload : " + str(payload))
            r = requests.get(url, params=params, data=json.dumps(payload), headers=header, verify=False)
            #print r.text
            #raw_input()
            logging.debug(r.text)
            return r
        elif type == "delete":
            r = requests.delete(url, params=params, data=json.dumps(payload), headers=header, verify=False)
            logging.debug(r.text)
            return r
        elif type == "post":
            r = requests.post(url, params=params, data=json.dumps(payload), headers=header, verify=False)
            logging.debug(r.text)
            return r
        elif type == "put":
            # logging.debug(str(json.dumps(payload)))
            r = requests.put(url, params=params, data=json.dumps(payload), headers=header, verify=False)
            logging.debug(r.text)
            return r
        else:
            return None

        # content = r.content
        # binary = json.loads(content)
        # logging.debug(binary)


    # Validates User Credentials by trying to look up the user's own info based on their username.deviceList = c42Lib.getDevicesCustomParams(currentPage,params)

    @staticmethod
    def validateUserCredentials():

        logging.debug ("=========== Validate User")

        # Check if username/password combination is valid

        isValidUser = False

        params = {}
        params['username'] = c42Lib.cp_username

        getUserInfo = c42Lib.getUser(params)

        if getUserInfo is not None:
            isValidUser = True

        return isValidUser

    #
    # KWARGS: cp_enterUserName - manually entered username & password,cp_userName - hardcoded username ,cp_useCustomerCredFile - use credentials file ,cp_credentialFile - name of credentials file
    # Returns: True once authentication parameters are entered.  Does not verify these are valid for the script.
    #
    @staticmethod
    def authenticateUser(**kwargs):

        logging.debug ("=========== Authenticate User")

        cp_enterUserName = False
        cp_useCustomerCredFile = False
        userInfoSet = False
        warningText = False
        userAuthType = 'Hardcoded'

        if not kwargs:
            kwargs = False

        if kwargs:
            
            # If no KWARGS it will use hardcoded values.
            
            if ('cp_userName' in kwargs):
                print "Entered Username..."
                c42Lib.cp_username = kwargs['cp_userName']
                cp_username = kwargs['cp_userName']
                cp_enterUserName = True
                userAuthType = 'Manually Entered'
                warningText = ''
            else:
                print "Did not enter username..."
                cp_enterUserName = False
                warningText = 'Check Entered userName'
                # cp_userName = c42Lib.cp_username

            if ('cp_credentialFile' in kwargs):
                print "Using credentials file..."
                cp_credentialFile = kwargs['cp_credentialFile']
                cp_useCustomerCredFile = True
            else:
                warningText = ''

        # end if

        if cp_useCustomerCredFile: # If using a credentials file

            print "Looking for credentials file..."
            
            with open(str(c42Lib.getFilePath(cp_credentialFile))) as f:
                c42Lib.cp_username = base64.b64decode(f.readline().strip())
                cp_username        = c42Lib.cp_username
                c42Lib.cp_password = base64.b64decode(f.readline().strip())


            userAuthType = 'Credentials File'
            userInfoSet = True

        if cp_enterUserName and userAuthType != 'Hardcoded':

            print ""
            c42Lib.cp_password = getpass.getpass('=========== Please enter the password for user ' + str(c42Lib.cp_username) + ' : ')

            userAuthType = 'Entered Password'
            userInfoSet= True

        if userAuthType == 'Hardcoded':

            if cp_username == 'admin':
                print ""
                print "Username is set to 'admin'!  If this is really your username you should change it."
                print ""
                raw_input("Please press 'Enter' to proceed.")
                print ""

            else:
                print "Username has been hardcoded to : " + c42Lib.cp_username

            if c42Lib.cp_password == 'admin':
                print ""
                print "Username is set to 'admin'!  If this is really your password you should change it."
                print ""
                raw_input("Please press 'Enter' to proceed.")
                print ""
            else:
                print "Password has been hardcoded.  Not shown."

            userInfoSet = True
            
        if warningText != '' and not userInfoSet:
            print ""
            print "**********"
            print "********** " + warningText
            print "**********"
            print ""

        if userInfoSet:
            return userAuthType
        else:
            return userInfoSet


    #
    # Params: cp_serverInfoFile,cp_serverInfoFileName,cp_serverEntryFlag,cp_serverHostURL,cp_serverHostPort
    # Returns: True once authentication parameters are entered.  Does not verify these are valid for the script.
    #
    @staticmethod
    def cpServerInfo(**kwargs):

        logging.debug ("=========== Set CP Server Info")

        print ""
        print "========= Checking Connection to Server..."
        print ""

        serverInfoType     = 'Hardcoded'
        warningText        = ''
        cp_serverInfoFile  = False
        cp_serverEntryFlag = False 

        if kwargs:
            
            # If no KWARGS it will use 'admin'/'admin' and proceed.
            
            if ('cp_serverHostURL' in kwargs) and ('cp_serverHostPort' in kwargs):
                cp_serverHostURL  = kwargs['cp_serverHostURL']
                cp_serverHostPort = kwargs['cp_serverHostPort']
                cp_serverEntryFlag = True
            else:
                cp_serverEntryFlag = False
                warningText = 'Check Server URL & Port (no colon between URL & port)'
                cp_serverHostURL  = c42Lib.cp_host
                cp_serverHostPort = c42Lib.cp_port

            if ('cp_serverInfoFileName' in kwargs) and not cp_serverEntryFlag:
                cp_serverInfoFileName = kwargs['cp_serverInfoFileName']
                cp_serverInfoFile = True
            elif not cp_serverEntryFlag:
                cp_serverInfoFile = False
                warningText = 'Check Server File Info'
                cp_serverInfoFileName = ''

        # end if

        if cp_serverInfoFile: # If using a credentials file
            
            with open(str(c42Lib.getFilePath(cp_serverInfoFileName))) as f:
                c42Lib.cp_host = f.readline().strip()
                c42Lib.cp_port = f.readline().strip()

            serverInfoType = 'Server Info File'

        if cp_serverEntryFlag:

            print ""
            c42Lib.cp_host = cp_serverHostURL
            c42Lib.cp_port = cp_serverHostPort

            serverInfoType = 'Manually Entered'

        canConnect = False
        canConnect = c42Lib.reachableNetworkTest(c42Lib.cp_host)

        if not canConnect:
            serverInfoType = False
            warningText = 'Connection to ' + str(c42Lib.cp_host)+":"+str(c42Lib.cp_port)+" Failed."

        if warningText != '' and not serverInfoType:
            print ""
            print "**********"
            print "********** " + warningText
            print "**********"
            print ""
            sys.exit(1)

        print ""
        print "========= Server Connection Check Complete"
        print ""

        return serverInfoType


    #
    # Params:
    # private address: address to check if reachbale
    # Returns: Check if address is reachable. None on failure
    # Takes at least 1 parameter:  URL to ping with port (example:  https://server.com:4285 )
    #
    @staticmethod
    def URLPing(private_address,**kwargs):

        if kwargs:
            if 'timeout' in kwargs:
                timeout = kwargs['timeout']
        else:
            timeout = 5 # 5 Seconds

        # print "Timeout : " + str(timeout)

        private_address = private_address + "/api/Ping"

        try:
            # print "Trying : " + str(private_address)
            r = requests.get(private_address, params={}, data={}, headers={}, verify=c42Lib.cp_verify_ssl,timeout=kwargs['timeout'])
            contents = r.content.decode("UTF-8")
            binary = json.loads(contents)
            return True if 'data' in binary else None
        except requests.exceptions.ConnectionError as e:
            return False

    #
    # Params:
    # private address: address to check if reachbale
    # Returns: Check if address is reachable. None on failure
    #
    @staticmethod
    def reachableNetworkTest(private_address, **kwargs):

        print ""
        print "Testing Connection to " + str(private_address)
        print ""

        connectionGood = False

        # strip off http or https if testing connectivity to URL that's more than a ping.
        if private_address[:5] == "https":
            private_address = private_address[8:]
        if private_address[:4] == "http":
            private_address = private_address[7:]

        payload = {
            "testType":"reachable",
            "address":private_address,
            "privateAddress":True
        }

        r = c42Lib.executeRequest("post", c42Lib.cp_api_networkTest, {}, payload, **kwargs)

        try:
            contents = r.content.decode("UTF-8")
            binary = json.loads(contents)
            binary['data'] if 'data' in binary else None

            print ""
            print "Connection to " + str(private_address) + " appears to be valid."
            print ""

            return binary

        except AttributeError:

            print ""
            print "Connection to " + str(private_address) + " does not appear to be valid."
            print ""

            return False


    # params:
    # 
    @staticmethod
    def requestLoginToken(**kwargs):
        logging.info("[begin] requestLoginToken: " + str(kwargs))
        payload = {}

        loginToken = None

        if kwargs and ('userId' in kwargs) and ('sourceGuid' in kwargs) and ('destinationGuid' in kwargs):
            payload['userId'] = str(kwargs['userId'])
            payload['sourceGuid'] = str(kwargs['sourceGuid'])
            payload['destinationGuid'] = str(kwargs['destinationGuid'])
        else:
            logging.info("Insufficient Parameters Passed in : " + str(kwargs))
            return None
        
        try:

            r = c42Lib.executeRequest("post", c42Lib.cp_api_loginToken, {}, payload, **kwargs)

            logging.info("Status Code : " + str(r.status_code))
            contents = r.content.decode("UTF-8")
            binary = json.loads(contents)
            logging.info("requestLoginToken Response: " + str(contents))

            if 'data' in binary:
                loginToken = binary['data']

        except Exception, e:

            logging.info("Error Login Token : " + str(e))
            logging.info("      Status Code : " + str(r.status_code))

        logging.info("[  end] requestLoginToken: " + str(loginToken))

        return loginToken

    #
    # Params:
    # host (kwargs): host location to use
    # port (kwargs): port to use
    # login_token (kwargs): necessary for storage nodes
    # Returns: Auth token. None on failure
    #
    @staticmethod
    def requestAuthToken(**kwargs):
        logging.info("^^^^^^^^^^^ requestAuthToken: start" + str(kwargs))

        if kwargs:
            if 'serverUrl' in kwargs:
                serverURL = kwargs['serverUrl'] + "/api/AuthToken"
            else:
                serverURL = c42Lib.cp_api_authToken 
            if 'header' in kwargs:
                header = kwargs['header']

        payload = {
            "sendCookieHeader":True
        }
        r = c42Lib.executeRequest("post", c42Lib.cp_api_authToken, {}, payload, **kwargs)
        if r.status_code != 200:
            logging.debug("Failed to get auth token")
            return None

        logging.info("requestAuthToken Response: " + r.content)
        return "-".join(json.loads(r.content.decode("UTF-8"))['data'])

    #
    # Params:
    # computer_Guid: guid to get datakey for
    # host (kwargs): host location to use
    # port (kwargs): port to use
    # auth_token (kwargs): auth_token to use
    # Returns: Datakey. None on failure
    #
    @staticmethod
    def getDataKeyToken(computerGuid, **kwargs):
        logging.info("[begin] getDataKeyToken : " + str(computerGuid))
        if kwargs:
            logging.info("                 kwargs : " + str(kwargs))

        params = {}
        payload = {'computerGuid': computerGuid}

        dataKeyToken = None

        try:
            r = c42Lib.executeRequest("post", c42Lib.cp_api_dataKeyToken, params, payload, **kwargs)
            logging.info("Data Key Token Response : " + str(r.status_code))
            logging.info("Data Key Token          : " + str(r.content))

        except Exception, e:

            logging.info("Error Getting DataKeyToken : " + str(e))
            return False

        if r.status_code != 200:
            logging.info("Returned Bad Status Code : " + str(r.status_code))
            return False
        else: 
            binary = json.loads(r.content.decode('UTF-8'))
            if 'data' in binary:
                logging.info("Successfully Retreived DataKeyToken : " + str(binary['data']['dataKeyToken']))
                dataKeyToken = binary['data']['dataKeyToken']
            else:
                logging.debug("No Data in returned result : " + str(binary))
                return 

        logging.info("[end] getDataKeyToken")
        return dataKeyToken

    #
    # Params:
    # computer_Guid: guid to start a session for
    # datakeytoken: data key token to use
    # host (kwargs): host location to use
    # port (kwargs): port to use
    # auth_token (kwargs): auth_token to use
    # Returns: Session information. None on failure
    #
    @staticmethod
    def startWebRestoreSession(computerGuid, dataKeyToken, **kwargs):
        payload = {
            "computerGuid":computerGuid,
            "dataKeyToken":dataKeyToken
        }
        r = c42Lib.executeRequest("post", c42Lib.cp_api_webRestoreSession, {}, payload, **kwargs)
        if r.status_code != 200:
            logging.debug("Failed to get web restore session")

            return None

        return json.loads(r.content.decode("UTF-8"))['data']

    #
    # Params:
    # session_id: sessionId to use for search
    # guid: guid to use for search
    # timestamp: timestamp to use for search
    # regex: regex to search for
    # host (kwargs): host location to use
    # port (kwargs): port to use
    # auth_token (kwargs): auth_token to use
    # Returns: Search results. None on failure
    #
    @staticmethod
    def requestWebRestoreSearch(session_id, guid, timestamp, regex, **kwargs):
        params = {}
        params['webRestoreSessionId'] = session_id
        params['guid'] = guid
        params['timestamp'] = timestamp
        params['regex'] = regex
        payload = {}
        r = c42Lib.executeRequest("get", c42Lib.cp_api_webRestoreSearch, params, payload, **kwargs)

        print r

        binary = json.loads(r.content.decode('UTF-8'))
        return binary['data'] if 'data' in binary else None


    #
    # Params:
    # srcGuid: guid of the device
    # destGuid: guid of the destination
    # Returns: Web Restore Job Info
    #
    @staticmethod
    def requestWebRestoreInfo(srcGuid,destGuid):
        params = {}
        params['srcGuid'] = srcGuid
        params['destGuid'] = destGuid
        payload = {}
        r = c42Lib.executeRequest("get", c42Lib.cp_api_webRestoreInfo, params, payload)
        binary = json.loads(r.content.decode('UTF-8'))
        return binary['data'] if 'data' in binary else None


    # params (guid)
    # returns: true / false / none based on computer online status according to master
    @staticmethod
    def getComputerOnlineStatus(client_guid):
        params = {}
        payload = {}
        try:
            r = c42Lib.executeRequest("get", c42Lib.cp_api_computerActivity+"/"+str(client_guid), params, payload)
            binary = json.loads(r.content.decode('UTF-8'))
            return binary['data']['clientConnected'] if 'data' in binary else False
        except Exception, e:
            logging.info("Error Returning Push Restore Job : " + str(e))
            print "********** Error With Push Restore Job"
            print "           " + str(e)
            return None


    #
    # Params:
    #
    #   
    #
    #
    @staticmethod
    def pushRestoreJob(webRestoreSessionId,sourceComputerGuid,pathSet,backupServerGuid,acceptingComputerGuid,restorePath, **kwargs):
        restoreDateEpochMS = int(round(time.time() * 1000))
        payload = {}
        payload["webRestoreSessionId"] = webRestoreSessionId
        payload["sourceGuid"] = str(sourceComputerGuid)
        payload["targetNodeGuid"] = str(backupServerGuid)
        payload["acceptingGuid"] = str(acceptingComputerGuid)
        payload["restorePath"] = restorePath
        payload["pathSet"] = pathSet
        payload["numBytes"] = 1
        payload["numFiles"] = 1
        if kwargs and 'showDeleted' in kwargs:
            payload["showDeleted"] = kwargs["showDeleted"]
        else:
            payload["showDeleted"] = True
        if kwargs and 'restoreFullPath' in kwargs:
            payload["restoreFullPath"] = kwargs["restoreFullPath"]
        else:
            payload["restoreFullPath"] = True
        payload["timestamp"] = restoreDateEpochMS

        logging.debug(payload)

        #post
        try:
            r = c42Lib.executeRequest("post", c42Lib.cp_api_pushRestoreJob, {}, payload)
            
            print r
            return json.loads(r.content.decode("UTF-8"))['data']
        except Exception, e:
            logging.info("Error Returning Push Restore Job : " + str(e))
            print "********** Error With Push Restore Job"
            print "           " + str(e)

            return None

    #
    # Params:
    # planUid: plan to get auth token for
    # destinationGuid: destination to get auth token for
    # Returns: Storage auth token on success, None on failure
    #
    @staticmethod
    def requestStorageAuthToken(planUid, destinationGuid, **kwargs):
        payload = {
            "planUid":planUid,
            "destinationGuid":destinationGuid
        }

        r = c42Lib.executeRequest("post", c42Lib.cp_api_storageAuthToken, {}, payload, **kwargs)
        if r.status_code != 200:
            logging.debug("Failed to get storage auth token")
            return None

        return json.loads(r.content.decode("UTF-8"))['data']


    #
    # Params:
    # planUid: planUid to download from
    # filepath: path to download
    # host (kwargs): host location to use
    # port (kwargs): port to use
    # auth_token (kwargs): auth_token to use
    # Returns: File content. None on failure
    #
    @staticmethod
    def getFileContentByFilePath(planUid, filepath, **kwargs):
        params = {}
        params['path'] = filepath
        params['restoreRecordKey'] = c42Lib.cp_magic_restoreRecordKey
        params['zipFolderContents'] = True
        r = c42Lib.executeRequest("get", c42Lib.cp_api_fileContent + "/" + planUid, params, {}, **kwargs)
        if r.status_code != 200:
            return None
        return r.content


    #
    # Params:
    # planUid: planUid to metadata from
    # filepath: path to get metadata for
    # host (kwargs): host location to use
    # port (kwargs): port to use
    # auth_token (kwargs): auth_token to use
    # Returns: File content. None on failure
    #
    @staticmethod
    def getFileMetadataByFilePath(planUid, filepath, **kwargs):
        params = {}
        params['path'] = filepath
        r = c42Lib.executeRequest("get", c42Lib.cp_api_fileMetadata + "/" + planUid, params, {}, **kwargs)
        if r.status_code != 200:
            return None
        return r.content


    #
    # Params:
    # planUid: planUid to download from
    # fileid: fileId to download
    # host (kwargs): host location to use
    # port (kwargs): port to use
    # auth_token (kwargs): auth_token to use
    # Returns: File content. None on failure
    #
    @staticmethod
    def getFileContentByFileId(planUid, file_id, **kwargs):
        params = {}
        params['restoreRecordKey'] = c42Lib.cp_magic_restoreRecordKey
        params['zipFolderContents'] = True
        r = c42Lib.executeRequest("get", c42Lib.cp_api_fileContent + "/" + planUid + "/" + file_id, params, {}, **kwargs)
        if r.status_code != 200:
            return None
        return r.content

         #
    # Params:
    # planUid: planUid to metadata from
    # fileid: fileId to get metadata for
    # host (kwargs): host location to use
    # port (kwargs): port to use
    # auth_token (kwargs): auth_token to use
    # Returns: File content. None on failure
    #
    @staticmethod
    def getFileMetadataByFileId(planUid, file_id, **kwargs):
        r = c42Lib.executeRequest("get", c42Lib.cp_api_fileMetadata + "/" + planUid + "/" + file_id, {}, {}, **kwargs)
        binary = json.loads(r.content.decode("UTF-8"))
        if 'data' in binary:
            return binary['data']
        else:
            return None




    #
    # Params:
    # sourceComputerGuid: guid to get backup plans for
    # host (kwargs): host location to use
    # port (kwargs): port to use
    # auth_token (kwargs): auth_token to use
    # Returns: Backup plans for guid located at host:port. None on failure
    #
    @staticmethod
    def getBackupPlans(sourceComputerGUID, **kwargs):
        params = {
            "sourceComputerGuid":sourceComputerGUID,
            "planTypes":"BACKUP"
        }
        r = c42Lib.executeRequest("get", c42Lib.cp_api_plan, params, {}, **kwargs)
        binary = json.loads(r.content.decode("UTF-8"))
        if 'data' in binary:
            return binary['data']
        else:
            return None

    #
    #  Params:
    #  planUid: planUid to get storage information about
    #  Returns: storage information based on passed in planUid or None on failure
    #
    @staticmethod
    def getStorageInformationByPlanUid(planUid, **kwargs):
        r = c42Lib.executeRequest("get", c42Lib.cp_api_storage +"/"+planUid, {}, {}, **kwargs)
        binary = json.loads(r.content.decode("UTF-8"))
        if 'data' in binary:
            return binary['data']
        else:
            return None

    #
    #  Returns: license information.  
    #  No parameters required but it is up the user to make sure
    #  its known which version of the API is being used
    #  The argument 'countsOnly=True' will work for both API calls
    #  to return just the current backup seats used.
    #
    @staticmethod
    def getLicenseInfo(**kwargs):
        logging.info("[start] getLicenseInfo")

        if kwargs:
            logging.info("        getLicneseInfo - kwargs : " + str(kwargs))

        # Get the sever version so the right call can be made
        # This is a courtesy to all those running < 6.0

        logging.info("Getting server info to obtain Code42 version...")

        serverInfo = c42Lib.getServer(0,this=True) # Gets the master server's sever info.

        logging.info("Server Info : " + str(serverInfo))

        licenseInfo = None
        newAPI      = True

        params = {}
        payload = {}

        r = None

        if serverInfo:
            serverVersion = serverInfo['version']
            print "           Server Version : " + str(serverVersion)

        else:
            logging.info("getLicenseInfo - no server version info returned.")
            return licenseInfo


        try:

            #print "Figuring out which method..."

            if int(serverVersion[:1]) > 5: # Use the new, unsupported API
                logging.info("getLicenseInfo - Use new, unsupported license API")
                logging.info("           Getting Auth Cookie")
                JWTAuthCookie = c42Lib.getJWTAuth()

                r = c42Lib.executeRequest("get", c42Lib.cp_api_customerLicense,{},{},cookie=JWTAuthCookie)

                if r.status_code == 200:
                    logging.info("           Auth Cookie Retrieved")

            if r is None or int(serverVersion[:1]) < 6:
                # Use the old masterLicense API
                logging.info("getLicenseInfo - Using masterLicense API")           
                r = c42Lib.executeRequest("get", c42Lib.cp_api_masterLicense,params,payload)

                newAPI = False
  
            content = r.content

            content = r.content.decode("UTF-8")
            binary = json.loads(content)

            licenseInfo = binary['data']

        except Exception, e:

            print "********** Error Will Robinson!  Error : " + str(e)

            logging.info("getLicenseInfo - Error : " + str(e))
            #print "Will return 'None'."
            return licenseInfo

        if kwargs:
            if 'countsOnly' in kwargs:
                if newAPI:
                    licenseInfo = licenseInfo['backupSeatsInUse']
                else:
                    licenseInfo = licenseInfo['seatsInUse']

        return licenseInfo

    #
    #  Returns: destinations know by server or None on failure
    #
    @staticmethod
    def getDestinations(**kwargs):
        logging.info("getDestinations")
        r = c42Lib.executeRequest("get", c42Lib.cp_api_destination, {}, {}, **kwargs)
        logging.debug(r.text)
        content = r.content.decode("UTF-8")
        binary = json.loads(content)
        return binary['data']['destinations'] if 'data' in binary else None

    #
    #  Returns: destination know by server or None on failure
    #
    @staticmethod
    def getDestinationById(id, **kwargs):
        logging.info("getDestinationById")

        if not kwargs:
            params = {}
        else:
            params = kwargs['params']
            kwargs = {}

        r = c42Lib.executeRequest("get", c42Lib.cp_api_destination + "/" + str(id), params, {}, **kwargs)
        logging.debug(r.text)
        content = r.content.decode("UTF-8")
        binary = json.loads(content)
        return binary['data'] if 'data' in binary else None



    # getServersByDestinationId(destinationId, **kwargs):
    # returns the servers in a given destination
    # Note that the API uses 'nodeId' for serverId
    # params:
    # destinationId: id of destination
    #

    @staticmethod
    def getServersByDestinationId(destinationId, **kwargs):
        logging.info("getServers({0})".format(destinationId))

        params = {}

        if kwargs and 'params' in kwargs:
                params = kwargs['params']

        params['destinationId'] = destinationId

        r = c42Lib.executeRequest("get", c42Lib.cp_api_server, params, {}, **kwargs)
        logging.debug(r.text)
        content = r.content.decode("UTF-8")
        binary = json.loads(content)
        return binary['data']['servers'] if 'data' in binary else None



    # getStorePointsByServerId(severId):
    # returns the storpoints on a given server
    # Note that the API uses 'nodeId' for serverId
    # params:
    # storePointId: id of storePoint
    #

    @staticmethod
    def getStorePointsByServerId(serverId):
        logging.info("getStorePointsByServerId-params:serverId[" + str(serverId) + "]")


        storePoint = ""
        params = {}
        payload = {}
        params['nodeId'] = serverId

        r = c42Lib.executeRequest("get", c42Lib.cp_api_storePoint, params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        storePoint = binary['data']

        return storePoint if 'data' in binary else None

    @staticmethod
    def getUser(params):
        logging.info("getUser-params:params[" + str(params) + "]")

        user = None

        if params:
            payload = {}

            keepTrying = True
            keepTryingCount = 0

            while keepTrying:

                keepTryingCount += 1

                if keepTryingCount < 4:

                    
                    try:
                        r = c42Lib.executeRequest("get", c42Lib.cp_api_user, params, payload)

                        logging.debug(r.text)
                        content = r.content
                        r.content
                        binary = json.loads(content)

                        logging.debug(binary)

                    except Exception, e:

                        logging.info("Error getting user : " + str(e))
                        print "********** " + str(keepTryingCount) + " | Error getting user : " + str(e)
                        break

                    if r.status_code == 200:

                        try:
                            return binary['data']['users']
                            keepTrying = False

                        except TypeError:

                            print str(keepTryingCount) + " | Error Code : " + str(r.status_code) + " | TypeError"
                            
                            logging.info("getUser-failed : " + r.status_code)
                            sys.exit()

                        except Exception, e:
                            print str(keepTryingCount) + " | Error : " + str(e)
                            
                            logging.info("getUser-failed : " + e)
                            return None
                    
                    else:
                    
                        print str(keepTryingCount) + " | Error Code : " + str(r.status_code)

                        if keepTryingCount == 4:

                            return None
                else:
                    print str(keepTryingCount) + " | Error Code : " + str(r.status_code)
                    keepTrying = False
                    return None
        



#
    # getUserById(userId):
    # returns the user json object of the requested userId
    # params:
    # userId: the id of the user within the system's database
    #
    @staticmethod
    def getUserById(userId,**kwargs):
        logging.info("getUser-params:userId[" + str(userId) + "]")

        params = {}
        if kwargs:
            params = kwargs
        else:
            params['incAll'] = 'true'
            params['idType'] = 'uid' # Needed for the 4.x series and beyond

        payload = {}

        logging.debug("cp_api_user/" + str(userId)+"/"+str(params)+" [payload] : " + str(payload))
        r = c42Lib.executeRequest("get", c42Lib.cp_api_user + "/" + str(userId), params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        try:
            logging.debug("[data] : " + str(binary['data']))
            user = binary['data']
        except TypeError:

            logging.info("There was an error getting the user [ " + str(userId) + " ] ")
            logging.info("This is the returned response : ")
            logging.info( binary )

            user = False

        return binary

    @staticmethod
    def getUserByMy():
        logging.info("getUserByMy")

        r = c42Lib.executeRequest("get", c42Lib.cp_api_user + "/my", {}, {})

        logging.debug(r.text)
        content = r.content.decode("UTF-8")
        binary = json.loads(content)
        return binary['data'] if 'data' in binary else None
    #
    # getUserByUserName(username):
    # returns the user json object of the requested username
    # params:
    # username: the username of the user within the system's database
    #
    @staticmethod
    def getUserByUserName(username):
        logging.info("getUser-params:username[" + str(username) + "]")

        params = {}
        params['username'] = username
        params['incAll'] = 'true'
        payload = {}

        user = None

        try:

            r = c42Lib.executeRequest("get", c42Lib.cp_api_user, params, payload)

        except Exception, e:

            logging.info("getUserByUserName - Error. " + str(username) + " | Error : " + str(e))
            print "Error getting archive: " + str(username)
            print "Error : " + str(e)
            print "Will return 'None'."

        logging.debug(r.text)

        content = r.content

        r.content

        binary = json.loads(content)
        logging.debug(binary)

        user = binary['data']

        binary_length = binary['data']['totalCount'] # Gets the number of users results returned

        if binary_length > 0:

            user = binary['data']['users'][0] # Returns the user info

        else:

            user = None # Returns null if nothing

        return user

    @staticmethod
    def getRestoreRecordByRestoreJobID(restoreId):
        r = c42Lib.executeRequest("get", c42Lib.cp_api_restoreRecord + "/" + str(restoreId), {}, {})
        content = r.content.decode("UTF-8")
        binary = json.loads(content)
        return binary

    #
    # getUsersByOrgPaged
    # Returns a list of active users within an orgization by page,
    # Params:
    # orgId - integer, that is used to limit the users to an org. Can be set to 0 to return all users.
    # pgNum - page request for user list (starting with 1)
    #
    @staticmethod
    def getUsersByOrgPaged(orgId, pgNum):
        logging.info("getUsersByOrgPaged-params:orgId[" + str(orgId) + "]:pgNum[" + str(pgNum) + "]")

        # headers = {"Authorization":getAuthHeader(cp_username,cp_password)}
        # url = cp_host + ":" + cp_port + cp_api_user
        params = {}
        params['orgId']        = orgId
        params['pgNum']        = str(pgNum)
        params['pgSize']       = str(c42Lib.MAX_PAGE_NUM)
        params['active']       = 'true'
        params['incChildOrgs'] = 'false'

        payload = {}
        logging.info(str(payload))
        # r = requests.get(url, params=payload, headers=headers)
        r = c42Lib.executeRequest("get", c42Lib.cp_api_user, params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)


        users = binary['data']['users']
        return users

    #
    # getUsersPaged(pageNum):
    # Returns list of active users within the system based on page number
    # params:
    # pgNum - page request for user list (starting with 1)
    #
    @staticmethod
    def getUsersPaged(pgNum,**kwargs):
        logging.info("getUsersPaged-params:pgNum[" + str(pgNum) + "]")

        params = {}
        users = None

        if kwargs:
            if 'params' in kwargs:
                params = kwargs['params'] 
                if 'pgSize' not in params: params['pgSize'] = str(c42Lib.MAX_PAGE_NUM)
        
        params['pgNum'] = pgNum

        payload = {}

        # r = requests.get(url, params=payload, headers=headers)
        try:
            r = c42Lib.executeRequest("get", c42Lib.cp_api_user, params, payload)

            logging.debug(r.text)

            content = r.content.decode('UTF-8')
            binary = json.loads(content)
            logging.debug(binary)

            users = binary['data']['users']
        
        except Exception, e:

            logging.info("Error Getting Users : " + str(e))

            users = False
        
        return users

    @staticmethod
    def getAllUsers(**kwargs):
        logging.info("getAllUsers")
        currentPage = 1
        keepLooping = True
        fullList = []

        params = {}

        if kwargs:
            if 'params' in kwargs:
                params = kwargs['params']
                if 'pgSize' in params:
                    pgSize = params['pgSize']

        while keepLooping:
            pagedList = c42Lib.getUsersPaged(currentPage,params=params)
            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False

            currentPage += 1
        return fullList


# getUsersReturnList
# this is an "all-purpose" method to get users.
# Pass in a file name with usernames and it will read the file and get the usersnames
# Get users by Org - pass in an org Uid or Id and it'll get the users in that org
# Or, just get all the users.



# getAllUsersActiveBackup():
# returns AllUser info + backup usage for active users
# - Jack Phinney

    @staticmethod
    def getAllUsersActiveBackup():
        logging.info("getAllUsersActiveBackup")
        currentPage = 1
        keepLooping = True
        fullList = []
        params={}
        params['incBackupUsage'] = True
        params['active'] = True
        while keepLooping:
            pagedList = c42Lib.getUsersPaged(currentPage,params)
            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList


    @staticmethod
    def generaticLoopUntilEmpty():
        currentPage = 1
        keepLooping = True
        fullList = []
        while keepLooping:
            # pagedList = c42Lib.getUsersPaged(currentPage)
            pagedList = c42Lib.getDevices(currentPage)
            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList


    @staticmethod
    def getAllUsersByOrg(orgId):
        logging.info("getAllUsersByOrg-params:orgId[" + str(orgId) + "]")
        currentPage = 1
        keepLooping = True
        fullList = []
        while keepLooping:
            pagedList = c42Lib.getUsersByOrgPaged(orgId, currentPage)
            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList

    #
    # putUserUpdate(userId, idType payload):
    # updates a users information based on the payload passed
    # params:
    # userId - id for the user to update
    # idType - to specify idType for 4.2+ (uid is now the standard)
    # payload - json object containing name / value pairs for values to update
    # returns: user object after the update
    #

    @staticmethod
    def putUserUpdate(userId, idType, payload):
        logging.info("putUserUpdate-params:userId[" + str(userId) + "],payload[" + str(payload) + "]")

        if (payload is not None and payload != ""):
            params = {}
            params['idType'] = idType

            r = c42Lib.executeRequest("put", c42Lib.cp_api_user + "/" + str(userId), params, payload)
            logging.debug(str(r.status_code))
            content = r.content
            binary = json.loads(content)
            logging.debug(binary)
            user = binary['data']
            return user
            # if (r.status_code == 200):
                # return True
            # else:
                # return False
        else:
            logging.error("putUserUpdate param payload is null or empty")


    #
    # putUserDeactivate(userId, reactive):
    # Deactivates a user based in the userId passed
    # params:
    # userId - id for the user to update
    # deactivate - deactivates the user if true, re-activates if false
    # returns: user object after the update
    #

    @staticmethod
    def putUserDeactivate(userId, deactivate):
        logging.info("putUserDeactivate-params:userId[" + str(userId) + "],deactivate[" + str(deactivate) + "]")
        params = {}
        payload = {}
        if (userId is not None and userId != ""):
            if deactivate:
                r = c42Lib.executeRequest("put", c42Lib.cp_api_deactivateUser+"/"+str(userId), params, payload)
                logging.debug('Deactivate Call Status: '+str(r.status_code))
                if not (r.status_code == ""):
                    return True
                else:
                    return False
            else:
                r = c42Lib.executeRequest("delete", c42Lib.cp_api_deactivateUser+"/"+str(userId), params, payload)
                logging.debug('Deactivate Call Status: '+str(r.status_code))
                if not (r.status_code == ""):
                    return True
                else:
                    return False
        else:
            logging.error("putUserDeactivate has no userID to act on")


    #
    # postUserMoveProcess(userUid, orgUid):
    # posts request to move use into specified organization
    # params:
    # userUid - Uid of the user for the move request
    # orgUid - Uid of destination org for the user
    # returns: true if 204, respose object if 500, else false
    #
    # Changed from ids to uids in 4.3+

    @staticmethod
    def postUserMoveProcess(userUid, orgUid):
        logging.info("postUserMoveProcess-params:userUid[" + str(userUid) + "],orgUid[" + str(orgUid) + "]")

        params = {}
        payload = {}
        payload["userId"] = userUid
        payload["parentOrgId"] = orgUid

        r = c42Lib.executeRequest("post", c42Lib.cp_api_userMoveProcess, params, payload)
        logging.debug(r.status_code)

        if (r.status_code == 204):
            return True
        elif (r.status_code == 500):
            content = r.content
            binary = json.loads(content)
            logging.debug(binary)
            return False
        else:
            return False


    #
    # createOrg(newOrgInfo):
    # Creates a new orginization based on the information passed
    # params:
    # parentOrgId - id of the parent organization.  Will default to 2, which is assumed to be the default org
    # Returns:
    # 204?
    #

    @staticmethod
    def createOrg(params):
        logging.info("createOrg-params: a list of things")

        if params['parentOrgId'] is None:
            params['parentOrgId'] = "2"

        payload = {}

        r = c42Lib.executeRequest("post", c42Lib.cp_api_org + "/" + str(orgId), params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)
        
        if (r.status_code == 204):
            return True
        elif (r.status_code == 500):
            content = r.content
            binary = json.loads(content)
            logging.debug(binary)
            return False
        else:
            return False


    #
    # updateOrg(orgUid):
    # Updates Org values
    # params:
    # orgUid - id of the organization.
    # idType - should be orgUid, orgId is being deprecated

    @staticmethod
    def modifyOrg(**kwargs):
        logging.info("modifyOrg-orgId:" + str(kwargs))

        if kwargs:

            params  = {}
            payload = {}

            if kwargs['orgUid'] and kwargs['payload']:
                
                params['idType'] = 'orgUid'
                payload = {kwargs['payload']}

                r = c42Lib.executeRequest('put', c42Lib.cp_api_org + "/" + str(orgUid), params, payload)

                logging.debug(r.text)

                content = r.content
                binary = json.loads(content)
                logging.debug(binary)

                try:
                    orgData = binary['data']

                    return orgData

                except TypeError:

                    return int(r.status_code)

        else:

            return 500  # Didn't provide an action



    #
    # deactivateOrg(orgId):
    # Deactivates an orginization based orgId
    # params:
    # orgId - id of the organization.
    # Returns:
    # 201 - Deactivated?
    # 204 - Already Deactivated
    # 404 - Not Found

    @staticmethod
    def deactivateOrg(**kwargs):
        logging.info("deactivatedOrg-orgId:" + str(kwargs))

        params  = {}
        payload = {}

        action = ''

        if kwargs:
            if kwargs['action']:
                if kwargs['action'] =='reactivate':
                    action = 'delete'  # Reactivate org (or remove deactivation)

                if kwargs['action'] == 'deactivate':
                    action = 'put'     # Deactivate org

            if action == '':
                return 500 # No action was passed along so return error code 500

            if kwargs['orgId']:
                
                orgId = kwargs['orgId']

                r = c42Lib.executeRequest(action, c42Lib.cp_api_orgDeactivation + "/" + str(orgId), params, payload)

                logging.debug(r.text)

                content = r.content
                binary = json.loads(content)
                logging.debug(binary)
                
                return int(r.status_code)
                    # 201 - Deactivated?
                    # 204 - Already Deactivated
                    # 404 - Not Found

        else:

            return 500  # Didn't provide an action


    #
    # getOrg(orgId):
    # Returns all organization data for specified organization
    # params:
    # orgId - id of the organization you want to return
    # Returns:
    # json object
    #

    @staticmethod
    def getOrg(orgId,**kwargs):
        logging.info("getOrg-params:orgId[" + str(orgId) + "]")

        params = {}

        if not kwargs:
            params['incAll'] = 'true'
            params['idType'] = 'orgId'
        else:
            params = kwargs['params']

        payload = {}

        r = c42Lib.executeRequest("get", c42Lib.cp_api_org + "/" + str(orgId), params, payload)

        logging.debug(r)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        try:
            if binary['data']:
                org = binary['data']

        except TypeError:

            org = None

        return org


    #
    # getOrgs(pgNum):
    # returns json list object of all users for the requested page number
    # params:
    # pgNum - page request for information (starting with 1)
    #

    @staticmethod
    def getOrgs(pgNum,**kwargs):
        logging.info("getOrgs-params:pgNum[" + str(pgNum) + "]")

        params = {}

        if kwargs:
            logging.info("getOrgs-params:kwargs[" + str(kwargs) + "]")

            if kwargs['params']:
                params = kwargs['params']

        params['pgNum'] = str(pgNum)
        params['pgSize'] = str(c42Lib.MAX_PAGE_NUM)

        payload = {}

        r = c42Lib.executeRequest("get", c42Lib.cp_api_org, params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        orgs = binary['data']
        return orgs


    #
    # getOrgsNew(**kwargs):
    # returns json list object of all users for the requested page number
    # params:
    # pgNum - page request for information (starting with 1)
    #

    @staticmethod
    def getOrgsNew(**kwargs):
        logging.info("getOrgs")

        params = {}

        if kwargs:
            logging.info("getOrgs-params:kwargs[" + str(kwargs) + "]")

            if kwargs['params']:
                params = kwargs['params']
            else:
                params['pgNum'] = 1

        params['pgSize'] = str(c42Lib.MAX_PAGE_NUM)

        payload = {}

        r = c42Lib.executeRequest("get", c42Lib.cp_api_org, params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        orgs = binary['data']
        return orgs


    #
    # getOrgPageCount():
    # returns number of pages of orgs within the system using MAX_PAGE_NUM
    # returns: integer
    #

    @staticmethod
    def getOrgPageCount():
        logging.info("getOrgPageCount")

        params = {}
        params['pgSize'] = '1'
        params['pgNum'] = '1'

        payload = {}
        r = c42Lib.executeRequest("get", c42Lib.cp_api_org, params, payload)

        logging.debug(r.text)
        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        orgs = binary['data']
        totalCount = orgs['totalCount']

        logging.info("getOrgPageCount:totalCount= " + str(totalCount))

        # num of requests is rounding down and not up. Add+1 as we know we are completed because the computerId value returns as 0
        numOfRequests = int(math.ceil(totalCount/c42Lib.MAX_PAGE_NUM)+1)

        logging.info("getOrgPageCount:numOfRequests= " + str(numOfRequests))

        return numOfRequests


    @staticmethod
    def getAllOrgs():
        logging.info("getAllOrgs")
        currentPage = 1
        keepLooping = True
        fullList = []
        while keepLooping:
            pagedList = c42Lib.getOrgs(currentPage)
            if pagedList['orgs']:
                fullList.extend(pagedList['orgs'])
            else:
                keepLooping = False
            currentPage += 1
        return fullList

    #
    # getDeviceByGuid(guid):
    # returns device information based on guid
    # params:
    # guid - guid of device
    #

    @staticmethod
    def getDeviceByGuid(guid, **kwargs):
        logging.info("[start] getDeviceByGuid-params:guid[" + str(guid) + "]")

        if kwargs and 'params' in kwargs:
            params = kwargs['params']
        else:
            params = {}
        if kwargs and 'incBackupUsage' in kwargs:
                params["incBackupUsage"] = "{0}".format(kwargs['incBackupUsage'])
        params['idType'] = "guid"

        payload = {}

        try:

            r = c42Lib.executeRequest("get", c42Lib.cp_api_computer + "/" + str(guid), params, payload)

            logging.debug(r.text)
            logging.info("Returned Status Code : {}".format(r.status_code))

            if r.status_code == 200:

                content = r.content
                binary = json.loads(content)
                logging.debug(binary)
                device = binary['data']

            else:

                logging.info("Returned Status Code [ {} ] when getting device GUID {}...".format(r.status_code,guid))
                device = None

        except Exception as e:
            logging.info("Error [ {} ] getting device GUID {}...".format(e,guid))
            device = None

        logging.info("[  end] getDeviceByGuid-params:guid[" + str(guid) + "]")
        return device


    #
    # getDeviceById(computerId):
    # returns device information based on computerId
    # params:
    # computerId: computerId of device
    #

    @staticmethod
    def getDeviceById(computerId):
        logging.debug("getDeviceById-params:computerId[" + str(computerId) + "]")

        params = {}
        params['incAll'] = 'true'

        payload = {}

        r = c42Lib.executeRequest("get", c42Lib.cp_api_computer + "/" + str(computerId), params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)

        logging.debug(binary)

        device = binary['data']
        return device

    #
    # getDeviceByParams(params):
    # returns device information based on custom parameters
    # params:
    # any of the device parameters
    #

    @staticmethod
    def getDeviceParams(**kwargs):
        logging.info("getDeviceParams-params: [" + str(kwargs))

        params = {}

        if kwargs['params']:
            params = kwargs['params']

            payload = {}

            r = c42Lib.executeRequest("get", c42Lib.cp_api_computer + "/", params, payload)

            logging.debug(r.text)

            content = r.content.decode("UTF-8")
            binary = json.loads(content)
            logging.debug(binary)

            binary_length = len(binary['data']['computers'])

            if binary_length > 0:

                device = binary['data']['computers'][0]

            else:

                device = None # If the result is null

        else:

            device = None

        return device



    #
    # getDeviceByName(deviceName):
    # returns device information based on computerId
    # params:
    # deviceName: name of device
    #

    @staticmethod
    def getDeviceByName(deviceName, **kwargs):
        logging.info("getDeviceByName-params:name[" + deviceName + "],  " + str(kwargs))

        params = {}

        if kwargs['params']:
            params = kwargs['params']

        params['q'] = deviceName     

        payload = {}

        r = c42Lib.executeRequest("get", c42Lib.cp_api_computer + "/", params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        binary_length = len(binary['data']['computers'])

        if binary_length > 0:

            device = binary['data']['computers'][0]

        else:

            device = None # If the result is null

        return device

    #
    # getDeviceBackupReport(**kwargs):
    # returns the DeviceBackupReport
    # params:
    # params - These can be passed in to maximize the utility of the function.
    #          Report will page automatically.
    #
    # kwargs:
    # kwargs - params in kwargs take precedence


    @staticmethod
    def getDeviceBackupReport(**kwargs):
        logging.info("[begin] getDeviceBackupReport")
        if kwargs:
            logging.info("getDeviceBackupReport-kwargs:[" + str(kwargs) + "]")

        df           = False
        howManyPages = 99999
        params = {}  
        fullDeviceList = None
        fileData       = None
        
        # Use kwargs to override any defaults...
        if kwargs:
            if 'df' in kwargs:
                df = True
            if 'howManyPages' in kwargs:
                howManyPages = kwargs['howManyPages']
            if 'params' in kwargs:
                params = kwargs['params']


        if 'pgNum' not in params:
            # Set some required defaults
            params['pgNum'] = 1                     # Begin w/ Page 1
            params['pgSize'] = c42Lib.MAX_PAGE_NUM  # Limit page size to 250 per page
            #params['srtKey'] = 'archiveBytes' # Sort on archiveBytes
            #params['srtDir'] = 'desc'

        if 'active' not in params:
            params['active'] = True


        currentPage = params['pgNum']
        keepLooping = True
        fullList = []
        loopCount = 1
        dataSize = 0

        payload = {}

        #print params

        while keepLooping:
            logging.debug("getDeviceBackupReport-page:[" + str(currentPage) + "]")

            print "---------- Getting Device Backup Report Data : " + str(currentPage).zfill(3)

            try:
                r = c42Lib.executeRequest("get", c42Lib.cp_api_deviceBackupReport, params, payload)

                logging.info("Returned Status Code : " + str(r.status_code))
                logging.debug("       Returned Text : " + str(r.text))

            except requests.exceptions, e:
                logging.info('Error Reading DeviceBackupReport : ' + str(e))

                print "**********"
                print "********** Error Reading DeviceBackupReport : " + str(url) + " | " + e
                print "**********"

                keepLooping = False
                fileList    = None
                break

            if r.status_code != 200:

                logging.info("Returned Status Code " + str(r.status_code) + "... bailing.")

                fullDeviceList = None
                keepLooping    = False
                break                  #If it returns anything but a 200, bail

            content = r.content.decode('UTF-8')
            binary  = json.loads(content)
            logging.debug(content)

            if 'data' not in binary:
                logging.info("No data returned...")
                # Empty value returned, skip it.
                keepLooping = False
                break

            if len(binary['data']) < params['pgSize'] and len(binary['data'])==0:  # This should keep us from an extra try to get data only to have it return none.

                keepLooping = False


            if df and len(binary['data'])>0:
                logging.debug("Using DataFrame...")
                if loopCount == 1:
                    logging.info("First Time Filling the DataFrame Object...")
                    fileData = pd.DataFrame(binary['data'])
                else:
                    logging.info("Appending to DataFrame Object...")
                    tempFileData = pd.DataFrame(binary['data'])
                    fileData = pd.concat([fileData,tempFileData])

                dataSize = fileData.shape[0] # Get the number of rows...

           
            elif len(binary['data']) > 0:
                logging.debug("Using Dict...")
                fullDeviceList.extend(binary['data'])
                dataSize = len(fullDeviceList)

            else:
                keepLooping = 0

            currentPage += 1
            loopCount   += 1

            params['pgNum'] = currentPage

            if loopCount > howManyPages:
                keepLooping = False

            logging.info("Total Rows Collected : " + str(dataSize))
            print "----------   Total Backup Device Report Rows : " + str(dataSize) + "\n"


        logging.info("[ end] getDeviceBackupReport - Size : " + str(dataSize))    

        if df:
                             # Return a dataframe object
            tempFileData = None      
            return fileData
        else:                      # Return a JSON object
            return fullDeviceList
    


    #
    # getDevicesPageCount():
    # returns number of pages it will take to return all of the devices based on MAX_PAGE_NUM
    # Returns: integer
    #


    #
    # getDevicesPageCountByOrg(orgId):
    # returns number of pages it will take to return devices by organization based on MAX_PAGE_NUM
    # Returns: integer


    #
    # getDevices(pgNum):
    # returns all devices in system for requested page number within a single json object
    #

    @staticmethod
    def getDevices(pgNum,**kwargs):
        logging.info("getDevices-params:pgNum[" + str(pgNum) + "]")

        # headers = {"Authorization":getAuthHeader(cp_username,cp_password)}
        # url = cp_host + ":" + cp_port + cp_api_user
        params = {}
        params['pgNum'] = str(pgNum)
        params['pgSize'] = str(c42Lib.MAX_PAGE_NUM)
        params['active'] = 'true'
        params['incBackupUsage'] = 'true'
        params['incHistory'] = 'true'

        payload = {}

        # r = requests.get(url, params=payload, headers=headers)
        r = c42Lib.executeRequest("get", c42Lib.cp_api_computer, params, payload)

        logging.debug(r.text)

        content = r.content.decode('UTF-8')
        binary = json.loads(content)
        logging.debug(binary)

        devices = binary['data']['computers']
        return devices

    #
    # getDevicesCustomParams(pgNum, parmas):
    # returns all devices in system for requested page number within a single json object
    #

    @staticmethod
    def getDevicesCustomParams(**kwargs):
        logging.debug("getDevicesCustomParams")

        getFile = False

        if not kwargs:
            return False
        else:
            logging.debug("Kwargs : " + str(kwargs))
        
        df      = kwargs['df']      if 'df'      in kwargs else False
        getFile = kwargs['getFile'] if 'getFile' in kwargs else False
        getAll  = kwargs['getAll']  if 'getAll'  in kwargs else False

        if 'pgNum' in kwargs:
            pgNum = kwargs['pgNum']
        if 'params' in kwargs:
            params = kwargs['params']
        else:
            params = None 

        # headers = {"Authorization":getAuthHeader(cp_username,cp_password)}
        # url = cp_host + ":" + cp_port + cp_api_user
        if not params and not isinstance(params, dict):
            params = {}

        payload = {}

        if getFile:

            tempFileName = "TEMP-ComputerDownload.csv"

            parameters = "?export=1"

            if 'active' in params:
                parameters = parameters + "&active="+str(params['active'])
            

            url    = c42Lib.getRequestUrl(c42Lib.cp_api_computer) + parameters
            header = c42Lib.getRequestHeaders()


            try:
                r = requests.get(url,headers=header,allow_redirects=True,verify=c42Lib.cp_verify_ssl).content
               
                with open(tempFileName,"wb") as f:
                    f.write(r)
            except Exception, e:
                print "********** Error Getting CSV"
                print "           " + str(e)
                devices = None
                frameObject = None

            try:
                frameObject = pd.read_csv(tempFileName,index_col='guid')

            except Exception, e:

                logging.info("Error. : " + str(tempFileName) + " | Error : " + str(e))
                print "Error getting CSV : " + str(tempFileName)
                print "Will return 'None'."  #frameObject is set to None


            try:
                os.remove(tempFileName)
                print "---------- Removed existing TEMP CSV file..."
            except OSError:
                print "           Failed to remove TEMP file : [ "+str(tempFileName)+" ]" 


            devices     = frameObject
            frameObject = None

        elif getAll:
            logging.info("Get All Devices...")

            keepLooping = True
            deviceCount = 0

            pgNum = 1
            pgSize = c42Lib.MAX_PAGE_NUM
            params['pgNum']  = pgNum
            params['pgSize'] = pgSize

            devices = pd.DataFrame()

            while keepLooping:
                logging.info("Page : {}".format(pgNum))

                r = None

                try:
                    r = c42Lib.executeRequest("get", c42Lib.cp_api_computer, params, payload)
                    if r.status_code == 201:
                        binary = json.loads(content)
                    else:
                        binary = None

                except Exception as e:
                    logging.info("Error [ {} ] getting computers...")

                if binary:
                    data = binary['data']
                    data = data['computers']
                else:
                    data = None

                if data:
                    if len(data) < pgSize:
                        keepLooping = False

                    if devices.empty:
                        devices = pd.DataFrame(data)
                    else:
                        devices = pd.concat([devices,data])

                else:
                    keepLooping = False

                logging.info("Loaded : {} computers...".format(devices.shape[0]))

        else:

            # r = requests.get(url, params=payload, headers=headers)
            r = c42Lib.executeRequest("get", c42Lib.cp_api_computer, params, payload)

            logging.debug(r.text)

            content = r.content
            binary = json.loads(content)
            logging.debug(binary)

            try:
                devices = binary['data']['computers']
            except TypeError:
                devices = False

        return devices
    #
    # getDevicesByOrgPaged(orgId, pgNum):
    # returns devices by organization for requested page number within a single json object
    #

    @staticmethod
    def getDevicesByOrgPaged(orgId, params):
        logging.info("getDevicesByOrgPaged-params:orgId[" + str(orgId) + "]:params[" + str(params) + "]")

        if not params:

            params = {}
            params['orgId'] = orgId
            params['pgNum'] = str(pgNum)
            params['pgSize'] = str(c42Lib.MAX_PAGE_NUM)
            params['active'] = 'true'
            params['incBackupUsage'] = 'true'
            params['incHistory'] = 'true'

        payload = {}

        # r = requests.get(url, params=payload, headers=headers)
        r = c42Lib.executeRequest("get", c42Lib.cp_api_computer, params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        devices = binary['data']['computers']
        return devices


    #
    # getAllDevices():
    # returns all devices in system within single json object
    #

    @staticmethod
    def getAllDevices():
        logging.info("getAllDevices")
        currentPage = 1
        keepLooping = True
        fullList = []
        while keepLooping:
            pagedList = c42Lib.getDevices(currentPage)
            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList



    @staticmethod
    def getAllDevicesCustomParams(params):
        logging.info("getAllDevicesCustomParams:params[" + str(params) + "]")
        currentPage = 1
        keepLooping = True
        fullList = []
        while keepLooping:
            pagedList = c42Lib.getDevicesCustomParams(pgNum=currentPage, params=params)
            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList


    @staticmethod
    def getAllDevicesByOrg(orgId):
        logging.info("getAllDevicesByOrg-params:orgId[" + str(orgId) + "]")
        currentPage = 1
        keepLooping = True
        fullList = []
        while keepLooping:
            pagedList = c42Lib.getDevicesByOrgPaged(orgId, currentPage)
            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList


    @staticmethod
    def putDeviceSettings(computerId, payload):
        logging.info("putDeviceSettings-params:computerId[" + str(computerId) + "]:payload[" + str(payload) + "]")
        params = {}

        r = c42Lib.executeRequest("put", c42Lib.cp_api_computer + "/" + str(computerId), params, payload)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        device = binary['data']
        return device


    @staticmethod
    def putDeviceUpgrade(computerId):
        logging.info("putDeviceUpgrade-params:computerId[" + str(computerId) + "]")

        result = False

        params = {}
        payload = {}

        r = c42Lib.executeRequest("put", c42Lib.cp_api_deviceUpgrade + "/" + str(computerId), params, payload)

        logging.debug(r.text)
        logging.debug(r.status_code)

        if (r.status_code == 201):
            return True
        else:
            return False

    #
    # putDeviceDeactivate(computerId):
    # Deactivates a device based in the computerId passed
    # params:
    # computerId - id for the user to update
    # returns: user object after the update
    #

    @staticmethod
    def putDeviceDeactivate(computerId):
        logging.info("putDeviceDeactivate-params:computerId[" + str(computerId) + "]")

        deactivateSuccess = False

        if (computerId is not None and computerId != ""):
            try:
                r = c42Lib.executeRequest("put", c42Lib.cp_api_deacivateDevice+"/"+str(computerId),"","")
                logging.debug('Deactivate Device Call Status: '+str(r.status_code))
                if not (r.status_code == ""):
                    deactivateSuccess = True

            except Exception, e:
                logging.info('Could Not Deactivate : ' + str(computerId) + " | Error : " + str(e))

        else:
            logging.error("putDeviceDeactivate has no userID to act on")

        return deactivateSuccess


    #
    # attempts to block device
    # PUT
    @staticmethod
    def blockDevice(computerId):
        logging.info("blockDevice-params: computerId[" + str(computerId) + "]")

        params = {}
        payload = {}

        r = c42Lib.executeRequest("put", c42Lib.cp_api_computerBlock + "/" + str(computerId), params, payload)

        logging.debug(r.text)
        logging.debug(r.status_code)

        return True

    #
    # attempts to unblock device
    # DELETE
    @staticmethod
    def unblockDevice(computerId):
        #error codes: USER_IS_BLOCKED, USER_IS_DEACTIVATED
        logging.info("unblockDevice-params: computerId[" + str(computerId) + "]")

        params = {}
        payload = {}

        r = c42Lib.executeRequest("delete", c42Lib.cp_api_computerBlock + "/" + str(computerId), params, payload)

        logging.debug(r.text)
        logging.debug(r.status_code)

        return r.text

    #
    # Get User Roles
    # 
    @staticmethod
    def getUserRole(userId):
        logging.info("getUserRole-params: userId [ " + str(userId) + " ]")

        roles = False
        params = {}
        payload = {}

        try:
            r = c42Lib.executeRequest("get", c42Lib.cp_api_userRole + "/" + str(userId),params,payload)

            logging.debug("Returned Result : Status Code - " + str(r.status_code))
            logging.debug("                :     Content - " + str(r.content))

            if r.status_code != 404:

                content = r.content
                binary = json.loads(content)
                logging.debug(binary)

                roles = binary['data']

        except:

            roles = False

        return roles


    #
    # Adds the role to an individual user.
    # Note: attempts to add the role to a user even if it already exists.
    #
    @staticmethod
    def addUserRole(userId, roleName):
        logging.info("addUserRole-params: userId[" + userId + "]:roleName[" + roleName + "]")

        result = False
        if(userId!=1):
            # headers = {"Authorization":getAuthHeader(cp_username,cp_password)}
            # url = cp_host + ":" + cp_port + cp_api_userRole
            params = {}

            payload = {}
            payload['userId'] = userId
            payload['roleName'] = roleName

            # r = requests.post(url, data=json.dumps(payload), headers=headers)

            r = c42Lib.executeRequest("post", c42Lib.cp_api_userRole, params, payload)

            logging.debug(r.text)
            logging.debug(r.status_code)
            if(r.status_code == 200):
                result = True
        else:
            logging.debug("user is the default admin user, skip adding the user role.")
            result = True
        # Post was successful with an HTTP return code of 200
        return result


    #
    # Adds a role for all users per org
    #
    @staticmethod
    def addAllUsersRoleByOrg(orgId, roleName):
        logging.info("addAllUsersRoleByOrg-params: orgId[" + str(orgId) + "]:userRole[" + roleName + "]")

        count = 0
        users = c42Lib.getAllUsersByOrg(orgId)
        for user in users['users']:
            userId = str(user['userId'])
            userName = user['username']
            if (c42Lib.addUserRole(userId, roleName)):
                count = count + 1
                logging.info("Success: userRole[" + roleName + "] added for userId[" + userId + "]:userName[" + userName + "]")
            else:
                logging.info("Fail: userRole[" + roleName + "] added for userId[" + userId + "]:userName[" + userName + "]")

        logging.info("Total Users affected: " + str(count))

    #
    # Adds a role for all users per org
    #
    @staticmethod
    def addAllUsersRole(roleName):
        logging.info("addAllUsersRole-params: roleName[" + roleName + "]")

        count = 0
        users = c42Lib.getAllUsers()
        for user in users['users']:
            userId = str(user['userId'])
            userName = user['username']
            if (c42Lib.addUserRole(userId, roleName)):
                count = count + 1
                logging.info("Success: userRole[" + userRole + "] added for userId[" + userId + "]:userName[" + userName + "]")
            else:
                logging.info("Fail: userRole[" + userRole + "] added for userId[" + userId + "]:userName[" + userName + "]")

        logging.info("Total Users affected: " + str(count))


    #
    # Remove the role from an individual user.
    # Note: attempts to remove the role from a user even if the role doesn't exist.
    #
    @staticmethod
    def removeUserRole(userId, roleName):
        logging.info("removeUserRole-params: userId[" + userId + "]:roleName[" + roleName + "]")

        # headers = {"Authorization":getAuthHeader(cp_username,cp_password)}
        # url = cp_host + ":" + cp_port + cp_api_userRole
        params = {}
        params['userId'] = userId
        params['roleName'] = roleName

        payload = {}

        # r = requests.delete(url, data=json.dumps(payload), headers=headers)
        r = c42Lib.executeRequest("delete", c42Lib.cp_api_userRole, params, payload)

        logging.debug(r.text)
        logging.debug(r.status_code)

        # Delete was successful with an HTTP return code of 204
        return r.status_code == 204


    #
    # Removes the role for all users within an org
    #
    @staticmethod
    def removeAllUsersRoleByOrg(orgId, roleName):
        logging.info("removeAllUsersRoleByOrg-params:orgId[" + str(orgId) + "]:roleName[" + roleName + "]")

        count = 0
        users = c42Lib.getAllUsersByOrg(orgId)
        for user in users['users']:
            userId = str(user['userId'])
            userName = user['username']
            if (c42Lib.removeUserRole(userId, userRole)):
                count = count + 1
                logging.info("Success: userRole[" + userRole + "] removeal for userId[" + userId + "]:userName[" + userName + "]")
            else:
                logging.info("Fail: userRole[" + userRole + "] removal for userId[" + userId + "]:userName[" + userName + "]")

        logging.info("Total Users affected: " + str(count))


    #
    # Removes the role for all users
    #
    @staticmethod
    def removeAllUsersRole(roleName):
        logging.info("removeAllUsersRole-params:roleName[" + roleName + "]")

        count = 0
        users = c42Lib.getAllUsers()
        for user in users['users']:
            userId = str(user['userId'])
            userName = user['username']
            if (c42Lib.removeUserRole(userId, userRole)):
                count = count + 1
                logging.info("Success: userRole[" + userRole + "] removeal for userId[" + userId + "]:userName[" + userName + "]")
            else:
                logging.info("Fail: userRole[" + userRole + "] removal for userId[" + userId + "]:userName[" + userName + "]")

        logging.info("Total Users affected: " + str(count))

    #
    # getPlan(params):
    # returns destination information
    # params:
    # See API reference

    @staticmethod
    def getPlan(params):
        logging.debug("getPlan - params: [" + str(params) + "]")

        payload = {}

        r = c42Lib.executeRequest("get", c42Lib.cp_api_plan, params, payload)

        logging.debug(r.text)

        if r.status_code == 200:

            content = r.content
            binary = json.loads(content)
            logging.debug(binary)

            if len(binary['data']) > 0:

                plan = binary['data']

            else:

                plan = None

        else:
            return None

        return plan

    # get a user's legal hold membership info
    # Minimum argument is userUid    

    @staticmethod
    def getUserLegalHoldMemberships(**kwargs):
        logging.info("getUserLegalHoldMembership-kwargs:userUid[" + str(kwargs) + "]")

        params = {}

        legalHoldMembershipInfo = None

        if 'params' in kwargs:

            params = kwargs['params']
        
        if 'activeState' in kwargs:
            params ['activeState'] = kwargs['activeState']  #Specifiy only the inactive, active or all memberships

        if 'userUid' in kwargs:
            params ['userUid'] = kwargs['userUid']
        payload = {}


        try:
            r = c42Lib.executeRequest("get", c42Lib.cp_api_legalHoldMembership, params, payload)
            logging.info("Server Response : " + str(r.status_code))

            # Check if legal hold is licensed.  If not return false...
            if r.status_code == '402':

                logging.info("Not licensed for legal hold... skipping.")

            else:

                logging.debug(r.text)
                content = r.content
                binary = json.loads(content)
                logging.debug(binary)

                logging.info("Returned membership response : " + str(binary))

                if 'data' in binary:

                    if 'legalHoldMemberships' in binary['data']:

                        legalHoldMembershipInfo = binary['data']['legalHoldMemberships']


        except Exception, e:
            logging.info("Error getting legal hold memberships : " + str(e))
            print "********** Could not get legal hold memberships : " + str(e)
            print "           Returning 'None'"
            
        return legalHoldMembershipInfo


    
    #
    # legalHoldHinfo(legalHoldUid):
    # Returns the info available for a Legal Hold
    # params:
    # legalHoldUid - Uid of the LegalHold to get/put info
    # userUid - Uid of the user being added or removed
    # actionType - "add" or "put" depending on what you'd like to have happen
    # returns: returns a 204 if successfully removed
    #


    @staticmethod
    def legalHoldInfo(**kwargs):
  
        logging.info("legalHoldInfo-params: " + str(kwargs))

        legalHoldInfo = False

        payload = {}

        if 'legalHoldUid' in kwargs:
            params = {}
            params["legalHoldUid"] = kwargs['legalHoldUid']
        
        elif 'params' in kwargs:
            params = kwargs['params']
        else:
            params = {}


        r = c42Lib.executeRequest("get", c42Lib.cp_api_legaHold, params, payload)
        logging.debug(r.status_code)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        try:
            if binary['data']['legalHolds']:
                legalHoldInfo = binary['data']['legalHolds']
        except TypeError:
            legalHoldInfo = False   

        return legalHoldInfo


    #
    # Params: Uid/Guid/Id - currently the API wants the ID not the GUID or UID
    # destinationId (kwargs): get storage history for destination
    # serverId (kwargs): get storage history for server
    # orgId (kwargs): get storage history for org
    # userId (kwargs): get storage history for destination
    # Returns: 30 days of storage history for the given type
    #
    @staticmethod
    def getStoredBytesHistory(Uid, **kwargs):
        logging.info("getStoredBytesHistory-params:Uid[" + str(Uid) + "], kwargs " + str(kwargs))

        params  = {}
        payload = {}

        if kwargs['destination']:
            params['destinationId'] = str(Uid)

        if kwargs['server']:
            params['serverId'] = str(Uid)

        if kwargs['org']:
            params['orgId'] = str(Uid)

        if kwargs['user']:
            params['userId'] = str(Uid)

        try:

            r = c42Lib.executeRequest("get", c42Lib.cp_api_storedBytesHistory, params, payload)
            content = r.content
            binary = json.loads(content)
            logging.debug(binary)

            if binary['data']:
                actionResults = binary['data']

            else:

                actionResults = None

        except Exception,e:

            logging.info("Failed to get stored bytes for userUid : " + str(Uid))
            logging.info("Error : " + str(e))

            actionResults = False


        return actionResults

    #
    # Get general legal hold info


    @staticmethod
    def getLegalHoldInfo(**kwargs):
        logging.info("getLegalHoldInfo-params:[" + str(kwargs) + "]")
        params = {}

        actionResults = False


        try:
            r = c42Lib.executeRequest("get", c42Lib.cp_api_legalHold, params, payload)

            logging.debug(r.status_code)
            content = r.content
            binary = json.loads(content)
            logging.debug(binary)

            if binary['data']:
                actionResults = binary['data']

            else:

                actionResults = False

        except Exception, e:
            logging.info("Error getting legal hold info : " + str(e))

        return actionResults




    # DO NOT USE, this api is un-paged and will cause performance issues
    # You've been warned
    # returns list of users in legal hold: active only
    #
    @staticmethod
    def getLegalHoldMembershipSummary(legalHoldUid):
        logging.info("getLegalHoldMembershipSummary-params:legalHoldUid[" + str(legalHoldUid) + "]")
        # Request URL:https://172.16.27.13:4285/api/legalHoldMembershipSummary/?legalHoldUid=741239804344030230&activeState=ALL
        # data.legalHoldMemberships.[0].user.username
        params = {}
        params['legalHoldUid'] = legalHoldUid
        params['activeState'] = "active"

        payload = {}
        # r = requests.get(url, params=payload, headers=headers)
        r = c42Lib.executeRequest("get", c42Lib.cp_api_legalHoldMembershipSummary, params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)


        users = binary['data']['legalHoldMemberships']

        return users

    @staticmethod
    def getAllLegalHoldMemberships(legalHoldUid, **kwargs):
        logging.info("getAllLegalHoldMemberships-params:legalHoldUid[" + str(legalHoldUid) + "]")
        if kwargs:
            logging.info("kwargs params: " + str(kwargs))

        currentPage = 1
        keepLooping = True
        fullList = []
        while keepLooping:
            pagedList = c42Lib.getAllLegalHoldMemberhipsPaged(legalHoldUid, currentPage, **kwargs)
            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList


    @staticmethod
    def getAllLegalHoldMemberhipsPaged(legalHoldUid, currentPage, **kwargs):
        logging.info("getAllLegalHoldMemberhipsPaged-params:legalHoldUid[" + str(legalHoldUid) + "]")
        if kwargs:
            logging.info("kwargs params: " + str(kwargs))
        logging.info("currentPage: " + str(currentPage))

        params = {}
        params['legalHoldUid'] = legalHoldUid
        params['pgNum'] = currentPage
        # default is 100... not sure if need to set
        # params['pgSize'] = "100"

        # spec says default is "Active", but not trusting it, so setting "Active" if no params inputted
        if kwargs and 'activeState' in kwargs:
            params['activeState'] = kwargs['activeState']
        else:
            params['activeState'] = "active"

        payload = {}
        r = c42Lib.executeRequest("get", c42Lib.cp_api_legalHoldMembership, params, payload)
        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        users = binary['data']['legalHoldMemberships']
        logging.info("number of users returned: " + str(len(users)))
        return users


    
    @staticmethod
    def addUserToLegalHold(legalHoldUid, userUid):
# {
#   "legalHoldUid":12938712892791283,
#   "userUid":"0cc175b9c0f1b6a8"
# }
        logging.info("addUserToLegalHold-params:legalHoldUid[" + str(legalHoldUid) + "]|userUid[" + str(userUid) + "]")
        params = {}

        payload = {}
        payload["legalHoldUid"] = legalHoldUid
        payload["userUid"] = userUid

        logging.info(str(payload))
        # r = requests.get(url, params=payload, headers=headers)
        r = c42Lib.executeRequest("post", c42Lib.cp_api_legalHoldMembership, params, payload)
        logging.debug(r.status_code)

        if (r.status_code == 201):
            logging.debug(r.text)

            content = r.content
            binary = json.loads(content)
            logging.debug(binary)


            response = binary['data']

            return response
        elif (r.status_code == 400):
            return False
        else:
            return False
        

    @staticmethod
    def deactivateUserFromLegalHoldMembership(legalHoldMembershipUid):
        logging.info("deactivateUserFromLegalHoldMembership-params:legalHoldMembershipUid[" + str(legalHoldMembershipUid) + "]")
        params = {}

        payload = {}
        payload["legalHoldMembershipUid"] = legalHoldMembershipUid

        logging.info(str(payload))
        # r = requests.get(url, params=payload, headers=headers)
        r = c42Lib.executeRequest("post", c42Lib.cp_api_legalHoldMembershipDeactivation, params, payload)
        logging.debug(r.status_code)


        if (r.status_code == 204):
            return True
        elif (r.status_code == 400):
            return False
        else:
            return False


    # Get an Archive

    @staticmethod
    def getArchive(**kwargs):

        logging.info("getArchive-params: " + str(kwargs))

        params = {}
        payload = {}

        if kwargs:

            if ('guid' in kwargs and 'params' not in kwargs):

                r = c42Lib.executeRequest("get", c42Lib.cp_api_archive+"/"+kwargs['guid'], payload)

            elif ('params' in kwargs):
                params = kwargs['params']

                r = c42Lib.executeRequest("get", c42Lib.cp_api_archive, params, payload)

            else:
                logging.info("getArchive-No archiveGUID or Params provided.  Returning None.")
                return None

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        try:
            archive = binary['data']['archives']
        
        except TypeError:
                
            return None

        return archive

    #End getArchive

    # Get Archives by entering by userUid - entered in the Params

    @staticmethod
    def getArchivesByUserId(params):
        logging.info("getArchivesByUserId-params: " + str(params))


        # params = {type: str(id), 'pgSize': '1', 'pgNum': '1'}
        # payload = {}
        # r = c42Lib.executeRequest("get", c42Lib.cp_api_archive, params, payload)


        payload = {}

        archives = None

        if params and (('userId' in params) or ('userUid' in params)):

            r = c42Lib.executeRequest("get", c42Lib.cp_api_archive, params, payload)

            logging.debug(r.text)

            content = r.content
            binary = json.loads(content)
            logging.debug(binary)

            archives = binary['data']['archives']

        return archives


## TO BE DELETED
##========================================================================================



    @staticmethod
    def getArchiveByStorePointId(storePointId,**kwargs):
        logging.info("getArchiveByStorePointId-params:storePointId[" + str(storePointId) + "]")
        currentPage = 1
        keepLooping = True
        fullList = []
        params = {}

        if kwargs:

            if 'params' in kwargs:
                params = kwargs['params']

        params['storePointId'] =  str(storePointId)
        while keepLooping:
            pagedList = c42Lib.getArchivesPaged(params,currentPage)
            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList


    @staticmethod
    def getArchivesByServerId(serverId):
        logging.info("getArchiveByServerId-params:serverId[" + str(serverId) + "]")
        currentPage = 1
        keepLooping = True
        fullList = []
        params = {}
        params['serverId'] = str(serverId)
        while keepLooping:
            pagedList = c42Lib.getArchivesPaged(params,currentPage)
            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList


    @staticmethod
    def getArchivesByDestinationId(destinationId):
        logging.info("getArchiveByDestinationId-params:destinationId[" + str(destinationId) + "]")
        currentPage = 1
        keepLooping = True
        fullList = []
        params = {}
        params['destinationId'] = str(destinationId)

        while keepLooping:
            pagedList = c42Lib.getArchivesPaged(params,currentPage)
            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList


    @staticmethod
    def getArchiveByGuidAndComputerId(guid, targetComputerId):
        logging.info("getArchiveByGuidAndComputerId-params:guid[" + str(guid) + "]:targetComputerId[" + str(targetComputerId) + "]")

        params = {}
        params['guid'] = str(guid)
        params['targetComputerId'] = str(targetComputerId)

        payload = {}

        r = c42Lib.executeRequest("get", c42Lib.cp_api_archive, params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        archives = binary['data']['archives']

        return archives


    @staticmethod
    def getArchivesByUserId(userId):
        logging.info("getArchivesByUserId-params:userId[" + str(userId) + "]")


        # params = {type: str(id), 'pgSize': '1', 'pgNum': '1'}
        # payload = {}
        # r = c42Lib.executeRequest("get", c42Lib.cp_api_archive, params, payload)

        params = {}
        params['userId'] = str(userId)
        #params['idType'] = 'uid' # For 4.x series

        payload = {}

        r = c42Lib.executeRequest("get", c42Lib.cp_api_archive, params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        archives = binary['data']['archives']

        return archives



    @staticmethod
    def getArchivesPaged(params, pgNum):
        logging.info("getArchivesPaged-params:params[" + str(params) + "]:pgNum[" + str(pgNum) + "]")

        params['pgSize'] = c42Lib.MAX_PAGE_NUM
        params['pgNum']  = pgNum
        payload = {}

        r = c42Lib.executeRequest("get", c42Lib.cp_api_archive, params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        archives = binary['data']['archives']

        #archives = collections.OrderedDict(sorted(unorderedArchives.items(),key=lambda X:X[14]))

        return archives


##===================================================================================================

    @staticmethod
    def getRestoreRecordPaged(params, pgNum):
        logging.info("[start] getRestoreRecordPaged-params:params[" + str(params) + "]:pgNum[" + str(pgNum) + "]")

        params['pgSize'] = c42Lib.MAX_PAGE_NUM
        params['pgNum'] = pgNum

        archives = None
        payload = {}

        try:

            r = c42Lib.executeRequest("get", c42Lib.cp_api_restoreRecord, params, payload)

            logging.debug(r.text)

            content = r.content
            binary = json.loads(content)
            logging.debug(binary)

        except Exception, e:
            logging.error("Error [ {} ] getting restore records".format(e))

        data = binary['data'] if 'data' in binary else None

        if data:
            archives = data['restoreRecords'] if 'restoreRecords' in data else None

        logging.info("[ end] getRestoreRecordPaged")
        return archives


    @staticmethod
    def getRestoreRecordAll():
        logging.info("getRestoreRecordAll")

        params = {}

        currentPage = 1
        keepLooping = True
        fullList = []
        while keepLooping:
            pagedList = c42Lib.getRestoreRecordPaged(params,currentPage)

            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList


    # cp_api_restoreHistory = "/api/restoreHistory"
    #?pgNum=1&pgSize=50&srtKey=startDate&srtDir=desc&days=9999&orgId=35

    @staticmethod
    def getRestoreHistoryForOrgId(orgId):
        logging.info("getRestoreHistoryForOrgId-params:orgId[" + str(orgId) + "]")

        params = {}
        params['strKey'] = 'startDate'
        params['days'] = '9999'
        params['strDir'] = 'desc'
        params['orgId'] = str(orgId)

        currentPage = 1
        keepLooping = True
        fullList = []
        while keepLooping:
            pagedList = c42Lib.getRestoreHistoryPaged(params,currentPage)

            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList


    @staticmethod
    def getRestoreHistoryForUserId(userId):
        logging.info("getRestoreHistoryForUserId-params:userId[" + str(userId) + "]")

        params = {}
        params['strKey'] = 'startDate'
        params['days'] = '9999'
        params['strDir'] = 'desc'
        params['userId'] = str(userId)
        params['idType'] = 'uid'

        currentPage = 1
        keepLooping = True
        fullList = []
        while keepLooping:
            pagedList = c42Lib.getRestoreHistoryPaged(params,currentPage)

            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList


    @staticmethod
    def getRestoreHistoryForComputerId(computerId):
        logging.info("getRestoreHistoryForComputerId-params:computerId[" + str(computerId) + "]")

        params = {}
        params['strKey'] = 'startDate'
        params['days'] = '9999'
        params['strDir'] = 'desc'
        params['computerId'] = str(computerId)

        currentPage = 1
        keepLooping = True
        fullList = []
        while keepLooping:
            pagedList = c42Lib.getRestoreHistoryPaged(params,currentPage)

            if pagedList:
                fullList.extend(pagedList)
            else:
                keepLooping = False
            currentPage += 1
        return fullList


    @staticmethod
    def getRestoreHistoryPaged(params, pgNum):
        logging.info("getRestoreHistoryPaged-params:params[" + str(params) + "]:pgNum[" + str(pgNum) + "]")

        #Let the page size be set in the params if it exists.

        try:
            if not params['pgSize']:
                params['pgSize'] = c42Lib.MAX_PAGE_NUM
        
        except TypeError:
            params['pgSize'] = params['pgSize']

        params['pgNum'] = pgNum

        payload = {}

        archives = False

        r = c42Lib.executeRequest("get", c42Lib.cp_api_restoreHistory, params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        try:

            archives = binary['data']['restoreEvents']
        
        except TypeError:
        
            archives = False

        return archives


    # this method gets the archive's metadata

    @staticmethod
    def archiveFileData(archiveData, **kwargs):

        logging.info("[start] archiveFileData - process archiveMetadata (clean it up)")

        dropColumns    = None
        includeDeleted = False
        isMetaData     = True

        if kwargs:
            if 'dropColumns' in kwargs:
                dropColumns = kwargs['dropColumns']

            if 'incDeleted' in kwargs:
                includeDeleted = True

            if 'isMetadata' in kwargs:
                isMetadata = True


        if dropColumns is None:

            dropColumns = [
                "planUid",
                "pathLength",
                "timestamp",
                "versionTimestamp",
                "sourceLastModified",
                "sourceLastModifiedTime",
                "fhPosition",
                "fhLen",
                "creatorGuid",
                "userUid",
                "fileId",
                "parentFileId",
                #"sourceChecksum",
                "fileType"
                ]

        fullFileData = []
        fileData     = []

        print "========== Reading Archive Metadata from Memory..."

        print "========== Archive Metadata Objects : " + str(len(archiveData['data']))
        # print archiveData['data']

        # convert to Pandas dataframe for more usefulness...

        logging.info("Begin Loading Data in to DataFrame")
        fileData = pd.DataFrame(archiveData['data'])
        logging.info("Done Loading data in to DataFrame")
        fileDataMemorySize = fileData.memory_usage(index=True).sum()
        logging.info(" Archive Data Memory Size : \n" + str(fileDataMemorySize))
        logging.info("Begin Processing of DataFrame - remove useless data")
        logging.info("  Pre-Clean Up Total Rows : " + str(fileData.shape[0]))

        # Remove Deleted, Empty files
        if includeDeleted is False:
            logging.info("Removing Deleted Files...")
            fileData = fileData.drop(fileData[(fileData.sourceChecksum == 'ffffffffffffffffffffffffffffffff') & (fileData.fileType == 0)].index)
            logging.info("Post-Remove Deleted Files : " + str(fileData.shape[0]))
        if not isMetadata:
            logging.info("Removing Directories...")
            fileData = fileData.drop(fileData[(fileData.fileType == 1)].index)  # Delete paths only
            logging.info("  Post-Remove Directories : " + str(fileData.shape[0]))
            logging.info("Removing Zero Byte Files...")
            fileData = fileData.drop(fileData[(fileData.sourceLength < 100)].index)
            logging.info(" Post-Remove 0 Byte Files : " + str(fileData.shape[0]))
        logging.info("Removing the first row because it's useless...")
        #fileData = fileData.drop(fileData.index[0])
        
        logging.info(" Post-Clean Up Total Rows : " + str(fileData.shape[0]))

        logging.info("Dropping unused columns...")
        for col in dropColumns:
            logging.info("Dropping : " + str(col))
            fileData = fileData.drop(col,axis=1)

        fileDataMemorySize = fileData.memory_usage(index=True).sum()
        logging.info(" Archive Data Memory Size : \n" + str(fileDataMemorySize))

        print "========== Done with basic processing of archive metadata..."

        logging.info("[end] archiveFileData - process archiveMetadata")

        return fileData


    #Get all archive metadata using the storage auth token
    @staticmethod
    def getAllArchiveMetadata(storageURL,storageAuthToken,dataKeyToken,guid,**kwargs):
        logging.info("getAllArchiveMetadata - params:")
        logging.info("                        Storage Server URL : " + str(storageURL))
        logging.info("                                 AuthToken : " + str(storageAuthToken))
        logging.info("                             DataKey Token : " + str(dataKeyToken))
        logging.info("                               Device GUID : " + str(guid))
        
        archiveSize = 0
        memoryLimit = 1073741826
        incDeleted  = False

        if kwargs:
            logging.info("                           Other Arguments : " + str(kwargs))

            if 'archiveSize' in kwargs:
                archiveSize = kwargs['archiveSize']

            if 'dropColumns' in kwargs:
                dropColumns = kwargs['dropColumns']
            else:
                dropColumns = [
                    "planUid",
                    "timestamp",
                    "sourceLastModified",
                    "sourceLastModifiedTime",
                    "userUid",
                    "fhPosition",
                    "fhLen",
                    "creatorGuid"
                    ]

            if 'memoryLimit' in kwargs:
                memoryLimit = kwargs['memoryLimit']

            if 'incDeleted' in kwargs:
                incDeleted = kwargs['incDeleted']


        params={}

        url = "{0}/api/ArchiveMetadata/{1}?decryptPaths=true&dataKeyToken={2}&incDeleted={3}"
        url = url.format(storageURL,guid,dataKeyToken,incDeleted)
        headers = {'Authorization': 'token ' + storageAuthToken[0] + '-' + storageAuthToken[1]}

        timeout = 7200


        fileData = None
        r        = None

        getMetadata_start_time = 0
        getMetadata_end_time   = 0
        getMetadata_total_time = 0

        params = {}

        logging.info("getAllArchivemetadata-Getting Archive Info : " + str(params))

        getMetadata_start_time = datetime.datetime.now().replace(microsecond=0)
        try:
            
            print "---------- [ " + str(guid) + " ] Archive Size : " + str(c42Lib.prettyNumberFormat(archiveSize))
            print "---------- [ " + str(guid) + " ] Start Time : " + str(getMetadata_start_time)
            r = requests.get(url, headers=headers, verify=False, timeout=timeout)
            getMetadata_end_time   = datetime.datetime.now().replace(microsecond=0)
            print "---------- [ " + str(guid) + " ]   End Time : " + str(getMetadata_end_time)
            getMetadata_total_time = getMetadata_end_time - getMetadata_start_time
            logging.info('Time to get archive metadata : ' + str(getMetadata_total_time))
            print "           Time to get archive metadata : " + str(getMetadata_total_time)
            print "           Metadata [ " + str(guid) + " ] Retrieved.  Begin processing..."

            #print r.content

        except requests.exceptions.Timeout:

            logging.info("getAllArchivemetadata - Timeout Error. GUID : " + str(guid) + " | Waited for : " + str(params['timeout']) + " seconds.")
            print "           Timing out getting archive: " + str(guid) + " | Waited for : " + str(params['timeout']) + " seconds."
            print "           Will return 'None'."
            getMetadata_end_time   = datetime.datetime.now().replace(microsecond=0)
            print "---------- [ " + str(guid) + " ]   End Time : " + str(getMetadata_end_time)
            getMetadata_total_time = getMetadata_end_time - getMetadata_start_time
            logging.info('Time to get archive metadata : ' + str(getMetadata_total_time))
            print "           Time to get archive metadata : " + str(getMetadata_total_time)
            return fileData

        except Exception, e:
            if e is None or e == '':
                e = "Unknown"
            logging.info("getAllArchivemetadata - Error. GUID : " + str(guid) + " | Error : " + str(e))
            print "********* Error getting archive: " + str(guid)
            print "          " + str(e)
            print "          Will return 'None'."
            getMetadata_end_time   = datetime.datetime.now().replace(microsecond=0)
            print "---------- [ " + str(guid) + " ]   End Time : " + str(getMetadata_end_time)
            getMetadata_total_time = getMetadata_end_time - getMetadata_start_time
            logging.info('Time to get archive metadata : ' + str(getMetadata_total_time))
            print "           Time to get archive metadata : " + str(getMetadata_total_time)
            return fileData


            # If the metadata is too big it we may have memory issues.
            # Check if metadata is less than 2 GB and then load into Pandas DataFrame from memory
            # otherwise, write to disk to read from disk into DataFrame

        if r:

            if len(r.content) < memoryLimit:

                print "========== Loading Data into JSON format..."

                try:
                    logging.info("Loading returned results into JSON")
                    content  = json.loads(r.content)

                except Exception, e:
                    
                    logging.info("getAllArchivemetadata - Error Parsing JSON : " + str(e))
                    print "********** Error Parsing JSON : " + str(guid)
                    print "           Will return 'None'."

                    return fileData

                try:

                    logging.info("Processing returned results into dataframe object")
                    fileData = c42Lib.archiveFileData(content,dropColumns=dropColumns,isMetadata=True)

                except Exception, e:

                    logging.info("Error processing data into dataframe object")
                    logging.info("Error : " + str(e))

                    return None

            else:

                logging.info("getAllArchivemetadata - Metadata file too big for memory : " + str(len(r.content)))
                print "Too Big..." + str(len(r.content)) + " bytes"
                print "Will return 'None'."

                return fileData

        return fileData            



    # Get 
    @staticmethod
    def getArchiveMetadata3(guid, dataKeyToken, decrypt, saveToDisk, **kwargs):
        logging.info("getArchiveMetadata3-params:guid["+str(guid)+"]:decrypt["+str(decrypt)+"]")

        fileData = None
        r        = None

        getMetadata_start_time = 0
        getMetadata_end_time   = 0
        getMetadata_total_time = 0

        memoryLimit = 1073741826

        params = {}
        if (decrypt):
            params['decryptPaths'] = "true"
        # always stream the response - remove memory limitation on requests library
        params['stream'] = "True"
        params['dataKeyToken'] = dataKeyToken
        params['timeout'] = 1800 # 30 minutes should Do It

        if kwargs:
            if 'memoryLimit' in kwargs:

                memoryLimit = kwargs['memoryLimit']

            if 'planUid' in kwargs:
                params['idType'] = 'planUid'

                # the following flags only apply if planUid is used

                if 'incDeleted' in kwargs:
                    params['excludeDeleted'] = kwargs['incDeleted']

                if 'startTime' in kwargs:
                    params['startTime'] = kwargs['startTime']

                if 'endTime' in kwargs:
                    params['endTime'] = kwargs['endTime']

 

        payload = {}

        logging.info("getArchiveMetadata3-Getting Archive Info : " + str(params))

        try:
            getMetadata_start_time = datetime.datetime.now().replace(microsecond=0)
            r = c42Lib.executeRequest("get", c42Lib.cp_api_archiveMetadata + "/" + str(guid), params, payload, **kwargs)
            getMetadata_end_time   = datetime.datetime.now().replace(microsecond=0)
            getMetadata_total_time = getMetadata_end_time - getMetadata_start_time
            logging.info('Time to get archive metadata : ' + str(getMetadata_total_time))
            print "Time to get archive metadata : " + str(getMetadata_total_time)
            print "Metadata [ " + str(guid) + " ] Retrieved.  Begin processing..."

        except requests.exceptions.Timeout:

            logging.info("getArchiveMetadata3 - Timeout Error. GUID : " + str(guid) + " | Waited for : " + str(params['timeout']) + " seconds.")
            print "Timing out getting archive: " + str(guid) + " | Waited for : " + str(params['timeout']) + " seconds."
            print "Will return 'None'."
            return fileData

        except Exception, e:

            logging.info("getArchiveMetadata3 - Error. GUID : " + str(guid) + " | Error : " + str(e))
            print "Error getting archive: " + str(guid)
            print "Will return 'None'."
            return fileData


            # If the metadata is too big it we may have memory issues.
            # Check if metadata is less than 2 GB and then load into Pandas DataFrame from memory
            # otherwise, write to disk to read from disk into DataFrame

        if r:

            if len(r.content) < memoryLimit:

                print "========= Loading Data into JSON format..."

                try:
                    logging.info("Loading returned results into JSON")
                    content  = json.loads(r.content)

                except Exception, e:
                    
                    logging.info("getArchiveMetadata3 - Error Parsing JSON : " + str(e))
                    print "********** Error Parsing JSON : " + str(guid)
                    print "           Will return 'None'."

                    return fileData

                try:

                    logging.info("Processing returned results into dataframe object")
                    fileData = c42Lib.archiveFileData(content)

                except Exception, e:

                    logging.info("Error processing data into dataframe object")
                    logging.info("Error : " + str(e))

                    return None

            else:

                logging.info("getArchiveMetadata3 - Metadata file too big for memory : " + str(len(r.content)))
                print "Too Big..." + str(len(r.content)) + " bytes"
                print "Will return 'None'."

                return fileData

        return fileData


    # only 3.6.2.1 and greater - json errors in pervious versions
    # will return array of info for every file within given archive
    # performance is not expected to be great when looking at large archives - impacted by number of files in archive
    # guid is int, decrypt is boolean

    # saveToDisk - will write out the response to a .json file
    @staticmethod
    def getArchiveMetadata2(guid, dataKeyToken, decrypt, saveToDisk, **kwargs):
        logging.info("getArchiveMetadata-params:guid["+str(guid)+"]:decrypt["+str(decrypt)+"]")

        params = {}
        if (decrypt):
            params['decryptPaths'] = "true"
        # always stream the response - remove memory limitation on requests library
        params['stream'] = "True"
        params['dataKeyToken'] = dataKeyToken
        params['timeout'] = 7200 # 2 Hours Should Do It
        payload = {}

        logging.info("Getting Archive Info : " + str(params))
        r = c42Lib.executeRequest("get", c42Lib.cp_api_archiveMetadata + "/" + str(guid), params, payload, **kwargs)

        print "---------- Getting Archive Metadata for GUID : " + str(guid)
        # http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
        if saveToDisk:
            # print r.text
            local_filename = "json/archiveMetadata_"+str(guid)+".json"
            logging.info("Begin Writing MetaData to File : " + str(loca))
            with open(local_filename, 'wb') as f:
                logging.debug("Opened : " + str(local_filename))
                chunkCounter = 0
                #print str(r)

                try: 
                    if not r.iter_content:
                        return ""
                except ChunkedEncodingError:
                    print "\n********** Chunked Encoding Error : " + str(r)
                    return ""
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk: # filter out keep-alive new chunks
                        chunkCounter += 1
                        # print "--------- Chunk : " + str(chunkCounter)
                        #print str(chunk)
                        #raw_input()
                        f.write(chunk)
                        #print str(chunkCounter).zfill(5) + " | " + str(chunk) + "\n"
                        f.flush()
                        if chunkCounter % 1000 == 0:
                            sys.stdout.write('.')
                            sys.stdout.flush()
                        if chunkCounter % 100000 == 0:
                            sys.stdout.write('|')
                            sys.stdout.flush()
                        if chunkCounter % 1000000 == 0:
                            sys.stdout.write('\nGuid : ' + str(guid) + " | " + str(c42Lib.prettyNumberFormat(chunkCounter*1000000)) + " Processed")
                            sys.stdout.write('\nTime Stamp : ' + str(time.strftime('%H:%M:%S', time.gmtime(time.time())))+"\n")
                            sys.stdout.flush()
                print ""

            logging.info("Done Writing Metadata to File : " + str(local_filename))

            print ""
        else:
            if r.text:
                content = ""
                if not r.iter_content:
                    return ""
                for chunk in r.iter_content(1024):
                    if chunk:
                        content = content + chunk
                binary = json.loads(content)
                del content
                # may be missing data by doing this call..
                # but this means the parcing failed and we can't extract the data
                if 'data' in binary:
                    
                    sys.stdout.write('*')
                    sys.stdout.flush()
                    print ""
                    
                    archiveMetadata = binary['data']
                    del binary
                    return archiveMetadata
                else:
                    return ""
            else:
                return ""


    #
    # getArchiveMainfest(url, headers, params):
    #
    # Get the archive manifest using the archiveMetadata API call
    # With the correct permissions, it works in the C42 Cloud
    #
    # Requires the proper auth tokens. Consult the API reference.
    #
    #
    @staticmethod
    def getArchiveManifest(url,headers,params):
        logging.info("getArchiveManifest - params: url [ " + str(url) + " ] headers [ " + str(headers) + " ] params [ " + str(params) + " ]")

        return None



    @staticmethod
    def getArchiveMetadata(guid, dataKeyToken, decrypt, **kwargs):
        c42Lib.getArchiveMetadata2(guid, dataKeyToken, decrypt, False, **kwargs)
    #
    # getServers():
    # returns servers information
    # params:
    #

    @staticmethod
    def getServers():
        logging.info("getServers")

        params = {}
        payload = {}

        return None

        try:
            r = c42Lib.executeRequest("get", c42Lib.cp_api_server, params, payload)

            logging.debug(r.text)

            content = r.content.decode("UTF-8")
            binary = json.loads(content)
            logging.debug(binary)

            servers = binary['data']['servers']

        except Exception, e:

            logging.info("Error getting servers : " + str(e))
            print "********** Error Getting Servers : " + str(e)

        return servers


    #
    # getServer(serverId):
    # returns server information based on serverId
    # params: serverId
    #

    @staticmethod
    def getServer(serverId,**kwargs):

        logging.info("getServer-params:serverId["+str(serverId)+"]")
        if kwargs:
            logging.info("getServer-kwargs : " + str(kwargs))

            if "this" in kwargs:
                logging.info("Getting THIS server's info...")
                serverId = "this"

        server = None

        params = {}
        payload = {}

        try:

            r = c42Lib.executeRequest("get", c42Lib.cp_api_server + "/" + str(serverId), params, payload)

            # logging.info("====server response : " + r.text + "====")

            logging.info("Returned Response Code : {}".format(r.status_code))
            if r.status_code == 200:

                content = r.content
                binary = json.loads(content)
                logging.debug(binary)

                if binary['data']:
                    logging.info("Server Info Size : {}".format(len(binary['data'])))
                    server = binary['data']
                else:
                    server = None

            else:
                logging.info("Reponse code [ {} ] returned.  Cannot provide server info.".format(r.status_code))
                return None

        except Exception, e:

            logging.info("Error getting servers : " + str(e))
            print "********** Error Getting Servers : " + str(e)

        logging.info("end - getServer-params:serverId["+str(serverId)+"]")
        return server

    #
    # getServer(serverId):
    # returns server information based on serverId
    # params: serverId
    #

    @staticmethod
    def getServerByParams(**kwargs):

        logging.info("getServer-params:serverId["+str(kwargs)+"]")

        params = {}
        payload = {}

        if kwargs:

            if ('params' in kwargs):
                params = kwargs['params']
                r = c42Lib.executeRequest("get", c42Lib.cp_api_server, params, payload)
            if ('serverId' in kwargs):
                serverId = kwargs['serverId']
                r = c42Lib.executeRequest("get", c42Lib.cp_api_server + "/" + str(serverId), params, payload)

        # logging.info("====server response : " + r.text + "====")

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        if binary['data']:
            server = binary['data']
        else:
            server = None

        return server

    #
    # getColdStorage(params):
    # Returns the cold storage archives using the supplied parameters
    # params:
    # returns: cold storage list for params
    #

    @staticmethod
    def getColdStorage(params):
        logging.info("getColdStorage - params [" + str(params)+ "]")

        
        payload = {}

        r = c42Lib.executeRequest("get", c42Lib.cp_api_coldStorage, params, payload)
            
        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        if binary['data']:
            
            return binary['data']

        else:
            
            return None



    #
    # getColdStorageByOrg(orgId):
    # Returns the cold storage archives in the supplied org
    # params:
    # orgId - id for the archive to update
    # returns: cold storage list for org object
    #

    @staticmethod
    def getColdStorageByOrg(orgId):
        logging.info("ColdStorageByOrg")

        params = {}
        params['pgSize'] = '250'
        params['pgNum'] = 1
        params['orgId'] = orgId
        params['srtKey'] = 'sourceUserName'
        params['srtDir'] = 'asc'
        params['active'] = 'true' # Only check against active orgs

        payload = {}

        currentPage = 1
        keepLooping = True
        fullList = []
        while keepLooping:
            pagedList = c42Lib.executeRequest("get", c42Lib.cp_api_coldStorage, params, payload)
            
            print 'Page :' + str(currentPage)
            content = pagedList.content
            binary = json.loads(content)
            list = binary['data']['coldStorageRows']
            
            if list:

                fullList.extend(list)
            else:
                keepLooping = False
            currentPage += 1
            params['pgNum'] = currentPage
            

        return fullList


    #
    # putColdStorageUpdate(archiveGuid, payload):
    # updates an archive's cold storage information based on the payload passed
    # params:
    # archiveId - id for the archive to update
    # payload - json object containing name / value pairs for values to update
    # returns: user object after the update
    #

    @staticmethod
    def putColdStorageUpdate(archiveGUID, payload):
        logging.info("putColdStorageUpdate-params:archiveGUID[" + str(archiveGUID) + "],payload[" + str(payload) + "]")

        params = {}
        params['idType'] = 'guid'

        if (payload is not None and payload != ""):
            r = c42Lib.executeRequest("put", c42Lib.cp_api_coldStorage + "/" + str(archiveGUID), params, payload)
            logging.debug(str(r.status_code))
            content = r.content
            binary = json.loads(content)
            logging.debug(binary)

            try:

                coldStorageArchive = binary['data']
                return coldStorageArchive
                logging.error("putColdStorageUpdate param payload is :" + str(coldStorageArchive))

            except TypeError:

                logging.error("putColdStorageUpdate returned nothing.")
                return None

            # if (r.status_code == 200):
                # return True
            # else:
                # return False
        else:
            logging.error("putColdStorageUpdate param payload is null or empty")
            return None


    @staticmethod
    def purgeColdStorage(guid,params):
        logging.debug("purgeColdStorage - guid: [" + str(guid) + "]")

        payload = {}
 
        r = c42Lib.executeRequest("delete", c42Lib.cp_api_coldStorage+"/"+str(guid), params, payload)

        logging.debug(r.text)

        coldStoragePurged = False

        if r.status_code == 200:

            content = r.content
            binary = json.loads(content)
            logging.debug(binary)

            coldStoragePurged = binary['data']

            #print coldStoragePurged
            #raw_input()

        return coldStoragePurged



    # getStorePoitnByStorePointId(storePointId):
    # returns store point information based on the storePointId
    # params:
    # storePointId: id of storePoint
    #

    @staticmethod
    def getStorePointByStorePointId(storePointId):
        logging.info("getStorePointByStorePointId-params:storePointId[" + str(storePointId) + "]")

        params = {}
        payload = {}

        storePoint = False

        r = c42Lib.executeRequest("get", c42Lib.cp_api_storePoint + "/" + str(storePointId), params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        try:
            storePoint = binary['data']

        except TypeError:

            storePoint = None


        return storePoint


    #EKR

    @staticmethod
    def ekr_jobCreate(userUid):
        logging.info("ekr_jobCreate-params:userUid[" + str(userUid) + "]")
        params = {}
        payload = {}

        r = c42lib.executeRequest("put", c42Lib.cp_api_ekr + "/" + str(userUid), params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        return binary


    @staticmethod
    def ekr_jobStatus(userUid, activeOnly):
        logging.info("ekr_jobStatus-params:userUid[" + str(userUid) + "] | activeOnly:[" + str(activeOnly) + "]")
        params = {}
        params['activeOnly'] = activeOnly
        payload = {}

        r = c42Lib.executeRequest("get", c42Lib.cp_api_ekr + "/" + str(userUid), params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        return binary


    @staticmethod
    def ekr_jobCancel(userUid):
        logging.info("ekr_jobCancel-params:userUid[" + str(userUid) + "]")
        params = {}
        payload = {}

        r = c42lib.executeRequest("delete", c42Lib.cp_api_ekr + "/" + str(userUid), params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        return binary

    @staticmethod
    def ekr_jobUpdate(userUid, command):
        # wakupJob
        # deleteBackupCopy
        logging.info("ekr_jobUpdate-params:userUid[" + str(userUid) + "] | command:[" + str(command) + "]")
        params = {}
        params['command'] = command
        payload = {}

        r = c42Lib.executeRequest("post", c42Lib.cp_api_ekr + "/" + str(userUid), params, payload)

        logging.debug(r.text)

        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        return binary


    # params:
    # 
    @staticmethod
    def smartsearch(**kwargs):
        logging.info("requestSmartSearch: " + str(kwargs))
        payload = {}
        if kwargs:
            params=kwargs['params']
        else:
            return None
        
        r = c42Lib.executeRequest("get", c42Lib.cp_api_smartsearch + "?", params, payload)
        contents = r.content.decode("UTF-8")
        binary = json.loads(contents)
        logging.info("requestSmartSearch Response: " + str(contents))
        return binary['data'] if 'data' in binary else None



    #
    # Compute base64 representation of the authentication token.
    #
    @staticmethod
    def getAuthHeader(u,p):

        format = '%s:%s' % (u,p)
        if isinstance(format, bytes):
            token = base64.b64encode(format).decode('UTF-8')
        else:
            token = base64.b64encode(bytes(format, 'UTF-8')).decode('UTF-8')

        return "Basic %s" % token


    #
    # Gets the V3 JWT Auth Token for such things as the new, undocumented customerLicense API
    #
    @staticmethod
    def getJWTAuth(**kwargs):
        params  = {}
        payload = {}

        JWTCookies = None

        try:
            r = c42Lib.executeRequest("get", c42Lib.cp_api_jwtAuthToken, params, payload)

            logging.debug(r.status_code)
            logging.debug(r.cookies)
            content = r.cookies
           
            for cookie in content:

                logging.debug("Cookie : " + str(cookie))

                JWTCookie = {}
                JWTCookie[cookie.name]  = cookie.value


        except Exception, e:

            logging.info("Error getting JWT Cooke : " + str(e))

        return JWTCookie




    #
    # Sets logger to file and console
    #
    @staticmethod
    def setLoggingLevel(**kwargs):
        # set up logging to file

        c42Lib.cp_logFileName = c42Lib.getFilePath(c42Lib.cp_logFileName)
        showInConsole = True

        if not kwargs:

            # Legacy Logging Setup
            if c42Lib.cp_logLevel == 'INFO':

                logging.basicConfig(
                                    level = logging.info,
                                    format='%(asctime)s [%(name)-8s] [ %(levelname)-6s ] [%(funcName)20s():%(lineno)5s] %(message)s',
                                    datefmt='%m-%d %H:%M',
                                    #filename = str(c42Lib.cp_logFileName),
                                    filemode='w')

            else:

                logging.basicConfig(
                                    level = logging.debug,
                                    format='%(asctime)s [%(name)-8s] [ %(levelname)-6s ] [%(funcName)20s():%(lineno)5s] %(message)s',
                                    datefmt='%m-%d %H:%M',
                                    #filename = str(c42Lib.cp_logFileName),
                                    filemode='w')

            # define a Handler which writes INFO messages or higher to the sys.stderr
            console = logging.StreamHandler()

           # set a format which is simpler for console use
            formatter = logging.Formatter('%(asctime)s [%(name)-8s] [ %(levelname)-6s ] [%(funcName)20s():%(lineno)5s] %(message)s')
            # tell the handler to use this format
            console.setFormatter(formatter)
            # add the handler to the root logger
            logging.getLogger('').addHandler(console)

        else:

            # Fancy Split Logging - requires the use of KWARGS when calling the logging function.

            if kwargs:
                if 'showInConsole' in kwargs:
                    showInConsole = kwargs['showInConsole']  # Let's you turn off logging to the console if you like.
                if 'loggingLevel' in kwargs:
                    c42Lib.cp_logLevel = kwargs['loggingLevel']
                else:
                    kwargs['loggingLevel'] = c42Lib.cp_logLevel

            if c42Lib.cp_logLevel == 'INFO':

                logging.basicConfig(
                                    level=logging.info,
                                    format='%(asctime)s [%(name)-8s] [ %(levelname)-6s ] [%(funcName)20s():%(lineno)5s] %(message)s',
                                    datefmt='%m-%d %H:%M',
                                    #filename = str(c42Lib.cp_logFileName),
                                    filemode='w')

            if c42Lib.cp_logLevel == 'WARNING':

                print "\nSetting Logging Level to WARNING\n"

                logging.basicConfig(
                                    level=logging.warning,
                                    format='%(asctime)s [%(name)-8s] [ %(levelname)-6s ] [%(funcName)20s():%(lineno)5s] %(message)s',
                                    datefmt='%m-%d %H:%M',
                                    #filename = str(c42Lib.cp_logFileName),
                                    filemode='w')

            if c42Lib.cp_logLevel == 'DEBUG':

                print "\nSetting Logging Level to DEBUG\n"

                logging.basicConfig(
                                    level=logging.debug,
                                    format='%(asctime)s [%(name)-8s] [ %(levelname)-6s ] [%(funcName)20s():%(lineno)5s] %(message)s',
                                    datefmt='%m-%d %H:%M',
                                    #filename = str(c42Lib.cp_logFileName),
                                    filemode='w')

            if c42Lib.cp_logLevel == 'ERROR':

                print "\nSetting Logging Level to ERROR\n"

                logging.basicConfig(
                                    level=logging.error,
                                    format='%(asctime)s [%(name)-8s] [ %(levelname)-6s ] [%(funcName)20s():%(lineno)5s] %(message)s',
                                    datefmt='%m-%d %H:%M',
                                    #filename = str(c42Lib.cp_logFileName),
                                    filemode='w')

            if c42Lib.cp_logLevel == 'CRITICAL':

                print "\nSetting Logging Level to CRITICAL\n"

                logging.basicConfig(
                                    level=logging.critical,
                                    format='%(asctime)s [%(name)-8s] [ %(levelname)-6s ] [%(funcName)20s():%(lineno)5s] %(message)s',
                                    datefmt='%m-%d %H:%M',
                                    #filename = str(c42Lib.cp_logFileName),
                                    filemode='w')

            # Set log file format
            loggingFormatter = logging.Formatter('%(asctime)s [%(name)-8s] [ %(levelname)-6s ] [%(funcName)20s():%(lineno)5s] %(message)s')
            #logfile = logging.FileHandler(str(c42Lib.cp_logFileName))
            #logfile.setFormatter(loggingFormatter)

            # set a format which is simpler for console use
            console = logging.StreamHandler()
            console.setFormatter(loggingFormatter)

            # add the handler to the root logger
            #logging.getLogger('').addHandler(logfile)
            
        if not showInConsole: 

            logging.getLogger('').addHandler(console)

        else:
            print "Suppress Logging Output to Console"
            logging.getLogger('').removeHandler(console)

        '''
        if os.path.exists(c42Lib.getFilePath('deleteme.log')):

            logging.debug('setLoggingLevel: delete temporary log file : ' + str(c42Lib.getFilePath('deleteme.log')))
            
            try:
                os.remove(c42Lib.getFilePath('deleteme.log'))
            except OSError:

                print ""
                print "Could not delete : " + str(c42Lib.getFilePath('deleteme.log'))
                print ""
        '''

        logging.debug('end: setLoggingLevel ' + str(c42Lib.cp_logLevel))



    @staticmethod
    def executeCLICommand(payload):
        params = {}

        r = c42Lib.executeRequest("post", c42Lib.cp_api_cli, params, payload)

        logging.debug(r.text)
        content = r.content
        binary = json.loads(content)
        logging.debug(binary)

        return binary['data']

    #
    # credit: http://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
    #
    @staticmethod
    def sizeof_fmt(num):
        for x in ['bytes','KiB','MiB','GiB']:
            if num < 1024.0 and num > -1024.0:
                return "%3.1f%s" % (num, x)
            num /= 1024.0
        return "%3.1f%s" % (num, 'TiB')



    @staticmethod
    def sizeof_fmt_si(num):
        for x in ['bytes','kB','MB','GB']:
            if num < 1000.0 and num > -1000.0:
                return "%3.1f%s" % (num, x)
            num /= 1000.0
        return "%3.1f%s" % (num, 'TB')




    @staticmethod
    def returnHostAndPortFromFullURL(url):
        p = '(?:http.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'
        m = re.search(p, str(url))

        # address = [m.group('protocol') +''+ m.group('host'),m.group('port')]
        # m.group('host') # 'www.abc.com'
        # m.group('port') # '123'
        # address = [m.group('http')]
        # print address
        return address


    # Read a CSV file

    @staticmethod
    def readCSVfile(csvFileName):
        logging.info("readCSVfile:file - [" + csvFileName + "]")

        fileList = []

        csvFileName = c42Lib.getFilePath(csvFileName)

        csvfile = open(csvFileName, 'rU')

        if (',' in csvfile.read(1024)):
            csvfile.seek(0) # Return to beginning of file
            fileDialect = csv.Sniffer().sniff(csvfile.read(1024),'\n')
            csvfile.seek(0) # Return to beginning of file

            reader = csv.reader(csvfile, delimiter=fileDialect.delimiter,dialect=fileDialect)

        else:  # Use for single column without a delimiter
            csvfile.seek(0) # Return to beginning of file
            reader = csv.reader(csvfile)

        for row in reader:
            if len(row) != 0:  #Don't include the row if it's blank or empty
                fileList.append(row)

        return fileList

    # Read a CSV file

    @staticmethod
    def readCSVFiletoDictionary(**kwargs):
        logging.info("readCSVfile:file - [" + str(kwargs) + "]")

        newValueList = []

        csvFileName = kwargs['csvFileName']
        csvFileName = c42Lib.getFilePath(csvFileName)

        fileList = {}

        with open (csvFileName,'r') as csvFile:
            row = csv.DictReader(csvFile)
            for value in row:
                fileList.setdefault(value['Key'],[]).append(value['Value'])

        newValueList = {}

        for key,value in fileList.items():
            newValueList[key] = value[0]

        if 'ordered' in kwargs:
            if kwargs['ordered']:

                newValueList = collections.OrderedDict(sorted(newValueList.items(),key=lambda X:X[0]))
        
        return newValueList

    # Read a CSV file into a dataframe
    @staticmethod
    def loadCSVtoDataFrame(fileName):
        logging.info('[begin] - loadCSVtoDataFrame : ' + str(fileName))

        frameObject = None

        try:
            frameObject = pd.read_csv(fileName)

        except Exception, e:

            logging.info("loadCSVtoDataFrame - Error. : " + str(fileName) + " | Error : " + str(e))
            print "Error getting CSV : " + str(fileName)
            print "Will return 'None'."  #frameObject is set to None

        logging.info('[  end] - loadCSVtoDataFrame')

        return frameObject


    # CSV Write & Append Method
    # Will apped to a CSV with n number of elements.  Pass in a list and it writes the CSV.

    @staticmethod
    def writeCSVappend(listtowrite,filenametowrite,writeType):
        logging.info("writeCSVappend:file - [" + filenametowrite + "]")

        #Check the length of the list to write.  If more than one item, then iterate through the list

        filenametowrite = c42Lib.getFilePath(filenametowrite)

        if (not isinstance(listtowrite, basestring)): #More than 1 item in list?
            # Correctly append to a CSV file
            output = open(filenametowrite, writeType) # Open the file to append to it

            # stufftowrite = []

            writestring = ''
            itemstowrite = ''
            itemsToWriteeEncoded = ''

            for stufftowrite in listtowrite:
                if (isinstance (stufftowrite,(int)) or isinstance(stufftowrite,(float)) or isinstance(stufftowrite,(long)) or isinstance(stufftowrite,(datetime.date))):
                    itemsToWriteeEncoded = stufftowrite
            
                elif stufftowrite is not None:

                    try: 
                        itemsToWriteeEncoded = stufftowrite.encode('utf8') # encoding protects against crashes
                    except AttributeError:
                        itemsToWriteeEncoded = stufftowrite
            
                else:
                    itemsToWriteeEncoded = stufftowrite
                writestring = writestring + str(itemsToWriteeEncoded) + ','
                logging.debug("writeCSVappend:file - [" + filenametowrite + "] - " + str(writestring))

            writestring = writestring[:-1] + "\n" # Remove an extra space at the end of the string and append a return
            output.write (writestring)
            output.close

        else: #What happens if there is only one item and not a list
            # Correctly append to a CSV file
            output = open(filenametowrite, writeType) # Open the file to append to it

            
            if (isinstance (listtowrite,(int)) or isinstance(listtowrite,(float)) or isinstance(stufftowrite,(long)) or isinstance(stufftowrite,(datetime.date))):
                itemsToWriteeEncoded = listtowrite # if the item is an integer, just add it to the list
            
            elif listtowrite is not None: 
                itemsToWriteeEncoded = listtowrite.encode
            
            else: #All other cases
                itemsToWriteeEncoded = listtowrite.encode('utf8') # encoding protects against crashes
            
            writestring = str(itemsToWriteeEncoded)
            logging.debug("writeCSVappend:file - [" + filenametowrite + "] - " + str(writestring))
            writestring = writestring + "\n" # Remove an extra space at the end of the string and append a return
            output.write (writestring)
            output.close
    
        return

    #Write out dataframes to CSV or Excel files
    @staticmethod
    def writeDataframeFiles(processedData,fileName,**kwargs):
        logging.info('[begin] - writeDataframeFiles')
        logging.info('                      Params:')
        logging.info("                  File Name : " + str(fileName))
        
        cp_createXLSX = False
        sheetName     = "Sheet"
        writeIndex    = True

        if kwargs:
            logging.info("                     Kwargs : " + str(kwargs))

            if 'sheetName' in kwargs:
                sheetName = kwargs['sheetName']

            if 'createXLSX' in kwargs:
                cp_createXLSX = kwargs['createXLSX']

            if 'index' in kwargs:
                writeIndex=kwargs['index']


        csvSuccess  = False
        xlsxSuccess = False

        fileName = fileName+str(c42Lib.cp_todayDate)

        csvFileName = fileName + '.csv'

        logging.info('If existing CSV file exists, delete it...')

        try:
            os.remove(csvFileName)
            print "---------- Removed existing CSV file..."
        except OSError:
            print "           OK to create new " + str(csvFileName) + " file."


        if cp_createXLSX:

            xlsFileName = fileName + '.xlsx'

            logging.info('If existing XLSX file exists, delete it...')

            try:
                os.remove(xlsFileName)
                print "---------- Removed existing XLSX file..."
            except OSError:
                print "           OK to create new " + str(xlsFileName) + " file."

        try:
            fileDataMemorySize = processedData.memory_usage(index=True).sum()
            logging.info(" Device Report Data Memory Size : " + str(fileDataMemorySize))
            logging.info("                     Total Rows : " + str(processedData.shape[0]))
        except Exception, e:
            logging.info("Cannot report on memory size: " + str(e))

        logging.info("[Begin] Writing processed device backup report [ " + str( fileName ) + " ] as files...")

        
        if cp_createXLSX:

            print "---------- [ " + str(time.strftime('%H:%M:%S', time.gmtime(time.time()))) + " ] Writing out as XLSX..."

            try:
                xlsOutput = pd.ExcelWriter(xlsFileName, engine='xlsxwriter')
                processedData.to_excel(xlsOutput,sheet_name=sheetName)
                xlsOutput.save()

                logging.info("[  End] Done writing processed device backup report [ " + str( xlsFileName ) + " ] as XLSX...")
                print "---------- [ " + str(time.strftime('%H:%M:%S', time.gmtime(time.time()))) + " ] Done writing [ " + str( xlsFileName ) + " ] as XLSX..."

                xlsxSuccess = True

            except Exception, e:

                logging.info("writeXLSFile - Error writing : " + str(xlsFileName) + " | Error : " + str(e))
                print "********* Error writing out XLSX file : " + str(xlsFileName)
                print "          " + str(e)
                print "          Will return 'False'."

        print "---------- [ " + str(time.strftime('%H:%M:%S', time.gmtime(time.time()))) + " ] Writing out as CSV..."

        try:
            logging.info("Include Index : {}".format(writeIndex))
            processedData.to_csv(csvFileName,index=writeIndex)

            logging.info("[  End] Done writing processed device backup report [ " + str( csvFileName ) + " ] as CSV...")
            print "---------- [ " + str(time.strftime('%H:%M:%S', time.gmtime(time.time()))) + " ] Done writing [ " + str( csvFileName ) + " ] as CSV..."

            csvSuccess = True

        except Exception, e:

            logging.info("writeCSVFile - Error writing : " + str(csvFileName) + " | Error : " + str(e))
            print "********** Error writing out CSV file : " + str(csvFileName)
            print "           Will return 'False'."
            
        if cp_createXLSX and xlsxSuccess and csvSuccess:
            return True
        elif not cp_createXLSX and csvSuccess:
            return True
        else:
            return False

        logging.info('[  end] - writeDataframeFiles - Success : ' + str(success))




    # CSV Creates files.  Single funciton that's used a lot to create output files in scripts.
    # params:   csvFileName - the base file name
    #           fileList - an array with a file name extension and the headers for the files to create
    #                       ['filetype':'whatisinthisfile','fileheaders':(header1,header2,header3,header4)]
    #           filedate - the timestamp for the files
    #           testMode - if anything except "execute" is passed to it the file

    @staticmethod
    def setupCSVFiles (csvFileName,fileList,fileDate,testMode,writeMode,**kwargs):
        logging.info("setupCSVFiles:base file name - [" + csvFileName + "]")

        # Add 'Test' to file name if a test
        fileNameTest = ''
        if testMode:
            fileNameTest = '-TEST'

        counter = 0
        fileNames = []

        if kwargs:
            if 'counter' in kwargs:
                counter = kwargs['counter']

        for index, fileHeader in enumerate(fileList):

            counter += 1

            fileDesc       = fileHeader['fileDesc']
            fileHeaderNames = fileHeader['fileHeaders']

            fileName = str(counter).zfill(2) + '-' + csvFileName + '-' + fileDesc + '-' + fileDate + fileNameTest + '.csv'

            fileName = c42Lib.getFilePath(fileName)

            c42Lib.writeCSVappend (fileHeaderNames,fileName,writeMode)
            fileNames.append(fileName)


        logging.info ("---------- CSV Files Created --------------------------------")
        return fileNames

        #End setupCSVFiles


    # Print Text File Contents to Screen.
    # Prints to the contents of a (text) file to the screen.
    # Used for printing disclaimer text out in executable script builds

    @staticmethod
    def printFileToScreen (filename):

        logging.info("printFileToScreen: filename - [" + str(filename) + "]")

        filename = c42Lib.getFilePath(filename)

        try:

            fileToPrint = open(filename, 'r')
            contentsToPrint = fileToPrint.read()
            print (contentsToPrint)
            fileToPrint.close()

        except IOError:

            print ""
            print "**********"
            print "********** Error Reading File [ " + str(filename) + " ] "
            print "**********"
            print ""

        logging.debug("END OF printFileToScreen: filename - [" + str(filename) + "]")

    #End printFileToScreen

    #Allow for arguments to be input/prompted rather than commandline.

    @staticmethod
    def inputArguments (**kwargs):

        logging.info("inputArguments: [" + str(kwargs) + "]")

        arguments = {}
        noArguments = False
        hasArguments = False


        if kwargs:

            # Check if an arguments file exists

            if ('argumentsFile' in kwargs):

                fileName = kwargs['argumentsFile']

                fileName = c42Lib.getFilePath(fileName)

                if os.path.exists(fileName):
                    arguments = c42Lib.readCSVFiletoDictionary(fileName)
                    if len(arguments) > 0:
                        hasArguments = True

                else:
                    print ""
                    print "********** Manual Parameter Entry Required"
                    print ""

                    noArguments = True


            if 'argumentList' in kwargs and not hasArguments:

                    noArguments = False

                    argumentList = kwargs['argumentList']

                    for index, argument in enumerate (sorted(argumentList,key=argumentList.__getitem__)):

                        if argumentList[argument] is not None:

                            if type(argumentList[argument]) is not bool:
                                arguments[argument] = raw_input(argumentList[argument])
                            else:
                                arguments[argument] = argumentList[argument]
                        else:
                            arguments[argument] = None

            elif not hasArguments:

                noArguments = True

        if noArguments or len(arguments) < 1:
            print ""
            print "********** NO PARAMETERS PROVIDED"
            print ""
            print "********** EXITING"
            print ""
            sys.exit('System Exit: No Parameters Provided')

        return arguments



    @staticmethod
    def processDirectorySyncData(dirSyncData,**kwargs):

        logging.info("[start] processDirectorySyncData")
        if kwargs:
            logging.info("kwargs : " + str(kwargs))

        print "========= Reading Directory Sync Data from Memory..."

        print "========= Directory Sync Objects : " + str(len(dirSyncData['data']))

        processArgs = None
        dropColumns = None

        if kwargs:
            if 'processArgs' in kwargs:
                processArgs = kwargs['processArgs']
                if 'dropColumns' in processArgs:
                    dropColumns = processArgs['dropColumns']

        fullFileData = []
        fileData     = []

        # print archiveData['data']

        # convert to Pandas dataframe for more usefulness...

        logging.info("Begin Loading Data in to DataFrame")
        fileData = pd.DataFrame(dirSyncData['data']['directorySyncHistories'],dtype=object)
        logging.info("Done Loading data in to DataFrame")
        fileDataMemorySize = fileData.memory_usage(index=True).sum()
        logging.info("Directory Sync Data Memory Size : " + str(fileDataMemorySize))
        logging.info("Begin Processing of DataFrame - remove useless data")
        logging.info("  Pre-Clean Up Total Rows : " + str(fileData.shape[0]))

        #logging.info("Removing the first row because it's useless...")
        #fileData = fileData.drop(fileData.index[0])
        
        logging.info(" Post-Clean Up Total Rows : " + str(fileData.shape[0]))

        if dropColumns is not None:
            logging.info("Dropping unused columns...")
            for col in dropColumns:
                logging.info("Dropping : " + str(col))
                fileData = fileData.drop(col,axis=1)

        logging.info("Set Index to existing ID")
        fileData = fileData.set_index('directorySyncHistoryId')

        fileDataMemorySize = fileData.memory_usage(index=True).sum()
        logging.info("Directory Sync Data Memory Size : " + str(fileDataMemorySize))

        print "========= Done with basic processing of directory sync data"

        logging.info("[end] processDirectorySyncData")

        return fileData


    # Get directory sync data
    @staticmethod
    def getDirectorySyncData(searchType,searchTerm,**kwargs):
        logging.info("[start] getDirectorySyncData")
        if kwargs:
            logging.info("getDirectorySyncData - kwargs : " + str(kwargs))

        directorySyncData = None
        r                 = None

        params      = {}
        timeout     = 1800 # 10 Minute Timeout Default
        processArgs = None
        pgSize      = 1000 # return up to 1000 directory sync results

        memoryLimit = 1073741826 # 1 GB Default

        if kwargs:
            if 'memoryLimit' in kwargs:
                memoryLimit = kwargs['memoryLimit']
            if 'params' in kwargs:
                params = kwargs['params']

                if not 'timeout' in params:
                    params['timeout'] = timeout

                if not 'pgSize' in params and searchType is not None:
                    params['pgSize'] = pgSize

                if not 'pgNum' in params:
                    params['pgNum'] = 1

            if 'processArgs' in kwargs:
                processArgs = kwargs['processArgs']
            else:
                processArgs = {}
        else:
            processArgs = {}

        payload = {}
        params['srtDir'] = "desc"  # Always sort from newest to oldest

        if searchType == None:
            searchType = "?pgSize="+str(pgSize)
        else:
            searchType = "/" + str(searchType) + "?" + str(searchTerm)

        try:
            print "---------- Getting directory sync data... please wait."
            r = c42Lib.executeRequest("get", c42Lib.cp_api_directorySync + searchType, params, payload,timeout=timeout)
            logging.info("Directory Sync Data Retreived... begin processing.")

        except requests.exceptions.Timeout:

            logging.info("getDirectorySyncData - Timeout Error.")
            return directorySyncData

        except Exception, e:

            logging.info("getDirectorySyncData - Error : " + str(e))
            return directorySyncData


                # If the metadata is too big it we may have memory issues.
                # Check if metadata is less than 2 GB and then load into Pandas DataFrame from memory
                # otherwise, write to disk to read from disk into DataFrame

        if r:

            if len(r.content) < memoryLimit:

                print "========= Loading Data into JSON format..."

                try:
                    logging.info("Loading returned results into JSON")
                    content  = json.loads(r.content)

                except Exception, e:
                    
                    logging.info("[end] getDirectorySyncData - Error Parsing JSON : " + str(e))
                    print "********** Error Parsing JSON"
                    print "           Will return 'None'."

                    return directorySyncData

                try:

                    logging.info("Processing returned results into dataframe object")
                    logging.info("Object has : " + str(len(content['data']['directorySyncHistories'])) + " directory sync entries.")
                    directorySyncData = c42Lib.processDirectorySyncData(content, processArgs = processArgs)

                except Exception, e:

                    logging.info("Error processing data into dataframe object")
                    logging.info("Error : " + str(e))
                    logging.info("[end] getDirectorySyncData")

                    return directorySyncData

            else:

                logging.info("getDirectorySyncData - Too big for memory : " + str(len(r.content)))
                print "Too Big..." + str(len(r.content)) + " bytes"
                print "Will return 'None'."
                logging.info("[end] getDirectorySyncData")

                return directorySyncData

        return directorySyncData



    @staticmethod
    def getFilePath(relativePath):
        logging.debug("getFilePath: [ " + str(relativePath) + " ]")

        try:
            base_path = sys._MEIPASS
            logging.debug("getFilePath - base_path :[ " + str(base_path) + " ]")

            # Get Platform Specific (mostly just Windows vs. the World)

            if str(os.name) != 'nt':
                # Find last directory slash

                logging.debug("getFilePath - os.name :[ " + str(os.name) + " ]")
                endOfPath = str(sys.executable).rfind('/')
                base_path = str(sys.executable)[:endOfPath+1]

                logging.debug("getFilePath - endOfPath :[ " + str(endOfPath) + " ]")
                logging.debug("getFilePath - base_path :[ " + str(base_path) + " ]")
            else:
                base_path = os.getcwd()
                logging.debug("getFilePath - base_path :[ " + str(base_path) + " ]")
        
        except Exception:
            
            base_path = os.path.abspath(".")
            logging.debug("getFilePath - base_path :[ " + str(base_path) + " ]")

        return os.path.join(base_path,relativePath)    


    # Try to make a directory
    @staticmethod
    def checkPathMakePath(filePath):

        try:

            os.makedirs(filePath)

        except OSError:

            if not os.path.isdir(filePath):

                # zero out file path if there is an issue
                filePath = ''

        return filePath
                

    # validateVersion method
    #
    # Inputs:
    #           version = version number #.#.# string - REQUIRED
    #           minorStrict = require the 2nd number to equal, otherwise must not be less than
    #           patchStrict = require the 3rd number to equal, otherwise must not be less than
    #
    # Output:
    #           True  if meets minimum version requirements
    #           False if does not meet minimum version requirements
    #
    # Note:
    #           Major version (1st #) must always be equal or greater than


    @staticmethod
    def validateVersion(**kwargs):

        logging.info('[start] - validateVersion : ' + str(kwargs))

        versionOK   = True
        minorStrict = False
        patchStrict = False

        majorOK     = True
        minorOK     = True

        c42Major = int(c42Lib.cp_c42Lib_version[0])
        c42Minor = int(c42Lib.cp_c42Lib_version[1])
        c42Patch = int(c42Lib.cp_c42Lib_version[2])

        if 'version' in kwargs:
            scriptVersion = kwargs['version'].split('.')
            if len(scriptVersion) != 3:
                versionOK = False
            else:
                major = int(scriptVersion[0])
                minor = int(scriptVersion[1])
                patch = int(scriptVersion[2])

        if 'majorStrict' in kwargs: majorStrict = kwargs['majorStrict']
        if 'minorStrict' in kwargs: minorStrict = kwargs['minorStrict']
        if 'patchStrict' in kwargs: patchStrict = kwargs['patchStrict']

        if majorStrict:

            if (major != c42Major):
                versionOK = False
                majorOK   = False
        elif (major > c42Major):
            versionOK = False
            majorOK   = False

        if majorOK:
            if minorStrict:

                if (minor != c42Minor):
                    versionOK = False
                    minorOK   = False
            elif (minor > c42Minor) and (major <= c42Major):
                versionOK = False
                minorOK   = False
        else:
            versionOK = False


        if majorOK and minorOK:
            if patchStrict:
                if (patch != c42Patch):
                    versionOK = False
            elif ((major == c42Major) and (minor == c42Minor) and (patch > c42Patch)):
                versionOK = False
        else:
            versionOK = False

        logging.info('[end] - validateVersion | Returned Value : ' + str(versionOK))

        return versionOK

    @staticmethod
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')



    @staticmethod
    def convertToBool(isItTrue):
        logging.debug('[start] - convertToBool : ' + str(isItTrue))
        if isItTrue:
            isItTrue = str(isItTrue).lower()
            if isItTrue in ('y','t','yes','true'):
                isItTrue = True
            else:
                isItTrue = False

        logging.debug('[  End] - convertToBool : ' + str(isItTrue))
        return isItTrue 


    @staticmethod
    def validateFileInput(userPrompt,fileToCheck):
        logging.info('[start] - validateFileInput : params - ' + str(userPrompt) + " , " + str(fileToCheck))

        fileName = None

        userInputOK = False
        tryCount = 0
        while not userInputOK and tryCount < 4:
            tryCount += 1
            if tryCount > 4:
                print ""
                print "********** Too many bad attempts.  Quitting."
                sys.exit()
            try:
                if os.path.exists(fileToCheck):
                    fileName = fileToCheck
                    userInputOK = True
                else:
                    logging.info('Failed to Find : ' + str(fileToCheck))
                    print ""
                    print "********** " + str(fileToCheck) + " Cannot be found.  Please try again."
                    print ""
                    fileToCheck = raw_input(userPrompt)
            except:
                logging.debug('********** Error trying to find file : ' + str(fileToCheck))
                print "********** ERROR ATTEMPTING TO FIND : " + str(fileToCheck)

        
        logging.info('[start] - validateFileInput : ' + str(fileName))
        return fileName         


    #Converts numbers to "pretty" format
    @staticmethod
    def prettyNumberFormat(num, suffix='B'):
        logging.debug('[start] - prettyNumberFormat : ' + str(num))
        for unit in ['',' K',' M',' G',' T',' P',' E',' Z']:
            if abs(num) < 1000.0:
                return "%3.2f%s%s" % (num, unit, suffix)
            num /= 1000.0
        logging.debug('[  end] - prettyNumberFormat : ' + "%.1f%s%s" % (num, 'Yi ', suffix))
        return "%.1f%s%s" % (num, 'Yi ', suffix)

    @staticmethod
    def yesNoMaybe(question,answer):
        logging.debug('[start] - yesNoMaybe : ' + str(question) + " | " + str(answer))
        
        whatDoYouSay = False
        inputCount = 0

        while inputCount < 4:  # User gets 4 chances to get it right.

            try:
                answer = answer.lower()  # Force it all lowercase
                if answer == 'y' or \
                   answer == 'yes' or \
                   answer == '1' or \
                   answer == 'true':
                    whatDoYouSay = True
                
                break

            except:

                print "********** Only Y or N, please...\n"
                inputCount += 1

                answer = raw_input(question)

        if inputCount > 3:

            print "********** Too many invalid inputs.  Quitting.  Please restart and retry."
            sys.exit(0)

        return whatDoYouSay

    # Generic Validate User Input method
    # Validates user input against a list of valid answers and allows a user to retry
    # answerType is "string", "number" or "bool" 

    @staticmethod
    def validateUserInput(userQuestion,validAnswers,answerType,**kwargs):

        logging.info("[begin] - validateUserInput")
        logging.info("          Question : " + str(userQuestion))
        logging.info("           Answers : " + str(validAnswers))
        logging.info("       Answer Type : " + str(answerType))
        logging.info("            Others : " + str(kwargs))

        tryCount = 0
        maxTries = 4
        userResponse  = None
        validResponse = False
        userValue     = None

        if kwargs:
            if 'maxTries'  in kwargs: tryCount  = kwargs['maxTries']
            if 'userValue' in kwargs: userValue = kwargs['userValue']

        if (answerType != 'integer' and answerType != 'float') or userValue == 'ALL':  # covert answers to lowercase for comparisons

            for index, answer in enumerate(validAnswers):
                validAnswers[index] = answer.lower()

        # Check if a user input has been passed in... if not, ask the question.
        if userValue is None:
            userResponse = raw_input(userQuestion).lower()
        else:
            userResponse = userValue.lower() # Make lower case!

        if userResponse == 'all' and answerType == 'integer':  # This lets a user input "ALL"
            answerType = ''

        while (tryCount < maxTries) and not validResponse:

            tryCount += 1

            if answerType == 'float':
                if userResponse.find('.'):  # Checks to see if the number is a float...      
                    userResponse = c42Lib.isFloat(userResponse)
                    if userResponse is None:
                        print "********** Not a valid decimal number.  Please try again."

                    else:
                        validResponse = True
                        break
            elif answerType == 'integer': # Number not a float, checks to see if it's an intenger...
                userResponse = c42Lib.isInteger(userResponse)
                if userResponse is None:
                    print "********** Not a valid integer.  Please try again."
                else:
                    validResponse = True
                    break

            elif answerType == 'bool':

                if userResponse == 'y' or \
                   userResponse == 'yes' or \
                   userResponse == '1' or \
                   userResponse == 'true':
                    userResponse = True

            else:
                # print "Check List..."
                for index, answer in enumerate(validAnswers):

                    if userResponse == answer:
                        validResponse = True

                        if answer == 'all':
                            userResponse = -1
                        break

                    else:
                        print "********** Not a valid response.  Please try again ( " + str(tryCount) + " of " + str(maxTries) + " tries remaining)."
                        print "           Valid answers include : " + str(validAnswers)

            if validResponse:
                #print "I got here..."
                break

            # If it gets here, it means that a valid response hasn't been provided
            # Re-ask the question...
            userResponse = raw_input(userQuestion).lower()

        #print "Try Count : " + str(tryCount)
        #print "Max Tries : " + str(maxTries)
        #print "    Valid : " + str(validResponse)

        if tryCount >= maxTries and not validResponse:
            print ""
            print "********** Too many bad input responses :\n"
            print "           " + str(userQuestion) + "\n"
            #print "           Quitting."
            #sys.exit()

        else:

            return userResponse 

    #Quick function to check if a string is an integer
    @staticmethod
    def isInteger(string):
        try: 
            int(string)
            return int(string)
        except ValueError:
            return None

    #Quick function to check if a string is a float
    @staticmethod
    def isFloat(string):
        try: 
            float(string)
            return float(string)
        except ValueError:
            return None

    # Some time functions for doing things like setting start, end, etc.
    @staticmethod
    def timeInfo(**kwargs):
        logging.debug ("[begin] timeInfo")

        timeThing = None

        if kwargs:
            logging.debug("        timeInfo - kwargs : " + str(kwargs))

            if 'now' in kwargs:
                timeThing = time.time()

            if 'start' in kwargs:
                c42Lib.cp_startTime = time.time()
            if 'end'   in kwargs:
                c42Lib.cp_endTime   = time.time()
            if 'elapsed' in kwargs and cpLib.cp_startTime:
                cpLib.cp_elapsedTime = time.time() - c42Lib.cp_startTime

            # Average time per event
            if 'count' in kwargs and c42Lib.cp_elapsedTime is not None:
                timeThing = cp_elapsedTime / kwargs['count']

            #Time remaning based on average time per event
            if 'numRemaining' in kwargs and 'aveTime' in kwargs:
                timeThing = aveTime * kwargs['numRemaining']
                
            # return a human readable format
            if 'fmt' in kwargs and timeThing is not None:
                timeThing = str(time.strftime('%H:%M:%S', time.gmtime(timeThing)))
            
        return timeThing

        logging.debug ("[end] timeInfo")

    @staticmethod
    def returnShortVersion(version):
        logging.debug('[begin] - returnShortVersion : ' + str(version))

        version = version[-3:]
        version = list(version)
        version = version[0]+"."+version[1]+"."+version[2]

        logging.debug('[  end] - returnShortVersion : ' + str(version))
        return version

    @staticmethod
    def dateCleanUp(rawDate):

        justTheDate = None

        if rawDate:

            justTheDate = rawDate[0:10] #Trim out date


        else:

            justTheDate = ""
        
        #sinceToday = int((datetime.today() - datetime.strptime(justTheDate , '%Y-%m-%d')).days)

        return justTheDate

    @staticmethod
    def killItPrompt(**kwargs):

        prompt = "K to end it now... "

        if kwargs and 'prompt' in kwargs:
            prompt = kwargs['prompt']

        shouldIDie = raw_input(prompt)

        if shouldIDie.lower() == 'k':
            sys.exit(0)


    @staticmethod
    def checkPyVersion(**kwargs):
        logging.info('[start] - checkPyVersion')
        logging.info("          " + str(sys.version_info))

        minPyVersion = 2
        pyOk = True

        if kwargs:
            logging.info("          kwargs : " + str(kwargs))
            if 'minPyVersion' in kwargs:
                minPyVersion = kwargs['minPyVerssion']

        # Assign version
        pyVersionMajor = sys.version_info.major
        pyVersionMinor = sys.version_info.minor
        pyVersionMicro = sys.version_info.micro

        pyVersionPretty = str(pyVersionMajor)+"."+str(pyVersionMinor)+"."+str(pyVersionMicro)

        if (minPyVersion < pyVersionMajor):

            logging.info("Python version not ok...  Exiting")
            pyOk = False

        if pyVersionMajor == 2:

            # Check if 2.7.9 or higher.  If not, then notify user and exit.
            if pyVersionMinor < 7 and pyVersionMicro < 9:
                pyOk = False
                logging.info("Python version not ok...  Exiting")


        if pyOk:
            print ('********** Minimum Python Version Required : 2.7. 9')
            print ('           Running Python Version : ' + pyVersionPretty + ' - Python version OK...')
        else:
            print ("********** This script requires Python 2.7.9 or higher.  You are running " + pyVersionPretty)
            print ("           Exiting.")
            sys.exit(0)
        
        logging.debug('  [end] - checkPyVersion')



# class UserClass(object)


# class OrgClass(object)

# class DeviceClass(object)