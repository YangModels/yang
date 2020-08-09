## Cisco-IOS-XE-call-home.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted


### Description

The node "/ios:native/ios:call-home/ios-ch:profile" and its sub-leaves are obsoleted.

### Reason

The node "/ios:native/ios:call-home/ios-ch:profile" and its sub-leaves are incorrectly implemented. There will be serious problems when netconf clients use it to configure call-home feature

- /native/call-home/ios-ch:profile
- /native/call-home/ios-ch:profile/ios-ch:active
- /native/call-home/ios-ch:profile/ios-ch:anonymous-reporting-only
- /native/call-home/ios-ch:profile/ios-ch:destination
- /native/call-home/ios-ch:profile/ios-ch:destination/ios-ch:address
- /native/call-home/ios-ch:profile/ios-ch:destination/ios-ch:address/ios-ch:email
- /native/call-home/ios-ch:profile/ios-ch:destination/ios-ch:address/ios-ch:http
- /native/call-home/ios-ch:profile/ios-ch:destination/ios-ch:transport-method
- /native/call-home/ios-ch:profile/ios-ch:profile-name
- /native/call-home/ios-ch:profile/ios-ch:reporting
- /native/call-home/ios-ch:profile/ios-ch:reporting/ios-ch:smart-call-home-data
- /native/call-home/ios-ch:profile/ios-ch:reporting/ios-ch:tac-sl-data
- /native/call-home/ios-ch:profile/ios-ch:reporting/ios-ch:user-sl-data
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:configuration
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:configuration/ios-ch:periodic
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:configuration/ios-ch:periodic/ios-ch:daily
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:configuration/ios-ch:periodic/ios-ch:daily/ios-ch:begin-time
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:configuration/ios-ch:periodic/ios-ch:monthly
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:configuration/ios-ch:periodic/ios-ch:monthly/ios-ch:begin-time
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:configuration/ios-ch:periodic/ios-ch:monthly/ios-ch:date
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:configuration/ios-ch:periodic/ios-ch:weekly
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:configuration/ios-ch:periodic/ios-ch:weekly/ios-ch:begin-time
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:configuration/ios-ch:periodic/ios-ch:weekly/ios-ch:day
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:diagnostic
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:diagnostic/ios-ch:severity
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:environment
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:environment/ios-ch:severity
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:inventory
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:inventory/ios-ch:periodic
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:inventory/ios-ch:periodic/ios-ch:daily
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:inventory/ios-ch:periodic/ios-ch:daily/ios-ch:begin-time
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:inventory/ios-ch:periodic/ios-ch:monthly
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:inventory/ios-ch:periodic/ios-ch:monthly/ios-ch:begin-time
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:inventory/ios-ch:periodic/ios-ch:monthly/ios-ch:date
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:inventory/ios-ch:periodic/ios-ch:weekly
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:inventory/ios-ch:periodic/ios-ch:weekly/ios-ch:begin-time
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:inventory/ios-ch:periodic/ios-ch:weekly/ios-ch:day
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:syslog
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:syslog/ios-ch:severity
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:syslog/ios-ch:severity/ios-ch:pattern
- /native/call-home/ios-ch:profile/ios-ch:subscribe-to-alert-group/ios-ch:syslog/ios-ch:severity/ios-ch:value
- /native/call-home/ios-ch:source-interface/ios-ch:TwentyFiveGigabitEthernet


## XPaths Deprecated

N/A

## XPaths Modified

### Description

Mandatory True added for the port node. 

### Reason

There is only one proxy-servers. Hence mandatory true added for the the port node.

- /native/call-home/ios-ch:http-proxy/ios-ch:proxy-servers/ios-ch:port


## XPaths Added

N/A
