# py-http-header-content-generator 
### a.k.a test my server header size configuration
https://jazlopez.github.io/py-http-header-content-generator/

Script utility to create request header on the fly upon user provided length.
Request headers will ultimately send to an user defined endpoint and it will capture
the response.

### INSTALLATION

```shell
pip install -r requirements.txt
```

### USAGE
```shell
# example:
# create two request headers of size of 4kb each and send tem to url address defined by the user.
python main.py --url http://localhost:8080 --total 2 --size 4
```

### VERSION

1.0.0. Inicial

### CONTACT

Jaziel Lopez jazlopez @ github.com
