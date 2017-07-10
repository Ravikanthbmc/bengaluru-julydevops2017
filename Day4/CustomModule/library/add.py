from ansible.module_utils.basic import *

def add( ):

    module = AnsibleModule (
            argument_spec =  dict ( 
                     input1 = dict ( required=True, type='int' ),
                     input2 = dict ( required=True, type='int' )
            )
    )

    firstNumber = module.params['input1']
    secondNumber = module.params['input2']

    result = firstNumber + secondNumber

    response = { "Result": str( result ) }

    module.exit_json(changed=True, meta=response)
    #module.fail_json(msg="Fatal error")

if __name__ == "__main__":
    add()
