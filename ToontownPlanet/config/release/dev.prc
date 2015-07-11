# Distribution:
distribution dev

# Art assets:
model-path ../resources

# Server:
server-version Toontown Planet Beta
min-access-level 100
accountdb-type developer
shard-low-pop 50
shard-mid-pop 100
battle-input-timeout 42
#active-holidays 105

# RPC:
want-rpc-server #f
rpc-server-endpoint http://localhost:8080/

# DClass files (in reverse order):
dc-file astron/dclass/toon.dc
dc-file astron/dclass/otp.dc

# Core features:
want-pets #t
want-parties #t
want-cogdominiums #f
want-achievements #f
estate-day-night #t
want-mega-invasions #t
want-news-page #f


# Chat:
want-whitelist #t

# Cashbot boss:
want-resistance-toonup #t
want-resistance-restock #t

# Optional:
want-yin-yang #f

# Developer options:
show-population #t
force-skip-tutorial #t
want-instant-parties #t

# Chat:
want-whitelist #t
want-blacklist-sequence #f
