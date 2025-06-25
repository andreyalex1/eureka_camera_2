from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='realsense2_camera',
            executable='realsense2_camera_node',
            name='realsense2_camera',
            parameters=[
                {'enable_color': False},
                {'enable_depth': False},
                {'enable_infra1': True},
                {'enable_infra2': True},
                # Включение IR-освещения (если есть)
                {'enable_ir_emitter': True},
                # Отключение автоэкспозиции для стабильности
                {'auto_exposure': False},
                # Установка фиксированной экспозиции и усиления (подбирайте экспериментально)
                {'exposure': 15000},  # значение в миллисекундах, подбирайте
                {'gain': 20},          # значение усиления, подбирайте
            ],
            output='screen'
        ),
    ])