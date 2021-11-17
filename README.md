> ## 🛠 Status: In Development
> Duka is currently in development. So we encourage you to use it and give us your feedback, but there are things that haven't been finalized yet and you can expect some changes.
>
> See the list of Known Issues and TODOs, below, for updates.

## Overview

Bus management system


## Getting Started

* Start services:

```bash
docker-compose build
docker-compose up
```

* After the all services are up and running, run migrate and add metadata:

```bash
cd hasura
hasura migrate apply --admin-secret admin
hasura metadata apply --admin-secret admin
```

P.S where `admin` is the **HASURA_GRAPHQL_ADMIN_SECRET**


* Running the hasura console:

```bash
hasura console --admin-secret admin
```


* Create a Bucket, go to [Minio dashboard][Minio] and follow the instructions:

![Screenshot](https://i.ibb.co/6wYd0q0/Screenshot-from-2021-09-27-17-33-55.png)
![Screenshot](https://i.ibb.co/tJY73QQ/Screenshot-from-2021-09-27-17-34-07.png)
![Screenshot](https://i.ibb.co/pynyg9Y/Screenshot-from-2021-09-27-17-34-27.png)
![Screenshot](https://i.ibb.co/YDCYgnx/Screenshot-from-2021-09-27-17-37-23.png)
![Screenshot](https://i.ibb.co/ySzkhHg/Screenshot-from-2021-09-27-17-35-01.png)



enjoy :)

# License: BSD-3


[Duka]: https://github.com/Mohamed-Kaizen/duka



[Minio]: http://storageui.localhost/



# TODO:

[X] Create the database Schema

[X] Add auth service

    [X] using username/phone_number and password

[ ] UseCase

    [X] Organization

        [X] Admin site create an organization
        
        [X] Organization manager can update organization information

        [X] Anyone can see the basic organization information
        
    [ ] Pickup

        [X] Admin site create an pick up service
        

        [X] Customer/operator/ticketer can select pick up service if they want to

    [ ] Notification


        [ ] System create the notification for events
        
        [X] User can see his own notification

    [ ] PaymentHistory

        [ ] System create the payment history after a transaction has been made

        [X] Bus Admin and managers in organization can see all the payment history

    [X] Passenger

        [X] Customer can create a passengers for a trip

        [X] Operator or ticketer can create a passengers for a trip

    [X] Ticket

        [X] Customer can create a ticket for trip

        [X] Ticketer can create a ticket for trip with Cash as the only payment method

        [X] Operator can create a ticket for trip, the same as customer

        [X] Customer can see all ticket that he buy

        [X] Ticketer can see all ticket that he created for a customer

        [X] Operator can see all ticket that he created for a customer

    [X] Seat

        [X] System create seats

        [X] Anyone can see list of seats per bus


    [X] Trip


        [X] Bus admin in organization create a trip


        [X] Customer/operator can see the trip basic information

        [X] Bus Admin can filter all trips within organization

        [X] Ticketer can only see trips within organization

    [X] Employ

        [X] Managers/bus_admin can add Employ within organization

        [X] Managers/bus_admin can see all employees within organization

        [X] Managers/bus_admin can update employee status

    [X] Bus

        [X] bus_admin create/update buses within organization

        [X] Customer/operator can see all bus basic information for trip

        [X] Ticketer can see all bus basic information for trip within organization

    [X] Route

        [X] Admin site can  create/update

        [X] Anyone can see all routes

    [X] Address

        [X] Admin site can  create/update

        [X] Anyone can see all address

    [ ] User

    [X] trip_bus

        [X] Bus_admin see/create/update trip bus within organization

        [X] Driver can see all his trips 

        [X] Driver/bus_admin can change the status

    [ ] trip_bus_seat

        [X] System assign seats to trip bus with available status

        [X] Customer can book an available

        [X] Driver can change a status of seat

        [ ] System can unbook a seat in case customer didn't pay before the payment dateline 


[ ] Duka service

    [ ] Ticket Endpoint

    [X] Seat creation Endpoint

    [X] trip_bus_seat creation Endpoint

    [ ] trip_bus_seat unbook Endpoint



[ ] Utils service

    [ ] Ticket code generation Endpoint

    [ ] payment Endpoint

    [ ] Notification Endpoint




[ ] Add Fake data


[ ] Testing the API's