# Web Side Channel

## Side Channels
- Registration form using already registered license plate confirms that plate is already registered
- Adversary can park car with license plate registered to another user
    - If trying to park in a location where the car already is parked this will be confirmed to the advesary, and the location of the car leaked to the user

## Possible Exploit
- Order of registration inputs is such that if a novel username is provided, and two mismatched passwords, the response will confirm the existence of a registered plate
- There exist 6^14 ~= 7500000 plates, and with an average of 15000 requests/s for an express node.js server, all plate combinations can be checked in under 9 minutes
- All registered license plates can then be compiled by an adversary
- The advesary can then in linear time (14n) find the locations of all parked cars

## Mitigation
- Check that only a user can park a car with license plate registered to themselves
