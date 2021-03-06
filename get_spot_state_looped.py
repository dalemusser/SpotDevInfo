#Stephen Bowen 2021
import argparse
import sys
import time
import json

import bosdyn.client
import bosdyn.client.util
from bosdyn.client.robot_state import RobotStateClient


"""
    RUN CONCURRENTLY WITH SCRIPT THAT GENERATES MOVEMENT. WASD.py is recommended.

    This program tracks Spot's current state on a regular interval and prints it to the console.
    
"""
def main():

    # Parse command line args.
    parser = argparse.ArgumentParser()
    bosdyn.client.util.add_common_arguments(parser)
    parser.add_argument('--verbose-results', dest='verbose_results', action='store_true',
                        help='Print results of get_robot_state_async()')
    options = parser.parse_args()
    print_results = options.verbose_results

    # Create robot object with a robot_state_client.
    sdk = bosdyn.client.create_standard_sdk('RobotStateClient')
    robot = sdk.create_robot(options.hostname)

    #Authenticate
    robot.authenticate(options.username, options.password)
    robot_state_client = robot.ensure_client(RobotStateClient.default_service_name)

    #Create and populate stateArray at regular intervals
    stateArray = []
    while True:
        currentState = robot_state_client.get_robot_state() #Grab current robot state through BosDyn API (connected to spot)
        print(currentState)
        stateArray.append(currentState) #Not sure if we can append to the array as a different type. Might be worth looking into...
        time.sleep(1/24) # 1 / (states per second)
        #break Run 

if __name__ == "__main__":
    if not main():
        sys.exit(1)
