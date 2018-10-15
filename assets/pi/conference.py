from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
import logging
 
pnconfig = PNConfiguration()
pnconfig.publish_key = 'pub-c-e4663fda-6425-4855-b16e-486e3cdaeec7'
pnconfig.subscribe_key = 'sub-c-6fab9416-d075-11e8-b02a-a6a8b6327be1'
pnconfig.ssl = False
 
pubnub = PubNub(pnconfig)

# We can publish data to our channels
try:
    envelope = pubnub.publish().channel("my_channel").message({
        'name': 'JENS JONG',
        'online': True
    }).sync()
    print("publish timetoken: %d" % envelope.result.timetoken)
except PubNubException as e:
    handle_exception(e)

pubnub.subscribe().channels('my_channel').execute() 