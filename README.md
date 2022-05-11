# Datascience Environment

Pre-reqs:

1. BigData environment - docker-compose
2. AWS cli. Data migration needs upload files to S3

## Steps

### Environment

   1. Create and enable Python Virtual Environment:

      ```sh
      python3 -m venv env
      source env/bin/activate
      pip install -r requirements.txt
      ```

### Preparing BigData Environment

1. Starting environment:

   ```sh
   docker-compose up -d
   ```

1. Generate Mysql data

   ```sh
   python3 src/inserts.py
   ```

### Jobs

Edit into jupyter notebook - <http://localhost:8888>

Show token:

```sh
docker logs jupyter 
```

### Notebooks

1. [Detect duplicities using TheFuzz](https://github.com/ortisan/datascience-environment/blob/main/data/jupyter/work/DuplicitiesTheFuzz.ipynb)

### Results

Use adminer to view results:

<http://localhost:8080/?server=mysql&username=root&db=persondb&sql=select%20*%20from%20person%0A%0A>

<http://localhost:8080/?server=mysql&username=root&db=persondb&sql=select%20*%20from%20phone%3B>

<http://localhost:8080/?server=mysql&username=root&db=persondb&sql=select%20*%20from%20address%3B>

### Usable commands and links

1. Glue sample:
<https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-samples-legislators.html>
