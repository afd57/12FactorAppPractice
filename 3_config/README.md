# III. Config
Store config in the environment

An app’s config is everything that is likely to vary between deploys (staging, production, developer environments, etc). This includes:

- Resource handles to the database, Memcached, and other backing services
- Credentials
- etc

Apps sometimes store config as constants in the code. **This is a violation of twelve-factor**, which requires strict separation of config from code. Config varies substantially across deploys, code does not.

**The twelve-factor app stores config in environment variables (often shortened to env vars or env).** Env vars are easy to change between deploys without changing any code; unlike config files, there is little chance of them being checked into the code repo accidentally; and unlike custom config files, or other config mechanisms such as Java System Properties, they are a language- and OS-agnostic standard.

Another aspect of config management is grouping. Sometimes apps batch config into named groups (often called “environments”) named after specific deploys, such as the `development`, `test`, and `production` environments in Rails. This method does not scale cleanly: as more deploys of the app are created, new environment names are necessary, such as staging or qa. As the project grows further, developers may add their own special environments like joes-staging, resulting in a combinatorial explosion of config which makes managing deploys of the app very brittle.

In a twelve-factor app, env vars are granular controls, each fully orthogonal to other env vars. They are never grouped together as “environments”, but instead are independently managed for each deploy. This is a model that scales up smoothly as the app naturally expands into more deploys over its lifetime.

Source: https://12factor.net/config

Please check Good practice and bad practice.

### In bad practice 

You want to use a different database in test config. You have to change code to use this different database.

### Good Practice

You want to use a different database. 
Only you will set database ip adress to environment varible while run docker container. 
`docker run -e APP_ENV=“development” -e CONFIG_1=“VALUE_1”`