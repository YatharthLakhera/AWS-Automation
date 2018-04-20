# AWS-Automation
The script is for automating the starting and stopping of EC2 instances for AWS in ordered fashion using AWS cli.

**Requirement :**

It is recommended to use Python version greater or equal to 3.5 as the 
subprocess.run() function used in the program was added in Python 3.5 
so versions older than 3.5 will through exception on running this script.

AWS CLI should be installed and configured with the AWS account before 
using this script. Please refer the following links for more information :
- [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html)
- [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

**Assumption :**

> This script does not wait for the instance to start or stop.
> The script starts or stops the instance and move to next,  
> on recieving aws response that the instance is starting or stopping
> The moving to the next after the response is based on the assumption
> aws starting or stopping an instance takes around same time for all
> instance but the response time may vary due to user connection speed
> and thus the instance state will change in the same order
> in which they are give to the program. 

**Using Program :**

create the class object with the instance_list given as parameters

With delimiter in the _instance_list_ string as ',' : 
  ```
  instance_list = "i-b079f1cffd958d6aa,i-20be8080fda613954,i-9e1f6827c43e770bd"
  aws = EC2_sevices(instance_list)
  ```
With delimiter in the _instance_list_ string other than ',' : 
  ```
  instance_list = "i-b079f1cffd958d6aa i-20be8080fda613954 i-9e1f6827c43e770bd"
  aws = EC2_sevices(instance_list, ' ')
  ``` 
Now calling _instance()_ function :

1. _To start, stop or get status of the above instance :_
    ```
     aws.instance("start")
     aws.instance("stop")
     aws.instance("status")
     ```
2. _To start, stop or get status for instance :_
    ``` 
    aws.instance("start") # will start the list of the instance given in class obj
    aws.instance("status","i-b079f1cffd958d6aa,i-20be8080fda613954")
    aws.instance("stop","i-b079f1cffd958d6aa i-20be8080fda613954"," ")
    aws.instance("stop") # will stop the list of the instance given in class obj
    ```
    > The instance given in the function do not affect the initially given
    > in the class object.

**Program Details :**

Now, the program is fairly simple. It contains one function

Class :

*EC2_services(aws_cloud_instance, splt)*

1. _aws_cloud_instance_ : String type
   > This argument takes string containing the list of instance 
   > separated by a delimiter. Instance should be in 
   > the order which they need to be started or stopped.
2. _splt_ : String type(optional)
   > This argument takes the delimiter by which the list of
   > instance in the first argument is separated
   > Its default value is comma(,)

*Function Prototype :*

- instance(process, instance_list, splt)

1. _process_ : String type
   > This agruments takes the state to which you want to change the instance state
   >  - start : means the instance given will change to start state 
   >  - stop : means the instance given will change to stop state
   >  - status : will give the current status of the given instances

2. _instance_list_ : String type(Optional)
   > This argument takes string containing the list of instance 
   > separated by a delimiter. Instance should be in the order
   > which they need to be started or stopped. Instance list given 
   > in this argument will override the list given to the class
   > object. 
   > Note : This functionlity is to avoid changing the initial list
   >        of given instance. If there is a list of instance to be 
   >        started and after starting you need to know a one or more
   >        instance status without changing inital list, this help to
   >        achieve this.
3. _splt_ : String type(Optional)
   > This argument takes the delimiter by which the list of
   > instance in the instance list argument is separated
   > Its default value is comma(,) 
