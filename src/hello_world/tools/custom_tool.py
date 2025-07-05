from crewai.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field

class HelloWorldArgsSchema(BaseModel):
    name: Optional[str] = Field(None, description="Name to greet.")

class HelloWorldTool(BaseTool):
    name: str = "hello_world"
    description: str = "Returns a friendly greeting."
    args_schema: Type[BaseModel] = HelloWorldArgsSchema

    def _run(self, name: Optional[str] = None) -> str:
        if name:
            return f"Hello, {name}!"
        else:
            return "Hello, world!"