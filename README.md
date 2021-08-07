# OpticRescue
Save your precious eyes from strain


### Application User Model ID
[Official Docs](https://docs.microsoft.com/en-us/windows/configuration/find-the-application-user-model-id-of-an-installed-app)
```
#finding all AUMIDs
#open powershell as Admin
get-StartApps

#get specific program's APPID
get-StartApps <App Name>
#ex.
get-StartApps python
```