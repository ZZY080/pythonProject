import matplotlib.pyplot as plt

import numpy as np

class Car:
    def __init__(self, fuel_capacity, thrust_power):
        self.fuel_capacity = fuel_capacity  # 燃料容量，kg
        self.thrust_power = thrust_power  # 推力，N
        self.fuel_level = fuel_capacity  # 初始燃料量，kg

    def update_fuel_level(self, burn_rate, time_step):
        self.fuel_level = max(0, self.fuel_level - burn_rate * time_step)

    def simulate_flight(self, simulation_time, time_step, wind_speed):
        time_points = [0]
        altitude_points = [0]
        velocity_points = [0]

        time = 0
        velocity = 0
        altitude = 0

        while time < simulation_time and altitude >= 0:
            # 计算推力
            thrust = self.thrust_power - 9.8 * self.fuel_level

            # 风力发动机的影响
            wind_force = wind_speed * 0.5
            net_thrust = thrust - wind_force

            # 计算加速度
            acceleration = net_thrust / (self.fuel_level + 1e-5)

            # 更新速度和高度
            velocity = velocity + acceleration * time_step
            altitude = altitude + velocity * time_step

            # 更新燃料
            burn_rate = 0.1 * max(0, (self.fuel_capacity / 2 - self.fuel_level))
            self.update_fuel_level(burn_rate, time_step)

            # 更新时间
            time += time_step

            # 存储结果
            time_points.append(time)
            altitude_points.append(altitude)
            velocity_points.append(velocity)

        # 绘制结果
        plt.figure(figsize=(10, 6))
        plt.subplot(2, 1, 1)
        plt.plot(time_points, altitude_points)
        plt.title('Rocket Altitude Simulation')
        plt.xlabel('Time (s)')
        plt.ylabel('Altitude (m)')

        plt.subplot(2, 1, 2)
        plt.plot(time_points, velocity_points)
        plt.title('Rocket Velocity Simulation')
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (m/s)')

        plt.tight_layout()
        plt.show()

# 创建火箭对象
my_rocket = Car(fuel_capacity=100, thrust_power=500)

# 运行仿真
my_rocket.simulate_flight(simulation_time=60, time_step=1, wind_speed=5)
