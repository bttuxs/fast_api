from fastapi import APIRouter
from modules.hello import routes
router = APIRouter()

router.include_router(routes.router, prefix="/hello")
