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
