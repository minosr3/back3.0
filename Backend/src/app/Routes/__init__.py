from flask import Blueprint

# Crea una instancia de Blueprint llamada "bp"
bp = Blueprint('mainBlueprint', __name__)

# Importa las rutas que deseas asociar con "bp"
from . import authRoutes
from . import UsersRoutes
from . import TicketsRoutes
from . import DistributorRoutes
from . import HostingRoutes
from . import DomainRoutes
from . import BuyoutRoutes
from . import CategoryRoutes
from . import CountryRoutes
from . import PayModeRoutes
from . import PlanRoutes
from . import PayPlanRoutes
from . import PlatformRoutes
from . import RolRoutes


# Agrega las rutas al Blueprint

mainRoute = bp