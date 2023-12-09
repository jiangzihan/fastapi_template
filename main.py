import uvicorn

from app import app, config


if __name__=="__main__":
    uvicorn.run(app,
                host=config.host,
                port=config.port,
                log_level=config.loglevel,   # warning, info, debug
                )
