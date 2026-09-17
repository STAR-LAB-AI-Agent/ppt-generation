import os
from pathlib import Path
from datetime import datetime

def create_log(cmd, result, result_info):
    log_dir = Path(__file__).parent.parent / "logs"
    os.makedirs(log_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}.log"
    filepath = os.path.join(log_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("Skill调用日志\n")
        f.write(f"运行命令: {cmd}\n")
        if not result:
            f.write(f"PPT生成成功: {result_info}\n")
        else:
            f.write(f"PPT生成失败: {result_info}\n")
        f.write(f"调用时间: {datetime.now().isoformat()}\n")

    return filepath