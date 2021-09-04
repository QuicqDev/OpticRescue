# OpticRescue
Notification Application for something you want a constant reminder for.

#### Example Features: 
1. Constant reminder for taking a break from screen when you're in front of screen for too long
2. Push commits regularly or in regular intervals
3. Reminder to check logs/some important metrics
4. Drink water in intervals

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

## Profiling
### Time Profiling
![Time Profile](statics/time_profilev0-1.jpg)

### Memory Profiling
![memory](statics/memory_usagev1.jpg)

### Queries
```
# time profiling
kernprof -l -v optic.py --interval 2 --stop_iterations 5
# memory profiling
python -m memory_profiler optic.py --interval 2 --stop_iterations 5
# generate time vs memory
mprof run optic.py --interval 2 --stop_iterations 5
mprof plot
```

## Support
#### Windows
```
Edition	        Windows 10 Home Single Language
Version	        20H2
OS build        19042.1110
```

#### Linux
(In progress)


# ChangeLog

