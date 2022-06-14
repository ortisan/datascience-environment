# BigData Environment

Big Data Environment.

## Starting services

```sh
docker-compose up -d
```

![image](images/ecosystem.jpeg)

## WebUI Services

* HDFS *<http://localhost:50070>*
* Presto *<http://localhost:8080>*
* Hbase *<http://localhost:16010/master-status>*
* Mongo Express *<http://localhost:8081>*
* Kafka Manager *<http://localhost:9000>*
* Metabase *<http://localhost:3000>*
* Nifi *<http://localhost:9090>*
* Jupyter Spark *<http://localhost:8889>*
* Hue *<http://localhost:8888>*
* Spark *<http://localhost:4040>*

## Acesso por shell

### HDFS

```sh
docker exec -it datanode bash
```

### HBase

```sh
docker exec -it hbase-master bash
```

### Sqoop

docker exec -it datanode bash

### Kafka

```sh
docker exec -it kafka bash
```

## JDBC Access

### MySQL

```sh
jdbc:mysql://database/employees
```

##### Hive

```sh
jdbc:hive2://hive-server:10000/default
```

### Presto

```sh
jdbc:presto://presto:8080/hive/default
```

## Users and Passwords

### Hue

```sh
user: admin
pass: admin
```

### Metabase

```sh
user: bigdata@class.com
pass: bigdata123 
```

### MySQL

```sh
user: root
pass: secret
```

### MongoDB

```sh
user: root
pass: root
auth database: admin
```

Author [fabiogjardim](https://github.com/fabiogjardim/bigdata_docker)
