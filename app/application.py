from contextlib import asynccontextmanager
from typing import Optional

from fastapi import Depends, FastAPI, Header, Body, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .config import Config, config


class Context:

    def __init__(self,cfg:Config):
        self.cfg = cfg

ctx = Context(
    cfg=config,
)

# 已下都是fastapi相关的
async def Setup(app:FastAPI):
    print("open ....")

async def Close(app:FastAPI):
    print("close .....")

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await Setup(app)  # 启动时运行
        yield
    finally:
        await Close(app)  # 结束时执行

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 中间件在这里配置
@app.middleware("http")
async def JwtAuth(request: Request, call_next):
    # 请求部分
    response = await call_next(request)
    # 响应部分
    return response


@app.get("/")
def read_root():
    return {"Hello": "World"}


class TestParams(BaseModel):
    v1: str
    timeout: Optional[int] = Field(300)

# 实例访问,包含了常用的资源获取, 如query, path, param, 
# {}路由的是资源
# Optional的是param参数
# 测试: curl -XPOST -H "content-type:application/json" --data '{"v1": "ok"}' 'http://127.0.0.1:9100/items/120?q1=1&q2=2&q=99'
@app.post("/items/{item_id}")
def read_item(request:Request, 
              body1:TestParams,  # post put body
              item_id: int,  # path
              q1: str,  # query
              q2: int,  # query
              q: Optional[str] = None,   # query
              authorization:str = Header(None),  # header
              ctx:Context = Depends(lambda: ctx)  # 注入依赖
              ):
    print("request: %s", request.headers)
    print("authorization: %s", authorization)

    return {"item_id": item_id, "q": q, "q1":q1, "q2": q2, "data": body1, "ctx": ctx}
