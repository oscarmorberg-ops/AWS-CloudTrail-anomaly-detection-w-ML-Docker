#!/usr/bin/env python3
import boto3
import sys

print("🛡️ EC2 SECURITY SCANNER v2")
print("="*60)

ec2 = boto3.client('ec2')

response = ec2.describe_instances()
reservations = response['Reservations']

high_risk = []
for reservation in reservations:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        public_ip = instance.get('PublicIpAddress', 'None')
        
        print(f"\n🔍 {instance_id} | {state} | Public IP: {public_ip}")
        
        # 🚨 HIGH RISK: Public IP + Running
        if public_ip != 'None' and state == 'running':
            high_risk.append(instance_id)
            print("🚨 PUBLIC EXPOSURE DETECTED!")
        
        # Security Groups
        for sg in instance['SecurityGroups']:
            print(f"   SG: {sg['GroupId']}")

if high_risk:
    print(f"\n🚨 {len(high_risk)} HIGH RISK INSTANCES:")
    for instance in high_risk:
        print(f"   → {instance}")
else:
    print("\n✅ No public exposure detected!")
