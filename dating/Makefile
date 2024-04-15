dating-server:
	$(TROUPE)/bin/troupec dating-server.trp -o ./out/dating-server.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-server.js --id=../ids/id-server.json --trustmap=../trustmaps/client.json --aliases=aliases.json

dating-client-alice:
	$(TROUPE)/bin/troupec dating-client-alice.trp -o ./out/dating-client-alice.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-client-alice.js --id=../ids/id-client-alice.json --trustmap=../trustmaps/server-alice.json --alieases=aliases.json

dating-client-bob:
	$(TROUPE)/bin/troupec dating-client-bob.trp -o ./out/dating-client-bob.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-client-bob.js --id=../ids/id-client-bob.json --trustmap=../trustmaps/server-bob.json --alieases=aliases.json
