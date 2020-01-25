from .base import *
# you need to set "myproject = 'prod'" as an environment variable
if os.environ['myproject'] == 'prod':
    from .prod import *
elif os.environ['myproject'] == 'test':
    from .test import *
else:
    from .dev import *
