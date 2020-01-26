# Good Practice


**The twelve-factor app stores config in environment variables** (often shortened to env vars or env). Env vars are easy to change between deploys without changing any code.

### Why is it good practice?

In a twelve-factor app, env vars are granular controls, each fully orthogonal to other env vars. They are never grouped together as “environments”, but instead are independently managed for each deploy. This is a model that scales up smoothly as the app naturally expands into more deploys over its lifetime.


    # Any variable setted
    > python3 run.py  
    -------------OUTPUT-------------
    all_ip_allowed
    localhost
    False
    
    -------- Setted DEBUG Flag as True --------
    >export DEBUG=TRUE
    > python3 run.py
    -------- OUTPUT --------
    all_ip_allowed
    localhost
    True
    
    -------- Setted ALLOWED_HOSTS Flag as True --------
    >export ALLOWED_HOSTS="1.2.3.4"
    > python3 run.py
    -------- OUTPUT --------
    1.2.3.4
    localhost
    True
    
    -------- Setted DATABASE_IP Flag as True --------
    > export DATABASE_IP="headless.service.database" 
    > python3 run.py
    -------- OUTPUT --------
    1.2.3.4
    headless.service.database
    True
    
