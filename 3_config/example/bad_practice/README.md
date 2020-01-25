# Bad Practice

It is bad practice because configuration is grouped.

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