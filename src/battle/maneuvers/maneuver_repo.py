from reposition import Reposition
from rally import Rally
from swap import Swap
from push import Push
from fall_back import FallBack


maneuvers = {
    'reposition': Reposition(),
    'swap': Swap(),
    'push': Push(),
    'rally': Rally(),
    'fall_back': FallBack(),
}

