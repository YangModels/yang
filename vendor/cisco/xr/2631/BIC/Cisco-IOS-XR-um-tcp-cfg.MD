## Cisco-IOS-XR-um-tcp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed debug directory config from UM model.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L73)	/tcp/path-mtu-discovery/age-timer
- (L105)	/tcp/throttle/low-water-mark
- (L114)	/tcp/throttle/high-water-mark
- (L150)	/tcp/num-thread/ingress-threads
- (L158)	/tcp/num-thread/max-threads
- (L231)	/pak-rate/tcp/stats-start/max-pkt-size/packet-size
- (L240)	/pak-rate/tcp/stats-start/max-pkt-size/max-pkt-rate

## XPaths Removed

- (L160)	/tcp/path-mtu-discovery/age-timer
- (L187)	/tcp/throttle
- (L234)	/tcp/num-thread
- (L280)	/tcp/ao/keychains/keychain[keychain-name]/keys/key[key-name]
- (L284)	/tcp/ao/keychains/keychain[keychain-name]/keys/key[key-name]/key-name
- (L266)	/tcp/ao/keychains/keychain[keychain-name]/keychain-name
- (L197)	/tcp/high-water-mark-throttling
- (L244)	/tcp/max-threads-in-thread-pool
- (L344)	/pak-rate/tcp/stats-start/max-pkt-size
- (L354)	/pak-rate/tcp/stats-start/max-pkt-rate
- (L45)	/
- (L50)	/service

## XPaths Modified

- (L49)	/tcp/window-size
- (L58)	/tcp/synwait-time
- (L72)	/tcp/path-mtu-discovery/age-timer
- (L72)	/tcp/path-mtu-discovery/age-timer
- (L89)	/tcp/receive-queue
- (L96)	/tcp/timestamp
- (L101)	/tcp/throttle
- (L124)	/tcp/selective-ack
- (L130)	/tcp/mss
- (L138)	/tcp/accept-rate
- (L146)	/tcp/num-thread
- (L175)	/tcp/ao/keychains/keychain[name]
- (L189)	/tcp/ao/keychains/keychain[name]/keys/key[key-id]
- (L200)	/tcp/ao/keychains/keychain[name]/keys/key[key-id]/send-id
- (L206)	/tcp/ao/keychains/keychain[name]/keys/key[key-id]/receive-id
- (L227)	/pak-rate/tcp/stats-start/max-pkt-size
- (L250)	/pak-rate/tcp/stats-start/rate-limit

