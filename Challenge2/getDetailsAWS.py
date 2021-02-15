# Query AWS ec2 for instance information
        my_aws_instances = subprocess.check_output("/home/XXXXX/.local/bin/aws ec2 describe-instances --region %s --profile %s" % (region, current_profile), shell=True)

        # Convert AWS json to python dictionary
        my_instance_dict = json.loads(my_aws_instances)

        # Pre-enter the 'Reservations' top level dictionary to make 'if' statement below cleaner.
        my_instances = my_instance_dict['Reservations']

        if my_instances:

            for my_instance in my_instances:

                if 'PublicIpAddress' in my_instance['Instances'][0]:
                    public_ip = my_instance['Instances'][0]['PublicIpAddress']
                else:
                    public_ip = "None"

                if 'PrivateIpAddress' in my_instance['Instances'][0]:
                    private_ip = my_instance['Instances'][0]['PrivateIpAddress']
                else:
                    private_ip = "None"

                if 'Tags' in my_instance['Instances'][0]:
                    tag_list = my_instance['Instances'][0]['Tags']

                     for tag in tag_list:
                        my_tag = tag.get('Key')

                        if my_tag == "Name":
                            instance_name = tag.get('Value')
                            break
                        else:
                            instance_name = "None"       

                state         = my_instance['Instances'][0]['State']['Name']
                instance_id   = my_instance['Instances'][0]['InstanceId']
                instance_type = my_instance['Instances'][0]['InstanceType']
