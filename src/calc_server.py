from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base


mcp = FastMCP("CalcMCPServer")

if __name__ == "__main__":
    mcp.run()

@mcp.tool()
def sum(a: int, b: int) -> int:
    """두 수의 합을 반환합니다.
    
    Args:
        a (int): 첫 번째 수
        b (int): 두 번째 수
        
    Returns:
        int: 두 수의 합
    """
    return a + b

@mcp.tool()
def sub(a: int, b: int) -> int:
    """두 수의 차를 반환합니다.
    
    Args:
        a (int): 첫 번째 수
        b (int): 두 번째 수

    Returns:
        int: 두 수의 차
    """        
    return a - b

@mcp.resource("calc://pi")
def pi() -> float:
    """원주율을 반환합니다.
    
    Returns:
        float: 원주율
    """
    return 3.141592653589793238462643383279502884197

@mcp.resource("calc://int/{value}")
def int(value: float) -> int:
    """주어진 값을 정수로 변환합니다.
    
    Args:
        value (float): 정수로 변환할 값

    Returns:
        int: 정수로 변환된 값
    """
    return int(value)

@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]