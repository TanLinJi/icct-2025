import os
import subprocess

def crop_video(video_path, end_seconds):
    """
    裁剪视频到指定秒数
    :param video_path: 视频文件路径
    :param end_seconds: 要保留的秒数（从0开始到该秒数结束）
    """
    # 验证输入路径是否存在
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"视频文件不存在: {video_path}")
    
    # 获取视频目录和文件名信息
    dir_name = os.path.dirname(video_path)
    file_name = os.path.splitext(os.path.basename(video_path))[0]
    ext = os.path.splitext(video_path)[1]
    output_path = os.path.join(dir_name, f"{file_name}_cropped{ext}")
    
    # 构建FFmpeg命令
    cmd = [
        'ffmpeg',
        '-i', video_path,         # 输入文件
        '-t', str(end_seconds),   # 持续时间（秒）
        '-c', 'copy',             # 流复制（无需重新编码）
        '-y',                    # 覆盖输出文件（如果存在）
        output_path              # 输出文件路径
    ]
    
    try:
        # 执行FFmpeg命令
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"视频裁剪成功！保存至: {output_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        error_msg = f"裁剪失败: {e.stderr.decode('utf-8')}" if e.stderr else "裁剪失败"
        raise RuntimeError(error_msg)

# 使用示例
if __name__ == "__main__":
    video_path = "/home/jtl/embodied_models/src/data/tools/sam2/gui/videos/kitti_car.mp4"  # 替换为你的视频路径
    end_seconds = 5           # 要保留的秒数
    
    try:
        cropped_path = crop_video(video_path, end_seconds)
    except Exception as e:
        print(f"错误: {str(e)}")