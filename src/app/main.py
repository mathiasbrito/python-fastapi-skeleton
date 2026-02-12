import logging
import click
import uvicorn
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app import config, routes

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic: Start other processes or resources here
    logger.info("Server starting up...")
    try:
        yield
    except asyncio.CancelledError:
        pass
    finally:
        # Shutdown logic: Stop other processes or resources here
        logger.info("Server shutting down...")

app = FastAPI(lifespan=lifespan)
app.include_router(routes.router)

server = uvicorn.Server(
    uvicorn.Config(
        "app.main:app",
        port=int(config.APP_PORT),
        host=config.APP_HOST,
        log_config=config.APP_LOG_CONFIG_FILE,
        ws_ping_interval=1200,
        ws_ping_timeout=300,
    )
)


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        try:
            server.run()
        except (KeyboardInterrupt, asyncio.CancelledError):
            pass
        logger.info("Server is Shutdown!")

if __name__ == "__main__":
    cli()