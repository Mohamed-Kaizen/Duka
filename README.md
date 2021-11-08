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

[ ] Create the database Schema

[ ] Add auth service

    [ ] using username/phone_number and password

[ ] UseCase

    [ ] Organization

        [ ] Admin site create an organization
        
        [ ] Organization manager can update organization information

        [ ] Anyone can see the basic organization information
        
    [ ] Pickup

        [ ] Admin site create an pick up service
        

        [ ] Customer/operator/ticketer can select pick up service if they want to

    [ ] Notification


        [ ] System create the notification for events
        
        [ ] User can see his own notification

    [ ] PaymentHistory

        [ ] System create the payment history after a transaction has been made

        [ ] Bus Admin and managers in organization can see all the payment history

    [ ] Passenger

        [ ] Customer can create a passengers for a trip

        [ ] Operator or ticketer can create a passengers for a trip

    [ ] Ticket

        [ ] Customer can create a ticket for trip

        [ ] Ticketer can create a ticket for trip with Cash as the only payment method

        [ ] Operator can create a ticket for trip, the same as customer

        [ ] Customer can see all ticket that he buy

        [ ] Ticketer can see all ticket that he created for a customer

        [ ] Operator can see all ticket that he created for a customer

    [ ] Seat

        [ ] System create seats

        [ ] Anyone can see list of seats per bus


    [ ] Trip


        [ ] Bus admin in organization create a trip


        [ ] Customer/operator can see the trip basic information

        [ ] Bus Admin can filter all trips within organization

        [ ] Ticketer can only see trips within organization

    [ ] Employ

        [ ] Managers/bus_admin can add Employ within organization

        [ ] Managers/bus_admin can see all employees within organization

        [ ] Managers/bus_admin can update employee status

    [ ] Bus

        [ ] bus_admin create/update buses within organization

        [ ] Customer/operator can see all bus basic information for trip

        [ ] Ticketer can see all bus basic information for trip within organization

    [ ] Route

        [ ] Admin site can  create/update

        [ ] Anyone can see all routes

    [ ] Address

        [ ] Admin site can  create/update

        [ ] Anyone can see all address

    [ ] User

    [ ] trip_bus

        [ ] Bus_admin see/create/update trip bus within organization

        [ ] Driver can see all his trips 

        [ ] Driver/bus_admin can change the status

    [ ] trip_bus_seat

        [ ] System assign seats to trip bus with available status

        [ ] Customer can book an available

        [ ] Driver can change a status of seat

        [ ] System can unbook a seat in case customer didn't pay before the payment dateline 


[ ] Duka service

    [ ] Notification Endpoint

    [ ] Ticket Endpoint

    [ ] Seat creation Endpoint

    [ ] trip_bus_seat creation Endpoint

    [ ] trip_bus_seat unbook Endpoint



[ ] Utils service

    [ ] Ticket code generation Endpoint

    [ ] payment Endpoint




[ ] Add Fake data


[ ] Testing the API's