#!/usr/bin/env python 

from __future__ import unicode_literals, print_function 
import yaml 
import json 
 
def main(): 
    yaml_file = 'lee_test.yml' 
    json_file = 'lee_test.json' 
    
    my_dict = { 
        'ip_addr': '192.168.254.1', 
        'platform': 'local traffic manager', 
        'vendor':   'f5', 
        'model':    '5250' 
     } 
    
    my_list = [ 
        'first string', 
        425, 
        909, 
        my_dict, 
        'second string', 
        'last string' 
    ] 
 
    with open(yaml_file, "w") as f: 
        f.write(yaml.dump(my_list, default_flow_style=False)) 

    with open(json_file, "w") as f: 
        json.dump(my_list, f) 

if __name__ == "__main__": 
        main() 

