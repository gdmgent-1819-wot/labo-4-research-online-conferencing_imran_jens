# Research WOT

## Jens Rottiers, Imran Muhammad - New Media Development

**Assignment:** Create an online conferencing app via WebSockets en WebRTC via de PubNub-service

### What are WebSockets?
```
WebSockets are a way to communicate between a client (browser) and a server.
The communication is bidirectional (data flow goes both ways)

Famous examples: chats, multiplayer games, shared todolists.
```

### What is WebRTC?
```
WebRTC is an open source project that allows direct connection between browsers.
The difference with websockets is that the client can directly communicate with 
eachother before talking to the server.
This makes the communication faster then using websockets. Not much but a little bit.

Famous examples: livestreaming, videochat
Good example app: [ION](https://ion.ooo/#/)
```

### What is [PubNub](https://www.pubnub.com/)
```
PubNub is a global Data Stream Network (DSN) and realtime infrastructure-as-a-service (IaaS).
PubNub's primary product is a realtime publish/subscribe[4] messaging API.

Very handy tutorial: [Youtube](https://www.youtube.com/watch?v=UJCaLlDE1KM/)
```

### The solutions that are critcial for our application?
#### ChatEngine:
```
ChatEngine makes it easy to build powerful, cross-platform chat with PubNub. It provides essential components (messages, users, typing indicators), microservices infrastructure (chatbots and programmability) and the network to build and scale production-ready chat apps.
```

#### WebRTC and VoIP* Signaling:
``` 
Realtime signaling to establish connections and data channels for WebRTC and VoIP
```

*Voice over Internet Protocol