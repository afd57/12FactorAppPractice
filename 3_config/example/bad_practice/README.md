# Bad Practice

It is bad practice because configuration is grouped.

### Why is it bad practice?

This method does not scale cleanly: as more deploys of the app are created, new environment names are necessary, such as `staging` or `qa`. As the project grows further, developers may add their own special environments like joes-staging, resulting in a combinatorial explosion of config which makes managing deploys of the app very brittle.



`export myproject=test`, `export myproject=prod`

    > export myproject=test
    > python run.py
    ----Output-----
    ['localhost']
    1.1.1.1
    True
    
    > export myproject=prod
    > python run.py
    ----Output-----
    ['service_ip']
    headless.service.database
    False

**Note**

------------
> Don't forget, it may good practice in some case.
------------