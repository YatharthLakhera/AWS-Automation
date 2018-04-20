# Please update to version 3.5 or higher version of python 

import json
import sys
import os
import subprocess 
import time


class EC2_sevices :

	# The list of all the instance are needed to be passed as arguments
	# to the class object in the order which instance are to be 
	# started or stopped or get instance status
	def __init__(self, aws_cloud_instance="",splt=",") :
		self.aws_cloud_instance = aws_cloud_instance.split(splt)

	# Function to start, stop or get status of instances
	def instance(self, process="status", instance_list = "", splt=",") :

		# Choosing the instances to be processed
		if (instance_list != "") : 
			aws_cloud_instance_list = instance_list.split(splt)
		else :
			aws_cloud_instance_list = self.aws_cloud_instance

		count = 1
		for instance in aws_cloud_instance_list :

			start_time = time.time()

			instance_status = "waiting"

			while (instance_status == "waiting" ) :

				try :

					print("Instance {0}({1}) : {2} (Time Taken : {3:.2f} seconds)\r".format(count, instance,
					 instance_status, time.time()-start_time), end="")

					instance_process = ""
					instance_state = ""

					# Executing aws cli for starting instance and getting response
					if(process == "start") : 
						instance_process = "start-instances"
						instance_state = "StartingInstances"

					# Executing aws cli for stopping instance and getting response
					elif(process == "stop") :
						instance_process = "stop-instances"
						instance_state = "StoppingInstances"

					# Executing aws cli for getting instance status
					elif(process == "status") : 
						instance_process = "describe-instance-status"
						instance_state = "InstanceStatuses"

					else :
						print("Invalid instance state given in function arguments!")
						return

					read = subprocess.run(['aws', 'ec2', instance_process,
						'--instance-ids', instance], stdout=subprocess.PIPE)

					output = json.loads(read.stdout.decode("utf-8"))
					instance_status = output[instance_state][0]["CurrentState"]["Name"]

					if(instance_status == "pending") : 
						instance_status = "started"
				
				except :
					instance_status = "waiting"	
				
				print("Instance {0}({1}) : {2} (Time Taken : {3:.2f} seconds)".format(count, instance,
					 instance_status, time.time()-start_time))

			count += 1